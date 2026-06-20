"""HR API with AI Timesheet Anomaly Detection and Leave Optimization."""
from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date

from app.db.session import get_db
from app.db.models import Employee, Department, Timesheet, LeaveRequest, EmployeeStatus
from app.api.v1.auth import get_current_user, require_role
from app.ai.agent_system import ai_orchestrator, AgentContext

router = APIRouter()

class EmployeeCreate(BaseModel):
    employee_code: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    department_id: Optional[str] = None
    job_title: str
    employment_type: str = "full_time"
    hire_date: str
    salary: Optional[float] = None
    pay_frequency: str = "monthly"
    manager_id: Optional[str] = None

class TimesheetCreate(BaseModel):
    employee_id: str
    week_start: str
    week_end: str
    entries: List[dict]

class LeaveRequestCreate(BaseModel):
    employee_id: str
    leave_type: str
    start_date: str
    end_date: str
    days_requested: int
    reason: Optional[str] = None

@router.get("/employees")
async def list_employees(status: Optional[str] = None, department: Optional[str] = None,
                         db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    query = select(Employee).where(Employee.tenant_id == current_user.tenant_id)
    if status:
        query = query.where(Employee.status == EmployeeStatus(status))
    if department:
        query = query.where(Employee.department_id == UUID(department))
    result = await db.execute(query)
    employees = result.scalars().all()
    return [{"id": str(e.id), "employee_code": e.employee_code, "first_name": e.first_name, "last_name": e.last_name,
             "email": e.email, "job_title": e.job_title, "status": e.status.value,
             "department_id": str(e.department_id) if e.department_id else None} for e in employees]

@router.post("/employees")
async def create_employee(employee: EmployeeCreate, db: AsyncSession = Depends(get_db),
                          current_user = Depends(require_role(["admin", "manager"]))):
    new_emp = Employee(tenant_id=current_user.tenant_id, employee_code=employee.employee_code,
                       first_name=employee.first_name, last_name=employee.last_name, email=employee.email,
                       phone=employee.phone, department_id=UUID(employee.department_id) if employee.department_id else None,
                       job_title=employee.job_title, employment_type=employee.employment_type,
                       hire_date=date.fromisoformat(employee.hire_date), salary=employee.salary,
                       pay_frequency=employee.pay_frequency, manager_id=UUID(employee.manager_id) if employee.manager_id else None)
    db.add(new_emp)
    await db.commit()
    await db.refresh(new_emp)
    return {"id": str(new_emp.id), "employee_code": new_emp.employee_code, "name": f"{new_emp.first_name} {new_emp.last_name}"}

@router.post("/timesheets")
async def submit_timesheet(timesheet: TimesheetCreate, db: AsyncSession = Depends(get_db),
                           current_user = Depends(get_current_user)):
    total_hours = sum(entry.get("hours", 0) for entry in timesheet.entries)
    regular_hours = min(total_hours, 40.0)
    overtime_hours = max(0, total_hours - 40.0)

    ts = Timesheet(employee_id=UUID(timesheet.employee_id), week_start=date.fromisoformat(timesheet.week_start),
                   week_end=date.fromisoformat(timesheet.week_end), total_hours=total_hours,
                   regular_hours=regular_hours, overtime_hours=overtime_hours, status="submitted")
    db.add(ts)
    await db.commit()

    if overtime_hours > 10 or total_hours > 60:
        ctx = AgentContext(tenant_id=str(current_user.tenant_id), user_id=str(current_user.id))
        await ai_orchestrator.execute("erp", "_timesheet_anomaly_detection",
                                       {"timesheets": [{"id": str(ts.id), "employee_id": timesheet.employee_id,
                                                        "total_hours": total_hours, "overtime": overtime_hours}]}, ctx)
    return {"id": str(ts.id), "total_hours": total_hours, "status": "submitted", "ai_flagged": overtime_hours > 10}

@router.post("/leave-requests")
async def request_leave(req: LeaveRequestCreate, db: AsyncSession = Depends(get_db),
                       current_user = Depends(get_current_user)):
    lr = LeaveRequest(employee_id=UUID(req.employee_id), leave_type=req.leave_type,
                      start_date=date.fromisoformat(req.start_date), end_date=date.fromisoformat(req.end_date),
                      days_requested=req.days_requested, reason=req.reason)
    db.add(lr)
    await db.commit()
    return {"id": str(lr.id), "status": "pending", "days": req.days_requested}

@router.post("/ai/leave-optimization")
async def ai_leave_optimization(db: AsyncSession = Depends(get_db),
                                current_user = Depends(require_role(["admin", "manager"]))):
    result = await db.execute(select(LeaveRequest).where(LeaveRequest.status == "pending"))
    requests = result.scalars().all()
    req_data = [{"request_id": str(r.id), "employee_id": str(r.employee_id), "leave_type": r.leave_type,
                 "start_date": r.start_date.isoformat(), "days": r.days_requested} for r in requests]
    ctx = AgentContext(tenant_id=str(current_user.tenant_id), user_id=str(current_user.id))
    result = await ai_orchestrator.execute("erp", "_leave_optimization",
                                           {"leave_requests": req_data, "staffing_requirements": {"min_per_dept": 3}}, ctx)
    return result.get("output", {})

@router.get("/dashboard")
async def hr_dashboard(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    total_employees = await db.execute(select(func.count(Employee.id)).where(Employee.tenant_id == current_user.tenant_id))
    active = await db.execute(select(func.count(Employee.id)).where(
        Employee.tenant_id == current_user.tenant_id, Employee.status == EmployeeStatus.ACTIVE))
    pending_leave = await db.execute(select(func.count(LeaveRequest.id)).where(LeaveRequest.status == "pending"))
    return {"total_employees": total_employees.scalar() or 0, "active_employees": active.scalar() or 0,
            "pending_leave_requests": pending_leave.scalar() or 0, "ai_insight": "Timesheets flagged for review."}
