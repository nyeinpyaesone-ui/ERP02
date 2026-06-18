Content from the zip file `None`:

## File: README.md

# AI-ERP System v2.2

Enterprise Resource Planning with AI-powered features, PWA support, Stripe payments, workflow automation, and predictive analytics.

## Features

- **Core ERP**: CRM, HR, Inventory, Finance, Projects
- **AI Chat**: Business intelligence assistant with Ollama
- **Document RAG**: Upload, chunk, embed, and search documents
- **Reports & Charts**: Revenue, pipeline, inventory analytics
- **Workflow Automation**: Trigger-based approvals and actions
- **Stripe Payments**: Invoice payments with webhooks
- **PWA**: Offline support, installable, background sync
- **AI Forecasting**: Revenue prediction, inventory risk, churn analysis
- **Bulk Import/Export**: CSV, Excel, JSON for 9 entity types
- **Alembic Migrations**: Schema evolution with version control
- **Real-time**: WebSocket notifications
- **Integrations**: Slack, Teams, Zapier, custom webhooks

## Architecture

```
ai-erp-system/
в”њв”Ђв”Ђ backend/                 # FastAPI + SQLAlchemy + PostgreSQL
в”‚   в”њв”Ђв”Ђ app/
в”‚   в”‚   в”њв”Ђв”Ђ main.py           # FastAPI app with 16 routers
в”‚   в”‚   в”њв”Ђв”Ђ config.py         # Pydantic settings
в”‚   в”‚   в”њв”Ђв”Ђ database.py       # SQLAlchemy engine & session
в”‚   в”‚   в”њв”Ђв”Ђ auth.py           # JWT, bcrypt, role guards
в”‚   в”‚   в”њв”Ђв”Ђ models.py         # 20+ SQLAlchemy models
в”‚   в”‚   в”њв”Ђв”Ђ routers/          # 16 API routers
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ auth.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ crm.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ hr.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ inventory.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ finance.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ projects.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ ai.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ documents.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ reports.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ workflows.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ payments.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ integrations.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ analytics.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ admin.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ websocket.py
в”‚   в”‚   в”‚   в”њв”Ђв”Ђ bulk_import_export.py
в”‚   в”‚   в”‚   в””в”Ђв”Ђ migrations.py
в”‚   в”‚   в””в”Ђв”Ђ services/
в”‚   в”‚       в”њв”Ђв”Ђ activity_log.py
в”‚   в”‚       в””в”Ђв”Ђ bulk_import_export.py
в”‚   в”њв”Ђв”Ђ alembic/              # Database migrations
в”‚   в”‚   в”њв”Ђв”Ђ env.py
в”‚   в”‚   в”њв”Ђв”Ђ script.py.mako
в”‚   в”‚   в””в”Ђв”Ђ versions/
в”‚   в”‚       в””в”Ђв”Ђ 001_initial_migration.py
в”‚   в”њв”Ђв”Ђ alembic.ini
в”‚   в”њв”Ђв”Ђ requirements.txt
в”‚   в”њв”Ђв”Ђ Dockerfile
в”‚   в””в”Ђв”Ђ .env.example
в”њв”Ђв”Ђ frontend-react/           # React 18 + Vite + Tailwind
в”‚   в”њв”Ђв”Ђ src/
в”‚   в”‚   в”њв”Ђв”Ђ main.jsx
в”‚   в”‚   в”њв”Ђв”Ђ App.jsx
в”‚   в”‚   в”њв”Ђв”Ђ index.css
в”‚   в”‚   в”њв”Ђв”Ђ components/
в”‚   в”‚   в”‚   в””в”Ђв”Ђ Layout.jsx
в”‚   в”‚   в””в”Ђв”Ђ pages/
в”‚   в”‚       в”њв”Ђв”Ђ Login.jsx
в”‚   в”‚       в”њв”Ђв”Ђ Dashboard.jsx
в”‚   в”‚       в”њв”Ђв”Ђ CRM.jsx
в”‚   в”‚       в”њв”Ђв”Ђ HR.jsx
в”‚   в”‚       в”њв”Ђв”Ђ Inventory.jsx
в”‚   в”‚       в”њв”Ђв”Ђ Finance.jsx
в”‚   в”‚       в”њв”Ђв”Ђ Projects.jsx
в”‚   в”‚       в”њв”Ђв”Ђ Reports.jsx
в”‚   в”‚       в”њв”Ђв”Ђ Analytics.jsx
в”‚   в”‚       в”њв”Ђв”Ђ AIChat.jsx
в”‚   в”‚       в”њв”Ђв”Ђ Documents.jsx
в”‚   в”‚       в”њв”Ђв”Ђ Workflows.jsx
в”‚   в”‚       в”њв”Ђв”Ђ Integrations.jsx
в”‚   в”‚       в”њв”Ђв”Ђ Settings.jsx
в”‚   в”‚       в”њв”Ђв”Ђ BulkImportExport.jsx
в”‚   в”‚       в””в”Ђв”Ђ MigrationManager.jsx
в”‚   в”њв”Ђв”Ђ public/
в”‚   в”‚   в”њв”Ђв”Ђ manifest.json
в”‚   в”‚   в””в”Ђв”Ђ sw.js
в”‚   в”њв”Ђв”Ђ package.json
в”‚   в”њв”Ђв”Ђ vite.config.js
в”‚   в”њв”Ђв”Ђ tailwind.config.js
в”‚   в”њв”Ђв”Ђ Dockerfile
в”‚   в””в”Ђв”Ђ nginx.conf
в””в”Ђв”Ђ docker-compose.yml
```

## Quick Start

### Local Development

```bash
# 1. Start PostgreSQL and Redis
docker-compose up -d db redis

# 2. Backend
cd backend
cp .env.example .env
pip install -r requirements.txt
alembic -c alembic.ini upgrade head
uvicorn app.main:app --reload --port 8000

# 3. Frontend (new terminal)
cd frontend-react
npm install
npm run dev

# 4. Open http://localhost:3000
```

### Docker (Full Stack)

```bash
docker-compose up -d
docker-compose exec ollama ollama pull qwen3.6
```

### First Time Setup

```bash
# Create admin user via API
curl -X POST http://localhost:8000/api/v1/auth/register   -H "Content-Type: application/json"   -d '{"email":"admin@company.com","password":"admin123","full_name":"Admin User","role":"admin"}'
```

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login (OAuth2)
- `GET /api/v1/auth/me` - Current user
- `GET /api/v1/auth/users` - List users (admin)

### CRM
- `GET/POST /api/v1/crm/contacts`
- `GET/POST /api/v1/crm/companies`
- `GET/POST /api/v1/crm/deals`
- `GET /api/v1/crm/deals/pipeline`
- `GET /api/v1/crm/dashboard`

### HR
- `GET/POST /api/v1/hr/departments`
- `GET/POST /api/v1/hr/employees`
- `GET /api/v1/hr/dashboard`

### Inventory
- `GET/POST /api/v1/inventory/products`
- `GET/POST /api/v1/inventory/movements`
- `GET /api/v1/inventory/dashboard`

### Finance
- `GET/POST /api/v1/finance/invoices`
- `POST /api/v1/finance/payments`
- `GET /api/v1/finance/dashboard`

### Projects
- `GET/POST /api/v1/projects/projects`
- `GET/POST /api/v1/projects/tasks`
- `GET /api/v1/projects/dashboard`

### AI
- `POST /api/v1/ai/chat` - AI business assistant
- `GET /api/v1/ai/insights` - Executive insights
- `GET /api/v1/ai/forecast/revenue` - Revenue forecasting

### Documents
- `POST /api/v1/documents/upload`
- `GET /api/v1/documents/documents`

### Reports
- `GET /api/v1/reports/revenue`
- `GET /api/v1/reports/pipeline`
- `GET /api/v1/reports/inventory`
- `GET /api/v1/reports/chart/revenue`

### Workflows
- `GET/POST /api/v1/workflows/workflows`
- `GET/POST /api/v1/workflows/executions`

### Payments (Stripe)
- `POST /api/v1/payments/create-intent`
- `POST /api/v1/payments/webhook`

### Integrations
- `GET/POST /api/v1/integrations/integrations`
- `GET/POST /api/v1/integrations/webhooks`

### Analytics
- `GET /api/v1/analytics/dashboard`
- `GET /api/v1/analytics/monthly-trends`

### Admin
- `GET/POST /api/v1/admin/settings`
- `GET /api/v1/admin/activity-logs`
- `GET /api/v1/admin/notifications`
- `GET /api/v1/admin/stats`

### Advanced Search (`/api/v1/search`)
- `POST /` вЂ” Full-text search with filters, facets, pagination
- `GET /?q=` вЂ” GET search endpoint for browser integration
- `GET /suggestions?q=` вЂ” Autocomplete suggestions
- `GET /facets` вЂ” Facet counts for filters
- `POST /reindex` вЂ” Reindex all entities (admin)
- `POST /index/{type}/{id}` вЂ” Index specific entity (admin)
- `GET /analytics` вЂ” Search analytics dashboard
- `GET /analytics/popular-queries` вЂ” Most popular queries

### LLM Integration (`/api/v1/llm`)
- `GET /models` вЂ” List configured models with availability status
- `PUT /models/{id}` вЂ” Update model configuration
- `POST /models/{id}/pull` вЂ” Pull model from Ollama
- `DELETE /models/{id}` вЂ” Remove model configuration
- `POST /chat` вЂ” Send chat with tool support
- `POST /chat/stream` вЂ” Stream chat response (SSE)
- `GET /conversations` вЂ” List user's conversations
- `GET /conversations/{id}` вЂ” Get conversation with messages
- `POST /conversations` вЂ” Create new conversation
- `PUT /conversations/{id}/archive` вЂ” Archive conversation
- `DELETE /conversations/{id}` вЂ” Delete conversation
- `GET /templates` вЂ” List prompt templates
- `GET /templates/{name}` вЂ” Get template
- `POST /templates` вЂ” Create template (admin)
- `DELETE /templates/{id}` вЂ” Delete template (admin)
- `GET /analytics/usage` вЂ” LLM usage analytics
- `GET /analytics/conversations` вЂ” Conversation statistics

### Permissions & RBAC (`/api/v1/permissions`)
- `GET /roles` вЂ” List all roles with permissions
- `POST /roles` вЂ” Create new role
- `GET /roles/{id}` вЂ” Get role details
- `PUT /roles/{id}` вЂ” Update role
- `DELETE /roles/{id}` вЂ” Delete role (superadmin only)
- `GET /permissions` вЂ” List all permissions
- `POST /roles/{id}/permissions` вЂ” Assign permissions to role
- `GET /users/{id}/roles` вЂ” Get user's roles
- `POST /users/{id}/roles` вЂ” Assign roles to user
- `GET /field-permissions` вЂ” List field-level permissions
- `POST /field-permissions` вЂ” Create field permission
- `DELETE /field-permissions/{id}` вЂ” Delete field permission
- `GET /data-policies` вЂ” List data policies
- `POST /data-policies` вЂ” Create data policy
- `PUT /data-policies/{id}/toggle` вЂ” Toggle policy
- `DELETE /data-policies/{id}` вЂ” Delete policy
- `GET /me` вЂ” Get current user's permissions and roles

### Bulk Import/Export
- `POST /api/v1/bulk/import/{entity_type}` - Import CSV/Excel
- `POST /api/v1/bulk/import/{entity_type}/preview` - Validate preview
- `GET /api/v1/bulk/export/{entity_type}?format=` - Export CSV/XLSX/JSON
- `GET /api/v1/bulk/templates/{entity_type}` - Download templates
- `GET /api/v1/bulk/entity-configs` - Field definitions
- `GET /api/v1/bulk/import-history` - Import history

### Migrations (Admin Only)
- `GET /api/v1/migrations/status` - Migration status
- `GET /api/v1/migrations/history` - Revision history
- `GET /api/v1/migrations/versions` - Migration files
- `POST /api/v1/migrations/upgrade` - Apply migrations
- `POST /api/v1/migrations/downgrade` - Revert migrations
- `POST /api/v1/migrations/create` - Create new migration
- `POST /api/v1/migrations/stamp` - Stamp revision

### WebSocket
- `WS /api/v1/ws/{client_id}` - Real-time connection

## Database Schema

20+ tables including:
- `users`, `contacts`, `companies`, `deals`
- `departments`, `employees`
- `products`, `inventory_movements`
- `invoices`, `invoice_items`, `payments`
- `projects`, `tasks`
- `documents`
- `workflows`, `workflow_steps`, `workflow_executions`
- `webhooks`, `webhook_deliveries`
- `integrations`
- `activity_logs`, `notifications`
- `reports`, `forecasts`
- `settings`

## Build History

| Version | Feature | Files |
|---------|---------|-------|
| v1.0 | Core ERP + AI Chat | 45 |
| v1.1 | PostgreSQL, Redis, Email | 55 |
| v1.2 | Document Upload, RAG | 65 |
| v1.3 | Reports, Charts, WebSocket | 75 |
| v1.4 | Workflow Automation | 79 |
| v1.5 | React Frontend | 100 |
| v1.6 | Stripe Payments | 102 |
| v1.7 | PWA + AI Forecasting | 109 |
| v2.2 | Alembic Migrations + Bulk Import/Export | 117 |

## License

MIT

## File: docker-compose.yml

version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: erp_user
      POSTGRES_PASSWORD: erp_password
      POSTGRES_DB: erp_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://erp_user:erp_password@db:5432/erp_db
      - REDIS_URL=redis://redis:6379/0
      - OLLAMA_BASE_URL=http://ollama:11434
    depends_on:
      - db
      - redis
      - ollama
    volumes:
      - ./uploads:/app/uploads

  frontend:
    build: ./frontend-react
    ports:
      - "3000:3000"
    depends_on:
      - backend

volumes:
  postgres_data:
  ollama_data:

## File: backend/.env.example

# Database
DATABASE_URL=postgresql://erp_user:erp_password@localhost:5432/erp_db

# Redis
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=your-super-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Email
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=
SMTP_PASSWORD=
SMTP_FROM=noreply@ai-erp.local

# AI / Ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1

# Stripe
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
STRIPE_PUBLISHABLE_KEY=pk_test_...

# File Upload
UPLOAD_DIR=./uploads
MAX_UPLOAD_SIZE=52428800

## File: backend/Dockerfile

FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p uploads static

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

## File: backend/app/models.py

from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime, Date,
    Numeric, ForeignKey, Index, Float, LargeBinary
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False, server_default="user")
    is_active = Column(Boolean, nullable=False, server_default="true")
    avatar_url = Column(String(500), nullable=True)
    last_login = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    contacts = relationship("Contact", back_populates="assigned_user", foreign_keys="Contact.assigned_to")
    deals = relationship("Deal", back_populates="assigned_user", foreign_keys="Deal.assigned_to")
    projects_managed = relationship("Project", back_populates="manager", foreign_keys="Project.manager_id")
    tasks = relationship("Task", back_populates="assigned_user", foreign_keys="Task.assigned_to")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    activity_logs = relationship("ActivityLog", back_populates="user")

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    industry = Column(String(100), nullable=True)
    size = Column(String(50), nullable=True)
    website = Column(String(255), nullable=True)
    address = Column(Text, nullable=True)
    phone = Column(String(50), nullable=True)
    logo_url = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    contacts = relationship("Contact", back_populates="company")
    deals = relationship("Deal", back_populates="company")
    invoices = relationship("Invoice", back_populates="company")

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), index=True, nullable=True)
    phone = Column(String(50), nullable=True)
    title = Column(String(100), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="SET NULL"), nullable=True)
    status = Column(String(50), nullable=False, server_default="lead")
    source = Column(String(100), nullable=True)
    notes = Column(Text, nullable=True)
    assigned_to = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    lifetime_value = Column(Numeric(15, 2), nullable=False, server_default="0")
    last_activity = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    company = relationship("Company", back_populates="contacts")
    assigned_user = relationship("User", back_populates="contacts", foreign_keys=[assigned_to])
    deals = relationship("Deal", back_populates="contact")
    invoices = relationship("Invoice", back_populates="contact")

class Deal(Base):
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    contact_id = Column(Integer, ForeignKey("contacts.id", ondelete="SET NULL"), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="SET NULL"), nullable=True)
    value = Column(Numeric(15, 2), nullable=False, server_default="0")
    stage = Column(String(50), nullable=False, server_default="prospect")
    probability = Column(Integer, nullable=False, server_default="0")
    expected_close_date = Column(Date, nullable=True)
    actual_close_date = Column(Date, nullable=True)
    assigned_to = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    contact = relationship("Contact", back_populates="deals")
    company = relationship("Company", back_populates="deals")
    assigned_user = relationship("User", back_populates="deals", foreign_keys=[assigned_to])

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    manager_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    budget = Column(Numeric(15, 2), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    manager = relationship("User", foreign_keys=[manager_id])
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    employee_code = Column(String(50), unique=True, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)
    job_title = Column(String(100), nullable=False)
    salary = Column(Numeric(15, 2), nullable=True)
    hire_date = Column(Date, nullable=False)
    status = Column(String(50), nullable=False, server_default="active")
    employment_type = Column(String(50), nullable=False, server_default="full_time")
    address = Column(Text, nullable=True)
    emergency_contact = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    department = relationship("Department", back_populates="employees")
    user = relationship("User", foreign_keys=[user_id])

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(100), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String(100), nullable=True)
    unit_price = Column(Numeric(15, 2), nullable=False, server_default="0")
    cost_price = Column(Numeric(15, 2), nullable=True)
    quantity_in_stock = Column(Integer, nullable=False, server_default="0")
    reorder_level = Column(Integer, nullable=False, server_default="10")
    reorder_quantity = Column(Integer, nullable=False, server_default="50")
    supplier = Column(String(255), nullable=True)
    supplier_contact = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False, server_default="active")
    barcode = Column(String(100), nullable=True)
    weight = Column(Float, nullable=True)
    dimensions = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    movements = relationship("InventoryMovement", back_populates="product", cascade="all, delete-orphan")
    invoice_items = relationship("InvoiceItem", back_populates="product")

class InventoryMovement(Base):
    __tablename__ = "inventory_movements"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    movement_type = Column(String(50), nullable=False)  # in, out, adjustment, transfer
    quantity = Column(Integer, nullable=False)
    unit_cost = Column(Numeric(15, 2), nullable=True)
    reference = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    product = relationship("Product", back_populates="movements")
    creator = relationship("User", foreign_keys=[created_by])

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String(100), unique=True, nullable=False)
    contact_id = Column(Integer, ForeignKey("contacts.id", ondelete="SET NULL"), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="SET NULL"), nullable=True)
    issue_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    subtotal = Column(Numeric(15, 2), nullable=False, server_default="0")
    tax_rate = Column(Numeric(5, 2), nullable=False, server_default="0")
    tax_amount = Column(Numeric(15, 2), nullable=False, server_default="0")
    total = Column(Numeric(15, 2), nullable=False, server_default="0")
    amount_paid = Column(Numeric(15, 2), nullable=False, server_default="0")
    status = Column(String(50), nullable=False, server_default="draft")
    notes = Column(Text, nullable=True)
    terms = Column(Text, nullable=True)
    stripe_payment_intent_id = Column(String(255), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    contact = relationship("Contact", back_populates="invoices")
    company = relationship("Company", back_populates="invoices")
    items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="invoice", cascade="all, delete-orphan")

class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="SET NULL"), nullable=True)
    description = Column(Text, nullable=False)
    quantity = Column(Numeric(10, 2), nullable=False)
    unit_price = Column(Numeric(15, 2), nullable=False)
    total = Column(Numeric(15, 2), nullable=False)

    invoice = relationship("Invoice", back_populates="items")
    product = relationship("Product", back_populates="invoice_items")

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id", ondelete="CASCADE"), nullable=False)
    amount = Column(Numeric(15, 2), nullable=False)
    payment_method = Column(String(50), nullable=False)
    payment_date = Column(Date, nullable=False)
    stripe_payment_intent_id = Column(String(255), nullable=True)
    stripe_charge_id = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False, server_default="completed")
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    invoice = relationship("Invoice", back_populates="payments")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), nullable=False, server_default="planning")
    priority = Column(String(50), nullable=False, server_default="medium")
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    budget = Column(Numeric(15, 2), nullable=True)
    actual_cost = Column(Numeric(15, 2), nullable=True)
    progress = Column(Integer, nullable=False, server_default="0")
    manager_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    client_id = Column(Integer, ForeignKey("contacts.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    manager = relationship("User", back_populates="projects_managed", foreign_keys=[manager_id])
    client = relationship("Contact", foreign_keys=[client_id])
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), nullable=False, server_default="todo")
    priority = Column(String(50), nullable=False, server_default="medium")
    assigned_to = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    due_date = Column(Date, nullable=True)
    estimated_hours = Column(Numeric(8, 2), nullable=True)
    actual_hours = Column(Numeric(8, 2), nullable=True)
    parent_task_id = Column(Integer, ForeignKey("tasks.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    project = relationship("Project", back_populates="tasks")
    assigned_user = relationship("User", back_populates="tasks", foreign_keys=[assigned_to])
    subtasks = relationship("Task", backref="parent", remote_side=[id])

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_size = Column(Integer, nullable=True)
    mime_type = Column(String(100), nullable=True)
    entity_type = Column(String(50), nullable=True)  # contact, company, project, etc.
    entity_id = Column(Integer, nullable=True)
    embedding_id = Column(String(255), nullable=True)
    extracted_text = Column(Text, nullable=True)
    uploaded_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    uploader = relationship("User", foreign_keys=[uploaded_by])

class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    entity_type = Column(String(50), nullable=False)  # invoice, deal, task, etc.
    trigger_type = Column(String(50), nullable=False)  # on_create, on_update, scheduled, manual
    trigger_condition = Column(JSONB, nullable=True)
    is_active = Column(Boolean, nullable=False, server_default="true")
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    creator = relationship("User", foreign_keys=[created_by])
    steps = relationship("WorkflowStep", back_populates="workflow", cascade="all, delete-orphan")
    executions = relationship("WorkflowExecution", back_populates="workflow", cascade="all, delete-orphan")

class WorkflowStep(Base):
    __tablename__ = "workflow_steps"

    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(Integer, ForeignKey("workflows.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    step_type = Column(String(50), nullable=False)  # approval, condition, action, notification, delay
    step_order = Column(Integer, nullable=False)
    config = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    workflow = relationship("Workflow", back_populates="steps")

class WorkflowExecution(Base):
    __tablename__ = "workflow_executions"

    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(Integer, ForeignKey("workflows.id", ondelete="CASCADE"), nullable=False)
    entity_type = Column(String(50), nullable=False)
    entity_id = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False, server_default="running")
    current_step = Column(Integer, nullable=False, server_default="0")
    context = Column(JSONB, nullable=True)
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)

    workflow = relationship("Workflow", back_populates="executions")

class Webhook(Base):
    __tablename__ = "webhooks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    url = Column(String(500), nullable=False)
    events = Column(JSONB, nullable=False)  # ["invoice.created", "deal.won"]
    secret = Column(String(255), nullable=True)
    is_active = Column(Boolean, nullable=False, server_default="true")
    retry_count = Column(Integer, nullable=False, server_default="3")
    last_triggered = Column(DateTime(timezone=True), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    creator = relationship("User", foreign_keys=[created_by])
    deliveries = relationship("WebhookDelivery", back_populates="webhook", cascade="all, delete-orphan")

class WebhookDelivery(Base):
    __tablename__ = "webhook_deliveries"

    id = Column(Integer, primary_key=True, index=True)
    webhook_id = Column(Integer, ForeignKey("webhooks.id", ondelete="CASCADE"), nullable=False)
    event = Column(String(100), nullable=False)
    payload = Column(JSONB, nullable=False)
    response_status = Column(Integer, nullable=True)
    response_body = Column(Text, nullable=True)
    attempt = Column(Integer, nullable=False, server_default="1")
    status = Column(String(50), nullable=False, server_default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    webhook = relationship("Webhook", back_populates="deliveries")

class Integration(Base):
    __tablename__ = "integrations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    provider = Column(String(100), nullable=False)  # slack, teams, zapier, generic
    config = Column(JSONB, nullable=True)
    is_active = Column(Boolean, nullable=False, server_default="true")
    last_sync = Column(DateTime(timezone=True), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    creator = relationship("User", foreign_keys=[created_by])

class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    action = Column(String(100), nullable=False)
    entity_type = Column(String(50), nullable=True)
    entity_id = Column(Integer, nullable=True)
    details = Column(JSONB, nullable=True)
    ip_address = Column(String(50), nullable=True)
    user_agent = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)

    user = relationship("User", back_populates="activity_logs")

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    type = Column(String(50), nullable=False, server_default="info")
    is_read = Column(Boolean, nullable=False, server_default="false")
    link = Column(String(500), nullable=True)
    entity_type = Column(String(50), nullable=True)
    entity_id = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="notifications")

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    report_type = Column(String(100), nullable=False)
    filters = Column(JSONB, nullable=True)
    file_path = Column(String(500), nullable=True)
    file_format = Column(String(20), nullable=True)
    chart_data = Column(JSONB, nullable=True)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    creator = relationship("User", foreign_keys=[created_by])

class Forecast(Base):
    __tablename__ = "forecasts"

    id = Column(Integer, primary_key=True, index=True)
    forecast_type = Column(String(100), nullable=False)  # revenue, inventory, churn
    entity_id = Column(Integer, nullable=True)
    period_start = Column(Date, nullable=False)
    period_end = Column(Date, nullable=False)
    predicted_value = Column(Numeric(15, 2), nullable=False)
    confidence_low = Column(Numeric(15, 2), nullable=True)
    confidence_high = Column(Numeric(15, 2), nullable=True)
    confidence_score = Column(Float, nullable=True)
    trend = Column(String(50), nullable=True)  # increasing, decreasing, stable
    growth_rate = Column(Float, nullable=True)
    model_used = Column(String(100), nullable=True)
    insights = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Setting(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(255), unique=True, nullable=False)
    value = Column(Text, nullable=True)
    category = Column(String(100), nullable=False, server_default="general")
    is_encrypted = Column(Boolean, nullable=False, server_default="false")
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

# ============ RBAC PERMISSIONS MODELS ============

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    display_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    is_system = Column(Boolean, nullable=False, server_default="false")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    permissions = relationship("Permission", secondary="role_permissions", back_populates="roles")
    users = relationship("User", secondary="user_roles", back_populates="roles")
    field_permissions = relationship("FieldPermission", back_populates="role", cascade="all, delete-orphan")
    data_policies = relationship("DataPolicy", back_populates="role", cascade="all, delete-orphan")

class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    resource = Column(String(100), nullable=False)
    action = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    roles = relationship("Role", secondary="role_permissions", back_populates="permissions")

class RolePermission(Base):
    __tablename__ = "role_permissions"

    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("permissions.id", ondelete="CASCADE"), primary_key=True)

class UserRole(Base):
    __tablename__ = "user_roles"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)

class FieldPermission(Base):
    __tablename__ = "field_permissions"

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    resource = Column(String(100), nullable=False)
    field_name = Column(String(100), nullable=False)
    access_level = Column(String(20), nullable=False, server_default="read")  # read, write, hidden
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    role = relationship("Role", back_populates="field_permissions")

class DataPolicy(Base):
    __tablename__ = "data_policies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    resource = Column(String(100), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    condition = Column(JSONB, nullable=True)
    effect = Column(String(20), nullable=False, server_default="allow")  # allow, deny
    priority = Column(Integer, nullable=False, server_default="100")
    is_active = Column(Boolean, nullable=False, server_default="true")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    role = relationship("Role", back_populates="data_policies")

# ============ LLM INTEGRATION MODELS ============

class LLMModel(Base):
    __tablename__ = "llm_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    provider = Column(String(50), nullable=False, server_default="ollama")
    model_id = Column(String(100), unique=True, nullable=False)
    display_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    parameters = Column(JSONB, nullable=True)
    is_active = Column(Boolean, nullable=False, server_default="true")
    is_default = Column(Boolean, nullable=False, server_default="false")
    supports_streaming = Column(Boolean, nullable=False, server_default="true")
    supports_tools = Column(Boolean, nullable=False, server_default="false")
    context_window = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AIConversation(Base):
    __tablename__ = "ai_conversations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=True)
    model_id = Column(String(100), nullable=False)
    system_prompt = Column(Text, nullable=True)
    context = Column(JSONB, nullable=True)
    is_archived = Column(Boolean, nullable=False, server_default="false")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("User")
    messages = relationship("AIMessage", back_populates="conversation", cascade="all, delete-orphan", order_by="AIMessage.created_at")

class AIMessage(Base):
    __tablename__ = "ai_messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("ai_conversations.id", ondelete="CASCADE"), nullable=False)
    role = Column(String(50), nullable=False)  # system, user, assistant, tool
    content = Column(Text, nullable=False)
    model_id = Column(String(100), nullable=True)
    tokens_used = Column(Integer, nullable=True)
    latency_ms = Column(Integer, nullable=True)
    tool_calls = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    conversation = relationship("AIConversation", back_populates="messages")

class LLMUsage(Base):
    __tablename__ = "llm_usage"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    model_id = Column(String(100), nullable=False)
    conversation_id = Column(Integer, nullable=True)
    prompt_tokens = Column(Integer, nullable=False, server_default="0")
    completion_tokens = Column(Integer, nullable=False, server_default="0")
    total_tokens = Column(Integer, nullable=False, server_default="0")
    latency_ms = Column(Integer, nullable=True)
    endpoint = Column(String(100), nullable=True)
    success = Column(Boolean, nullable=False, server_default="true")
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)

class AIPromptTemplate(Base):
    __tablename__ = "ai_prompt_templates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    display_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    system_prompt = Column(Text, nullable=False)
    user_prompt_template = Column(Text, nullable=True)
    variables = Column(JSONB, nullable=True)
    model_id = Column(String(100), nullable=True)
    category = Column(String(50), nullable=False, server_default="general")
    is_active = Column(Boolean, nullable=False, server_default="true")
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    creator = relationship("User", foreign_keys=[created_by])

# ============ SEARCH MODELS ============

class SearchIndex(Base):
    __tablename__ = "search_indexes"

    id = Column(Integer, primary_key=True, index=True)
    entity_type = Column(String(100), nullable=False, index=True)
    entity_id = Column(Integer, nullable=False)
    title = Column(String(500), nullable=True)
    content = Column(Text, nullable=True)
    searchable_text = Column(Text, nullable=False)
    metadata = Column(JSONB, nullable=True)
    tags = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('entity_type', 'entity_id', name='uq_search_index_entity'),
    )

class SearchQuery(Base):
    __tablename__ = "search_queries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    query = Column(Text, nullable=False)
    filters = Column(JSONB, nullable=True)
    results_count = Column(Integer, nullable=False, server_default="0")
    execution_time_ms = Column(Integer, nullable=True)
    clicked_results = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)

class SearchSuggestion(Base):
    __tablename__ = "search_suggestions"

    id = Column(Integer, primary_key=True, index=True)
    query_text = Column(String(255), nullable=False)
    suggestion_type = Column(String(50), nullable=False, server_default="autocomplete")
    entity_type = Column(String(100), nullable=True)
    entity_id = Column(Integer, nullable=True)
    frequency = Column(Integer, nullable=False, server_default="1")
    last_used = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint('query_text', 'suggestion_type', 'entity_type', name='uq_search_suggestion'),
    )

## File: backend/app/__init__.py

## File: backend/app/auth.py

from datetime import datetime, timedelta
from typing import Optional, List
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Role, Permission
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    payload = decode_token(token)
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None or not user.is_active:
        raise HTTPException(status_code=401, detail="User not found or inactive")
    return user

async def require_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role not in ["admin", "superadmin"]:
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

async def require_superadmin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != "superadmin":
        raise HTTPException(status_code=403, detail="Superadmin access required")
    return current_user

async def get_current_user_optional(token: Optional[str] = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Optional[User]:
    if not token:
        return None
    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
        if user_id is None:
            return None
        return db.query(User).filter(User.id == int(user_id), User.is_active == True).first()
    except Exception:
        return None

def has_permission(user: User, resource: str, action: str, db: Session) -> bool:
    """Check if user has a specific permission through any of their roles."""
    if not user or not user.is_active:
        return False
    if any(r.name == "superadmin" for r in user.roles):
        return True
    for role in user.roles:
        for perm in role.permissions:
            if perm.resource == resource and perm.action == action:
                return True
    return False

def get_user_permissions(user: User, db: Session) -> List[str]:
    """Get all permission names for a user."""
    permissions = set()
    for role in user.roles:
        for perm in role.permissions:
            permissions.add(f"{perm.resource}.{perm.action}")
    return list(permissions)

def get_user_role_names(user: User) -> List[str]:
    """Get all role names for a user."""
    return [r.name for r in user.roles]

## File: backend/app/config.py

from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "AI-ERP System"
    APP_VERSION: str = "2.1.0"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "postgresql://erp_user:erp_password@localhost:5432/erp_db"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Security
    SECRET_KEY: str = "your-super-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # Email
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM: str = "noreply@ai-erp.local"

    # AI / Ollama
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen3.6"

    # Stripe
    STRIPE_SECRET_KEY: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""
    STRIPE_PUBLISHABLE_KEY: str = ""

    # File Upload
    UPLOAD_DIR: str = "./uploads"
    MAX_UPLOAD_SIZE: int = 50 * 1024 * 1024  # 50MB

    # WebSocket
    WS_HEARTBEAT_INTERVAL: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()

## File: backend/app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=20,
    max_overflow=30,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

## File: backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from app.database import engine, Base
from app.routers import (
    auth, crm, hr, inventory, finance, projects,
    ai, documents, reports, workflows, payments,
    integrations, analytics, admin, websocket,
    bulk_import_export, migrations, permissions, llm, search
)
from app.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title=settings.APP_NAME,
    description="Enterprise Resource Planning with AI-powered features",
    version="2.1.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(crm.router, prefix="/api/v1/crm", tags=["CRM"])
app.include_router(hr.router, prefix="/api/v1/hr", tags=["HR"])
app.include_router(inventory.router, prefix="/api/v1/inventory", tags=["Inventory"])
app.include_router(finance.router, prefix="/api/v1/finance", tags=["Finance"])
app.include_router(projects.router, prefix="/api/v1/projects", tags=["Projects"])
app.include_router(ai.router, prefix="/api/v1/ai", tags=["AI"])
app.include_router(documents.router, prefix="/api/v1/documents", tags=["Documents"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["Reports"])
app.include_router(workflows.router, prefix="/api/v1/workflows", tags=["Workflows"])
app.include_router(payments.router, prefix="/api/v1/payments", tags=["Payments"])
app.include_router(integrations.router, prefix="/api/v1/integrations", tags=["Integrations"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["Admin"])
app.include_router(websocket.router, prefix="/api/v1/ws", tags=["WebSocket"])
app.include_router(bulk_import_export.router, prefix="/api/v1/bulk", tags=["Bulk Import/Export"])
app.include_router(migrations.router, prefix="/api/v1/migrations", tags=["Migrations"])
app.include_router(permissions.router, prefix="/api/v1/permissions", tags=["Permissions & RBAC"])
app.include_router(llm.router, prefix="/api/v1/llm", tags=["LLM Integration"])
app.include_router(search.router, prefix="/api/v1/search", tags=["Advanced Search"])

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "features": [
            "Core ERP (CRM, HR, Inventory, Finance, Projects)",
            "AI Chat & RAG",
            "Document Management",
            "Reports & Analytics",
            "Workflow Automation",
            "Stripe Payments",
            "WebSocket Real-time",
            "PWA with Offline Support",
            "AI Forecasting",
            "Bulk Import/Export",
            "Alembic Migrations",
            "Advanced Permissions & RBAC",
            "Multi-Model LLM Integration",
            "AI Agent with Tools",
            "LLM Streaming & Analytics",
            "Advanced Search (Full-text, Facets, Suggestions)"
        ]
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

## File: backend/app/routers/inventory.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

from app.database import get_db
from app.models import Product, InventoryMovement
from app.auth import get_current_user
from app.services.activity_log import log_activity

router = APIRouter()

class ProductCreate(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    unit_price: float = 0
    cost_price: Optional[float] = None
    quantity_in_stock: int = 0
    reorder_level: int = 10
    reorder_quantity: int = 50
    supplier: Optional[str] = None
    supplier_contact: Optional[str] = None
    status: str = "active"
    barcode: Optional[str] = None
    weight: Optional[float] = None
    dimensions: Optional[str] = None

class MovementCreate(BaseModel):
    product_id: int
    movement_type: str
    quantity: int
    unit_cost: Optional[float] = None
    reference: Optional[str] = None
    notes: Optional[str] = None

@router.post("/products")
def create_product(data: ProductCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    existing = db.query(Product).filter(Product.sku == data.sku).first()
    if existing:
        raise HTTPException(status_code=400, detail="SKU already exists")

    product = Product(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    log_activity(db, user_id=current_user.id, action="product_created", entity_type="product", entity_id=product.id)
    return product

@router.get("/products")
def list_products(
    category: Optional[str] = None,
    status: Optional[str] = None,
    low_stock: bool = False,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category)
    if status:
        query = query.filter(Product.status == status)
    if low_stock:
        query = query.filter(Product.quantity_in_stock <= Product.reorder_level)
    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))
    return query.all()

@router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}")
def update_product(product_id: int, data: ProductCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in data.dict().items():
        setattr(product, key, value)
    product.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(product)
    return product

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted"}

@router.post("/movements")
def create_movement(data: MovementCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == data.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    movement = InventoryMovement(**data.dict(), created_by=current_user.id)

    # Update stock
    if data.movement_type == "in":
        product.quantity_in_stock += data.quantity
    elif data.movement_type == "out":
        if product.quantity_in_stock < data.quantity:
            raise HTTPException(status_code=400, detail="Insufficient stock")
        product.quantity_in_stock -= data.quantity
    elif data.movement_type == "adjustment":
        product.quantity_in_stock = data.quantity

    product.updated_at = datetime.utcnow()
    db.add(movement)
    db.commit()
    db.refresh(movement)
    log_activity(db, user_id=current_user.id, action="inventory_moved", entity_type="inventory_movement", entity_id=movement.id)
    return movement

@router.get("/movements")
def list_movements(product_id: Optional[int] = None, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    query = db.query(InventoryMovement)
    if product_id:
        query = query.filter(InventoryMovement.product_id == product_id)
    return query.order_by(InventoryMovement.created_at.desc()).all()

@router.get("/dashboard")
def inventory_dashboard(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    from sqlalchemy import func
    total_products = db.query(Product).count()
    total_stock_value = db.query(func.sum(Product.quantity_in_stock * Product.unit_price)).scalar() or 0
    low_stock_count = db.query(Product).filter(Product.quantity_in_stock <= Product.reorder_level).count()
    out_of_stock = db.query(Product).filter(Product.quantity_in_stock == 0).count()

    return {
        "total_products": total_products,
        "total_stock_value": float(total_stock_value),
        "low_stock_count": low_stock_count,
        "out_of_stock": out_of_stock,
        "categories": db.query(Product.category, func.count(Product.id)).group_by(Product.category).all()
    }

## File: backend/app/routers/crm.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime, date
from decimal import Decimal

from app.database import get_db
from app.models import Contact, Company, Deal
from app.auth import get_current_user, require_admin, has_permission
from app.services.activity_log import log_activity

router = APIRouter()

# Schemas
class CompanyCreate(BaseModel):
    name: str
    industry: Optional[str] = None
    size: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None

class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    title: Optional[str] = None
    company_id: Optional[int] = None
    status: str = "lead"
    source: Optional[str] = None
    notes: Optional[str] = None

class DealCreate(BaseModel):
    title: str
    contact_id: Optional[int] = None
    company_id: Optional[int] = None
    value: float = 0
    stage: str = "prospect"
    probability: int = 0
    expected_close_date: Optional[date] = None
    description: Optional[str] = None

class DealUpdate(BaseModel):
    title: Optional[str] = None
    value: Optional[float] = None
    stage: Optional[str] = None
    probability: Optional[int] = None
    expected_close_date: Optional[date] = None
    actual_close_date: Optional[date] = None

# Companies
@router.post("/companies")
def create_company(data: CompanyCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    company = Company(**data.dict())
    db.add(company)
    db.commit()
    db.refresh(company)
    log_activity(db, user_id=current_user.id, action="company_created", entity_type="company", entity_id=company.id)
    return company

@router.get("/companies")
def list_companies(
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = db.query(Company)
    if search:
        query = query.filter(Company.name.ilike(f"%{search}%"))
    return query.offset(skip).limit(limit).all()

@router.get("/companies/{company_id}")
def get_company(company_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@router.put("/companies/{company_id}")
def update_company(company_id: int, data: CompanyCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    for key, value in data.dict().items():
        setattr(company, key, value)
    db.commit()
    db.refresh(company)
    return company

@router.delete("/companies/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    db.delete(company)
    db.commit()
    return {"message": "Company deleted"}

# Contacts
@router.post("/contacts")
def create_contact(data: ContactCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    if not has_permission(current_user, "contacts", "create", db):
        raise HTTPException(status_code=403, detail="Permission denied: contacts.create")
    contact = Contact(**data.dict(), assigned_to=current_user.id)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    log_activity(db, user_id=current_user.id, action="contact_created", entity_type="contact", entity_id=contact.id)
    return contact

@router.get("/contacts")
def list_contacts(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if not has_permission(current_user, "contacts", "read", db):
        raise HTTPException(status_code=403, detail="Permission denied: contacts.read")
    query = db.query(Contact)
    if status:
        query = query.filter(Contact.status == status)
    if search:
        query = query.filter(
            (Contact.first_name + " " + Contact.last_name).ilike(f"%{search}%") |
            Contact.email.ilike(f"%{search}%")
        )
    return query.offset(skip).limit(limit).all()

@router.get("/contacts/{contact_id}")
def get_contact(contact_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.put("/contacts/{contact_id}")
def update_contact(contact_id: int, data: ContactCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    for key, value in data.dict().items():
        setattr(contact, key, value)
    contact.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(contact)
    return contact

@router.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(contact)
    db.commit()
    return {"message": "Contact deleted"}

# Deals / Pipeline
@router.post("/deals")
def create_deal(data: DealCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    deal = Deal(**data.dict(), assigned_to=current_user.id)
    db.add(deal)
    db.commit()
    db.refresh(deal)
    log_activity(db, user_id=current_user.id, action="deal_created", entity_type="deal", entity_id=deal.id)
    return deal

@router.get("/deals")
def list_deals(
    skip: int = 0,
    limit: int = 100,
    stage: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = db.query(Deal)
    if stage:
        query = query.filter(Deal.stage == stage)
    return query.offset(skip).limit(limit).all()

@router.get("/deals/pipeline")
def get_pipeline(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    stages = ["prospect", "qualification", "proposal", "negotiation", "closed_won", "closed_lost"]
    pipeline = {}
    for stage in stages:
        deals = db.query(Deal).filter(Deal.stage == stage).all()
        total = sum(d.value or 0 for d in deals)
        pipeline[stage] = {
            "count": len(deals),
            "total_value": float(total),
            "deals": deals
        }
    return pipeline

@router.get("/deals/{deal_id}")
def get_deal(deal_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    deal = db.query(Deal).filter(Deal.id == deal_id).first()
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    return deal

@router.put("/deals/{deal_id}")
def update_deal(deal_id: int, data: DealUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    deal = db.query(Deal).filter(Deal.id == deal_id).first()
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")

    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(deal, key, value)

    # Auto-update probability based on stage
    stage_probabilities = {
        "prospect": 10,
        "qualification": 25,
        "proposal": 50,
        "negotiation": 75,
        "closed_won": 100,
        "closed_lost": 0
    }
    if deal.stage in stage_probabilities and "stage" in update_data:
        deal.probability = stage_probabilities[deal.stage]

    if deal.stage == "closed_won" and not deal.actual_close_date:
        deal.actual_close_date = date.today()

    deal.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(deal)
    log_activity(db, user_id=current_user.id, action="deal_updated", entity_type="deal", entity_id=deal.id, details={"stage": deal.stage})
    return deal

@router.delete("/deals/{deal_id}")
def delete_deal(deal_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    deal = db.query(Deal).filter(Deal.id == deal_id).first()
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    db.delete(deal)
    db.commit()
    return {"message": "Deal deleted"}

# Dashboard stats
@router.get("/dashboard")
def crm_dashboard(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    total_contacts = db.query(Contact).count()
    total_companies = db.query(Company).count()
    total_deals = db.query(Deal).count()
    total_pipeline_value = db.query(func.sum(Deal.value)).filter(Deal.stage != "closed_lost").scalar() or 0
    won_deals = db.query(Deal).filter(Deal.stage == "closed_won").count()

    return {
        "total_contacts": total_contacts,
        "total_companies": total_companies,
        "total_deals": total_deals,
        "pipeline_value": float(total_pipeline_value),
        "won_deals": won_deals,
        "conversion_rate": (won_deals / total_deals * 100) if total_deals > 0 else 0
    }

## File: backend/app/routers/finance.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime
from decimal import Decimal

from app.database import get_db
from app.models import Invoice, InvoiceItem, Payment
from app.auth import get_current_user
from app.services.activity_log import log_activity

router = APIRouter()

class InvoiceItemCreate(BaseModel):
    product_id: Optional[int] = None
    description: str
    quantity: float = 1
    unit_price: float

class InvoiceCreate(BaseModel):
    invoice_number: str
    contact_id: Optional[int] = None
    company_id: Optional[int] = None
    issue_date: date
    due_date: date
    tax_rate: float = 0
    notes: Optional[str] = None
    terms: Optional[str] = None
    items: List[InvoiceItemCreate]

class PaymentCreate(BaseModel):
    invoice_id: int
    amount: float
    payment_method: str
    payment_date: date
    notes: Optional[str] = None

def generate_invoice_number(db: Session) -> str:
    count = db.query(Invoice).count() + 1
    return f"INV-{datetime.now().year}-{count:05d}"

@router.post("/invoices")
def create_invoice(data: InvoiceCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    existing = db.query(Invoice).filter(Invoice.invoice_number == data.invoice_number).first()
    if existing:
        raise HTTPException(status_code=400, detail="Invoice number already exists")

    subtotal = sum(item.quantity * item.unit_price for item in data.items)
    tax_amount = subtotal * (data.tax_rate / 100)
    total = subtotal + tax_amount

    invoice = Invoice(
        invoice_number=data.invoice_number,
        contact_id=data.contact_id,
        company_id=data.company_id,
        issue_date=data.issue_date,
        due_date=data.due_date,
        subtotal=subtotal,
        tax_rate=data.tax_rate,
        tax_amount=tax_amount,
        total=total,
        notes=data.notes,
        terms=data.terms,
        created_by=current_user.id
    )
    db.add(invoice)
    db.flush()

    for item_data in data.items:
        item_total = item_data.quantity * item_data.unit_price
        item = InvoiceItem(
            invoice_id=invoice.id,
            product_id=item_data.product_id,
            description=item_data.description,
            quantity=item_data.quantity,
            unit_price=item_data.unit_price,
            total=item_total
        )
        db.add(item)

    db.commit()
    db.refresh(invoice)
    log_activity(db, user_id=current_user.id, action="invoice_created", entity_type="invoice", entity_id=invoice.id)
    return invoice

@router.get("/invoices")
def list_invoices(
    status: Optional[str] = None,
    contact_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = db.query(Invoice)
    if status:
        query = query.filter(Invoice.status == status)
    if contact_id:
        query = query.filter(Invoice.contact_id == contact_id)
    return query.order_by(Invoice.created_at.desc()).all()

@router.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@router.put("/invoices/{invoice_id}/status")
def update_invoice_status(
    invoice_id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    invoice.status = status
    db.commit()
    db.refresh(invoice)
    return invoice

@router.post("/payments")
def create_payment(data: PaymentCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    invoice = db.query(Invoice).filter(Invoice.id == data.invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    payment = Payment(**data.dict())
    db.add(payment)

    invoice.amount_paid = (invoice.amount_paid or 0) + data.amount
    if invoice.amount_paid >= invoice.total:
        invoice.status = "paid"
    else:
        invoice.status = "partial"

    db.commit()
    db.refresh(payment)
    log_activity(db, user_id=current_user.id, action="payment_received", entity_type="payment", entity_id=payment.id)
    return payment

@router.get("/dashboard")
def finance_dashboard(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    total_invoices = db.query(Invoice).count()
    total_revenue = db.query(func.sum(Invoice.amount_paid)).scalar() or 0
    outstanding = db.query(func.sum(Invoice.total - Invoice.amount_paid)).filter(Invoice.status != "paid").scalar() or 0
    overdue = db.query(Invoice).filter(Invoice.due_date < date.today(), Invoice.status != "paid").count()

    return {
        "total_invoices": total_invoices,
        "total_revenue": float(total_revenue),
        "outstanding": float(outstanding),
        "overdue_count": overdue,
        "monthly_revenue": db.query(
            func.extract('month', Invoice.issue_date),
            func.sum(Invoice.total)
        ).group_by(func.extract('month', Invoice.issue_date)).all()
    }

## File: backend/app/routers/payments.py

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
import stripe

from app.database import get_db
from app.models import Invoice, Payment
from app.auth import get_current_user
from app.config import settings
from app.services.activity_log import log_activity

router = APIRouter()

if settings.STRIPE_SECRET_KEY:
    stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentIntentRequest(BaseModel):
    invoice_id: int
    amount: Optional[float] = None

@router.post("/create-intent")
def create_payment_intent(
    data: PaymentIntentRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if not settings.STRIPE_SECRET_KEY:
        raise HTTPException(status_code=400, detail="Stripe not configured")

    invoice = db.query(Invoice).filter(Invoice.id == data.invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    amount = data.amount or float(invoice.total - (invoice.amount_paid or 0))
    amount_cents = int(amount * 100)

    try:
        intent = stripe.PaymentIntent.create(
            amount=amount_cents,
            currency="usd",
            metadata={"invoice_id": invoice.id, "invoice_number": invoice.invoice_number}
        )

        invoice.stripe_payment_intent_id = intent.id
        db.commit()

        return {
            "client_secret": intent.client_secret,
            "payment_intent_id": intent.id,
            "amount": amount,
            "publishable_key": settings.STRIPE_PUBLISHABLE_KEY
        }
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/webhook")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    if not settings.STRIPE_WEBHOOK_SECRET:
        raise HTTPException(status_code=400, detail="Webhook secret not configured")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)
    except (ValueError, stripe.error.SignatureVerificationError):
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "payment_intent.succeeded":
        intent = event["data"]["object"]
        invoice_id = intent["metadata"].get("invoice_id")

        if invoice_id:
            invoice = db.query(Invoice).filter(Invoice.id == int(invoice_id)).first()
            if invoice:
                amount = intent["amount_received"] / 100
                payment = Payment(
                    invoice_id=invoice.id,
                    amount=amount,
                    payment_method="stripe",
                    payment_date=datetime.now().date(),
                    stripe_payment_intent_id=intent["id"],
                    stripe_charge_id=intent["charges"]["data"][0]["id"] if intent.get("charges") else None,
                    status="completed"
                )
                db.add(payment)
                invoice.amount_paid = (invoice.amount_paid or 0) + amount
                if invoice.amount_paid >= invoice.total:
                    invoice.status = "paid"
                db.commit()

    return {"status": "success"}

from datetime import datetime

## File: backend/app/routers/analytics.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from datetime import datetime, timedelta

from app.database import get_db
from app.models import Invoice, Deal, Contact, Product, Employee, Project, Task, ActivityLog
from app.auth import get_current_user

router = APIRouter()

@router.get("/dashboard")
def get_dashboard_analytics(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Revenue
    total_revenue = db.query(func.sum(Invoice.total)).filter(Invoice.status == "paid").scalar() or 0
    outstanding = db.query(func.sum(Invoice.total - Invoice.amount_paid)).filter(Invoice.status != "paid").scalar() or 0

    # CRM
    total_contacts = db.query(Contact).count()
    total_deals = db.query(Deal).count()
    pipeline_value = db.query(func.sum(Deal.value)).filter(Deal.stage != "closed_lost").scalar() or 0

    # HR
    total_employees = db.query(Employee).count()
    active_employees = db.query(Employee).filter(Employee.status == "active").count()

    # Inventory
    total_products = db.query(Product).count()
    low_stock = db.query(Product).filter(Product.quantity_in_stock <= Product.reorder_level).count()

    # Projects
    total_projects = db.query(Project).count()
    active_projects = db.query(Project).filter(Project.status == "active").count()
    total_tasks = db.query(Task).count()
    completed_tasks = db.query(Task).filter(Task.status == "done").count()

    # Activity
    recent_activity = db.query(ActivityLog).order_by(ActivityLog.created_at.desc()).limit(10).all()

    return {
        "revenue": {
            "total": float(total_revenue),
            "outstanding": float(outstanding),
            "collection_rate": (float(total_revenue) / (float(total_revenue) + float(outstanding)) * 100) if (total_revenue + outstanding) > 0 else 0
        },
        "crm": {
            "contacts": total_contacts,
            "deals": total_deals,
            "pipeline_value": float(pipeline_value)
        },
        "hr": {
            "total_employees": total_employees,
            "active_employees": active_employees
        },
        "inventory": {
            "total_products": total_products,
            "low_stock": low_stock
        },
        "projects": {
            "total_projects": total_projects,
            "active_projects": active_projects,
            "tasks": {"total": total_tasks, "completed": completed_tasks}
        },
        "recent_activity": [
            {"action": a.action, "entity_type": a.entity_type, "created_at": a.created_at.isoformat() if a.created_at else None}
            for a in recent_activity
        ]
    }

@router.get("/monthly-trends")
def get_monthly_trends(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    months_back = 6
    start_date = datetime.now() - timedelta(days=30 * months_back)

    revenue_by_month = db.query(
        extract('year', Invoice.issue_date).label('year'),
        extract('month', Invoice.issue_date).label('month'),
        func.sum(Invoice.total).label('total')
    ).filter(Invoice.issue_date >= start_date).group_by('year', 'month').order_by('year', 'month').all()

    deals_by_month = db.query(
        extract('year', Deal.created_at).label('year'),
        extract('month', Deal.created_at).label('month'),
        func.count(Deal.id).label('count'),
        func.sum(Deal.value).label('value')
    ).filter(Deal.created_at >= start_date).group_by('year', 'month').order_by('year', 'month').all()

    return {
        "revenue": [
            {"period": f"{r.year}-{r.month:02d}", "amount": float(r.total)}
            for r in revenue_by_month
        ],
        "deals": [
            {"period": f"{d.year}-{d.month:02d}", "count": d.count, "value": float(d.value or 0)}
            for d in deals_by_month
        ]
    }

## File: backend/app/routers/search.py

from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models import User
from app.auth import get_current_user, require_admin
from app.services.search_service import SearchService
from app.services.activity_log import log_activity

router = APIRouter(prefix="/api/v1/search", tags=["Advanced Search"])

# Schemas
class SearchRequest(BaseModel):
    query: str
    entity_types: Optional[List[str]] = None
    filters: Optional[Dict[str, Any]] = None
    limit: int = 20
    offset: int = 0

class SearchResult(BaseModel):
    id: int
    entity_type: str
    entity_id: int
    title: str
    content_preview: str
    metadata: Dict[str, Any]
    tags: List[str]
    updated_at: Optional[str]

class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]
    total: int
    execution_time_ms: int
    facets: Dict[str, Any]
    page: int
    per_page: int

class SuggestionResponse(BaseModel):
    text: str
    type: str
    entity_type: Optional[str]
    frequency: int

class SearchAnalytics(BaseModel):
    period_days: int
    total_queries: int
    no_results_queries: int
    no_results_rate: float
    avg_execution_time_ms: float
    top_queries: List[Dict[str, Any]]
    daily_volume: List[Dict[str, Any]]
    popular_filters: List[Dict[str, Any]]

# ==================== SEARCH ====================

@router.post("/", response_model=SearchResponse)
def search(
    request: SearchRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Advanced full-text search across all indexed entities.
    Supports entity type filtering, metadata filters, and faceted results.
    """
    service = SearchService(db)

    results, total, execution_time = service.search(
        query=request.query,
        entity_types=request.entity_types,
        filters=request.filters,
        limit=request.limit,
        offset=request.offset
    )

    facets = service.get_facets(
        query=request.query,
        entity_types=request.entity_types
    )

    # Log query for analytics
    service.log_query(
        user_id=current_user.id,
        query=request.query,
        filters=request.filters,
        results_count=total,
        execution_time_ms=execution_time
    )

    # Record suggestion
    if request.query and len(request.query) >= 3:
        service.record_suggestion(request.query)

    log_activity(db, user_id=current_user.id, action="search", entity_type="search", details={"query": request.query, "results": total})

    return {
        "query": request.query,
        "results": results,
        "total": total,
        "execution_time_ms": execution_time,
        "facets": facets,
        "page": (request.offset // request.limit) + 1,
        "per_page": request.limit
    }

@router.get("/")
def search_get(
    q: str = Query(..., description="Search query"),
    types: Optional[str] = Query(None, description="Comma-separated entity types"),
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """GET endpoint for search (useful for browser/search engine integration)."""
    service = SearchService(db)

    entity_types = types.split(",") if types else None

    results, total, execution_time = service.search(
        query=q,
        entity_types=entity_types,
        limit=limit,
        offset=offset
    )

    facets = service.get_facets(query=q, entity_types=entity_types)

    service.log_query(
        user_id=current_user.id,
        query=q,
        results_count=total,
        execution_time_ms=execution_time
    )

    return {
        "query": q,
        "results": results,
        "total": total,
        "execution_time_ms": execution_time,
        "facets": facets,
        "page": (offset // limit) + 1,
        "per_page": limit
    }

# ==================== SUGGESTIONS ====================

@router.get("/suggestions", response_model=List[SuggestionResponse])
def get_suggestions(
    q: str = Query(..., min_length=2, description="Query prefix for suggestions"),
    limit: int = Query(default=10, ge=1, le=20),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get autocomplete suggestions for search queries."""
    service = SearchService(db)
    suggestions = service.get_suggestions(q, limit=limit)
    return suggestions

# ==================== FACETS ====================

@router.get("/facets")
def get_facets(
    q: Optional[str] = Query(None, description="Optional query to filter facets"),
    types: Optional[str] = Query(None, description="Comma-separated entity types"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get facet counts for search results."""
    service = SearchService(db)
    entity_types = types.split(",") if types else None
    return service.get_facets(query=q, entity_types=entity_types)

# ==================== INDEXING ====================

@router.post("/reindex")
def reindex_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Reindex all entities for search. Admin only."""
    service = SearchService(db)
    counts = service.reindex_all()

    log_activity(db, user_id=current_user.id, action="search_reindex", entity_type="search", details=counts)

    return {
        "status": "success",
        "message": "All entities reindexed",
        "counts": counts
    }

@router.post("/index/{entity_type}/{entity_id}")
def index_entity(
    entity_type: str,
    entity_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Index a specific entity. Admin only."""
    service = SearchService(db)

    # Fetch entity based on type
    if entity_type == "contact":
        from app.models import Contact
        entity = db.query(Contact).filter(Contact.id == entity_id).first()
        if entity:
            service.index_entity("contact", entity.id, f"{entity.first_name} {entity.last_name}",
                f"{entity.email or ''} {entity.phone or ''} {entity.title or ''} {entity.notes or ''}",
                metadata={"email": entity.email, "status": entity.status})
    elif entity_type == "company":
        from app.models import Company
        entity = db.query(Company).filter(Company.id == entity_id).first()
        if entity:
            service.index_entity("company", entity.id, entity.name,
                f"{entity.industry or ''} {entity.website or ''} {entity.address or ''}",
                metadata={"industry": entity.industry, "size": entity.size})
    elif entity_type == "product":
        from app.models import Product
        entity = db.query(Product).filter(Product.id == entity_id).first()
        if entity:
            service.index_entity("product", entity.id, entity.name,
                f"{entity.sku} {entity.description or ''} {entity.category or ''}",
                metadata={"sku": entity.sku, "category": entity.category, "price": float(entity.unit_price) if entity.unit_price else 0})
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported entity type: {entity_type}")

    return {"message": f"{entity_type} {entity_id} indexed"}

# ==================== ANALYTICS ====================

@router.get("/analytics")
def get_search_analytics(
    days: int = Query(default=30, ge=1, le=365),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Get search analytics. Admin only."""
    service = SearchService(db)
    return service.get_search_analytics(days=days)

@router.get("/analytics/popular-queries")
def get_popular_queries(
    limit: int = Query(default=20, ge=1, le=100),
    days: int = Query(default=30, ge=1, le=365),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Get most popular search queries. Admin only."""
    from datetime import datetime, timedelta
    from sqlalchemy import func

    start_date = datetime.utcnow() - timedelta(days=days)

    queries = db.query(
        SearchQuery.query,
        func.count(SearchQuery.id).label("count"),
        func.avg(SearchQuery.results_count).label("avg_results")
    ).filter(
        SearchQuery.created_at >= start_date
    ).group_by(SearchQuery.query).order_by(func.count(SearchQuery.id).desc()).limit(limit).all()

    return {
        "queries": [
            {"query": q.query, "count": q.count, "avg_results": round(float(q.avg_results or 0), 1)}
            for q in queries
        ]
    }

from app.models import SearchQuery

## File: backend/app/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from datetime import datetime

from app.database import get_db
from app.models import User
from app.auth import (
    verify_password, get_password_hash, create_access_token,
    get_current_user, require_admin
)
from app.services.activity_log import log_activity

router = APIRouter()

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: str = "user"

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user_data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=user_data.email,
        hashed_password=get_password_hash(user_data.password),
        full_name=user_data.full_name,
        role=user_data.role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    log_activity(db, user_id=user.id, action="user_registered", entity_type="user", entity_id=user.id)
    return user

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user.last_login = datetime.utcnow()
    db.commit()

    token = create_access_token({"sub": str(user.id), "role": user.role})
    log_activity(db, user_id=user.id, action="user_login", entity_type="user", entity_id=user.id)

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user
    }

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/users", response_model=list[UserResponse])
def list_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return db.query(User).offset(skip).limit(limit).all()

@router.put("/users/{user_id}")
def update_user(
    user_id: int,
    user_data: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user_data.items():
        if hasattr(user, key) and key != "id":
            setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

## File: backend/app/routers/documents.py

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import Optional, List
import os
import shutil
import uuid

from app.database import get_db
from app.models import Document
from app.auth import get_current_user
from app.config import settings
from app.services.activity_log import log_activity

router = APIRouter()

UPLOAD_DIR = settings.UPLOAD_DIR
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    entity_type: Optional[str] = None,
    entity_id: Optional[int] = None,
    title: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    file_ext = os.path.splitext(file.filename)[1]
    unique_name = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    doc = Document(
        title=title or file.filename,
        filename=file.filename,
        file_path=file_path,
        file_size=os.path.getsize(file_path),
        mime_type=file.content_type,
        entity_type=entity_type,
        entity_id=entity_id,
        uploaded_by=current_user.id
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    log_activity(db, user_id=current_user.id, action="document_uploaded", entity_type="document", entity_id=doc.id)
    return doc

@router.get("/documents")
def list_documents(
    entity_type: Optional[str] = None,
    entity_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = db.query(Document)
    if entity_type:
        query = query.filter(Document.entity_type == entity_type)
    if entity_id:
        query = query.filter(Document.entity_id == entity_id)
    return query.order_by(Document.created_at.desc()).all()

@router.get("/documents/{doc_id}")
def get_document(doc_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.delete("/documents/{doc_id}")
def delete_document(doc_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    if os.path.exists(doc.file_path):
        os.remove(doc.file_path)

    db.delete(doc)
    db.commit()
    return {"message": "Document deleted"}

## File: backend/app/routers/workflows.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

from app.database import get_db
from app.models import Workflow, WorkflowStep, WorkflowExecution
from app.auth import get_current_user, require_admin
from app.services.activity_log import log_activity

router = APIRouter()

class StepConfig(BaseModel):
    step_type: str
    approvers: Optional[List[int]] = None
    condition: Optional[str] = None
    action: Optional[str] = None
    notification_template: Optional[str] = None
    delay_minutes: Optional[int] = None

class WorkflowCreate(BaseModel):
    name: str
    description: Optional[str] = None
    entity_type: str
    trigger_type: str
    trigger_condition: Optional[Dict[str, Any]] = None
    steps: List[StepConfig]

@router.post("/workflows")
def create_workflow(data: WorkflowCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    workflow = Workflow(
        name=data.name,
        description=data.description,
        entity_type=data.entity_type,
        trigger_type=data.trigger_type,
        trigger_condition=data.trigger_condition,
        created_by=current_user.id
    )
    db.add(workflow)
    db.flush()

    for idx, step_data in enumerate(data.steps):
        step = WorkflowStep(
            workflow_id=workflow.id,
            name=f"Step {idx + 1}",
            step_type=step_data.step_type,
            step_order=idx,
            config=step_data.dict()
        )
        db.add(step)

    db.commit()
    db.refresh(workflow)
    log_activity(db, user_id=current_user.id, action="workflow_created", entity_type="workflow", entity_id=workflow.id)
    return workflow

@router.get("/workflows")
def list_workflows(
    entity_type: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = db.query(Workflow)
    if entity_type:
        query = query.filter(Workflow.entity_type == entity_type)
    return query.all()

@router.get("/workflows/{workflow_id}")
def get_workflow(workflow_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return workflow

@router.put("/workflows/{workflow_id}/toggle")
def toggle_workflow(workflow_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    workflow.is_active = not workflow.is_active
    db.commit()
    return workflow

@router.delete("/workflows/{workflow_id}")
def delete_workflow(workflow_id: int, db: Session = Depends(get_db), current_user = Depends(require_admin)):
    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    db.delete(workflow)
    db.commit()
    return {"message": "Workflow deleted"}

@router.get("/executions")
def list_executions(
    workflow_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = db.query(WorkflowExecution)
    if workflow_id:
        query = query.filter(WorkflowExecution.workflow_id == workflow_id)
    return query.order_by(WorkflowExecution.started_at.desc()).all()

@router.post("/workflows/{workflow_id}/execute")
def execute_workflow(
    workflow_id: int,
    entity_type: str,
    entity_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
    if not workflow or not workflow.is_active:
        raise HTTPException(status_code=404, detail="Workflow not found or inactive")

    execution = WorkflowExecution(
        workflow_id=workflow_id,
        entity_type=entity_type,
        entity_id=entity_id,
        status="running",
        current_step=0,
        context={"triggered_by": current_user.id}
    )
    db.add(execution)
    db.commit()
    db.refresh(execution)

    log_activity(db, user_id=current_user.id, action="workflow_executed", entity_type="workflow_execution", entity_id=execution.id)
    return execution

## File: backend/app/routers/__init__.py

## File: backend/app/routers/reports.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, date
import io
import base64

from app.database import get_db
from app.models import Invoice, Deal, Contact, Product, Employee, Project, Task
from app.auth import get_current_user
from app.services.activity_log import log_activity

router = APIRouter()

@router.get("/revenue")
def revenue_report(
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    from sqlalchemy import func, extract

    query = db.query(Invoice)
    if start_date:
        query = query.filter(Invoice.issue_date >= start_date)
    if end_date:
        query = query.filter(Invoice.issue_date <= end_date)

    invoices = query.all()
    total = sum(i.total or 0 for i in invoices)
    paid = sum(i.amount_paid or 0 for i in invoices)

    monthly = db.query(
        extract('month', Invoice.issue_date).label('month'),
        extract('year', Invoice.issue_date).label('year'),
        func.sum(Invoice.total).label('total'),
        func.count(Invoice.id).label('count')
    ).group_by('year', 'month').order_by('year', 'month').all()

    return {
        "total_revenue": float(total),
        "total_paid": float(paid),
        "outstanding": float(total - paid),
        "invoice_count": len(invoices),
        "monthly_breakdown": [
            {"month": f"{m.year}-{m.month}", "revenue": float(m.total), "count": m.count}
            for m in monthly
        ]
    }

@router.get("/pipeline")
def pipeline_report(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    stages = ["prospect", "qualification", "proposal", "negotiation", "closed_won", "closed_lost"]
    result = {}
    for stage in stages:
        deals = db.query(Deal).filter(Deal.stage == stage).all()
        result[stage] = {
            "count": len(deals),
            "value": float(sum(d.value or 0 for d in deals))
        }
    return result

@router.get("/inventory")
def inventory_report(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    products = db.query(Product).all()
    total_value = sum(p.quantity_in_stock * p.unit_price for p in products)
    low_stock = [p for p in products if p.quantity_in_stock <= p.reorder_level]

    return {
        "total_products": len(products),
        "total_stock_value": float(total_value),
        "low_stock_count": len(low_stock),
        "low_stock_items": [
            {"id": p.id, "name": p.name, "sku": p.sku, "stock": p.quantity_in_stock}
            for p in low_stock
        ],
        "categories": {}
    }

@router.get("/chart/revenue")
def revenue_chart(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from sqlalchemy import func, extract

        monthly = db.query(
            extract('month', Invoice.issue_date).label('month'),
            extract('year', Invoice.issue_date).label('year'),
            func.sum(Invoice.total).label('total')
        ).group_by('year', 'month').order_by('year', 'month').all()

        if not monthly:
            return {"chart": None}

        labels = [f"{m.year}-{m.month:02d}" for m in monthly]
        values = [float(m.total) for m in monthly]

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(labels, values, color='#4f46e5')
        ax.set_xlabel('Month')
        ax.set_ylabel('Revenue ($)')
        ax.set_title('Monthly Revenue')
        plt.xticks(rotation=45)
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode()
        plt.close()

        return {"chart": f"data:image/png;base64,{img_base64}"}
    except Exception as e:
        return {"chart": None, "error": str(e)}

## File: backend/app/routers/hr.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from decimal import Decimal

from app.database import get_db
from app.models import Employee, Department
from app.auth import get_current_user, require_admin
from app.services.activity_log import log_activity

router = APIRouter()

class DepartmentCreate(BaseModel):
    name: str
    description: Optional[str] = None
    manager_id: Optional[int] = None
    budget: Optional[float] = None

class EmployeeCreate(BaseModel):
    employee_code: str
    job_title: str
    department_id: Optional[int] = None
    salary: Optional[float] = None
    hire_date: date
    status: str = "active"
    employment_type: str = "full_time"
    address: Optional[str] = None
    emergency_contact: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None

@router.post("/departments")
def create_department(data: DepartmentCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    dept = Department(**data.dict())
    db.add(dept)
    db.commit()
    db.refresh(dept)
    log_activity(db, user_id=current_user.id, action="department_created", entity_type="department", entity_id=dept.id)
    return dept

@router.get("/departments")
def list_departments(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.query(Department).all()

@router.post("/employees")
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    existing = db.query(Employee).filter(Employee.employee_code == data.employee_code).first()
    if existing:
        raise HTTPException(status_code=400, detail="Employee code already exists")

    emp = Employee(**data.dict())
    db.add(emp)
    db.commit()
    db.refresh(emp)
    log_activity(db, user_id=current_user.id, action="employee_created", entity_type="employee", entity_id=emp.id)
    return emp

@router.get("/employees")
def list_employees(
    status: Optional[str] = None,
    department_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = db.query(Employee)
    if status:
        query = query.filter(Employee.status == status)
    if department_id:
        query = query.filter(Employee.department_id == department_id)
    return query.all()

@router.get("/employees/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/employees/{employee_id}")
def update_employee(employee_id: int, data: EmployeeCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in data.dict().items():
        setattr(emp, key, value)
    emp.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(emp)
    return emp

@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db), current_user = Depends(require_admin)):
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}

@router.get("/dashboard")
def hr_dashboard(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    from sqlalchemy import func
    total_employees = db.query(Employee).count()
    active_employees = db.query(Employee).filter(Employee.status == "active").count()
    total_departments = db.query(Department).count()
    total_payroll = db.query(func.sum(Employee.salary)).filter(Employee.status == "active").scalar() or 0

    return {
        "total_employees": total_employees,
        "active_employees": active_employees,
        "total_departments": total_departments,
        "monthly_payroll": float(total_payroll),
        "avg_salary": float(total_payroll / active_employees) if active_employees > 0 else 0
    }

## File: backend/app/routers/llm.py

from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
import json
import asyncio

from app.database import get_db
from app.models import User, LLMModel, AIConversation, AIMessage, LLMUsage, AIPromptTemplate
from app.auth import get_current_user, require_admin
from app.services.llm_service import LLMService
from app.services.activity_log import log_activity

router = APIRouter(prefix="/api/v1/llm", tags=["LLM Integration"])

# Schemas
class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    model_id: Optional[str] = None
    conversation_id: Optional[int] = None
    stream: bool = False
    temperature: float = 0.7
    system_prompt: Optional[str] = None
    template_name: Optional[str] = None
    use_tools: bool = False

class ConversationCreate(BaseModel):
    title: Optional[str] = None
    model_id: Optional[str] = None
    system_prompt: Optional[str] = None

class TemplateCreate(BaseModel):
    name: str
    display_name: str
    description: Optional[str] = None
    system_prompt: str
    user_prompt_template: Optional[str] = None
    variables: Optional[List[str]] = None
    category: str = "general"
    model_id: Optional[str] = None

class ModelUpdate(BaseModel):
    display_name: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    is_active: Optional[bool] = None
    is_default: Optional[bool] = None

# ==================== MODELS ====================

@router.get("/models")
async def list_models(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all configured LLM models."""
    models = db.query(LLMModel).all()

    # Also fetch available models from Ollama
    service = LLMService(db)
    available = await service.get_available_models()
    available_ids = {m["name"] for m in available}

    result = []
    for model in models:
        result.append({
            "id": model.id,
            "name": model.name,
            "provider": model.provider,
            "model_id": model.model_id,
            "display_name": model.display_name,
            "description": model.description,
            "parameters": model.parameters,
            "is_active": model.is_active,
            "is_default": model.is_default,
            "supports_streaming": model.supports_streaming,
            "supports_tools": model.supports_tools,
            "context_window": model.context_window,
            "is_available": model.model_id in available_ids,
            "created_at": model.created_at.isoformat() if model.created_at else None
        })

    return {"models": result, "available_from_provider": available}

@router.get("/models/{model_id}")
def get_model(
    model_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get specific model details."""
    model = db.query(LLMModel).filter(LLMModel.model_id == model_id).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return model

@router.put("/models/{model_id}")
def update_model(
    model_id: str,
    data: ModelUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Update model configuration. Admin only."""
    model = db.query(LLMModel).filter(LLMModel.model_id == model_id).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")

    if data.is_default and data.is_default != model.is_default:
        # Unset other defaults
        db.query(LLMModel).filter(LLMModel.is_default == True).update({"is_default": False})

    for key, value in data.dict(exclude_unset=True).items():
        setattr(model, key, value)

    db.commit()
    db.refresh(model)
    log_activity(db, user_id=current_user.id, action="llm_model_updated", entity_type="llm_model", entity_id=model.id)
    return model

@router.post("/models/{model_id}/pull")
async def pull_model(
    model_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Pull a model from Ollama. Admin only."""
    service = LLMService(db)
    try:
        import httpx
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(
                f"{service.ollama_base}/api/pull",
                json={"name": model_id, "stream": False}
            )
            if response.status_code == 200:
                return {"status": "success", "message": f"Model {model_id} pulled successfully"}
            return {"status": "error", "message": f"Failed to pull model: {response.text}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/models/{model_id}")
def delete_model(
    model_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Delete a model configuration. Admin only."""
    model = db.query(LLMModel).filter(LLMModel.model_id == model_id).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    db.delete(model)
    db.commit()
    return {"message": "Model deleted"}

# ==================== CHAT ====================

@router.post("/chat")
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Send a chat message to the LLM."""
    service = LLMService(db)

    # Get or create conversation
    conversation = None
    if request.conversation_id:
        conversation = db.query(AIConversation).filter(
            AIConversation.id == request.conversation_id,
            AIConversation.user_id == current_user.id
        ).first()

    if not conversation:
        model_id = request.model_id or service.default_model
        system_prompt = request.system_prompt

        if request.template_name and not system_prompt:
            template = db.query(AIPromptTemplate).filter(
                AIPromptTemplate.name == request.template_name,
                AIPromptTemplate.is_active == True
            ).first()
            if template:
                system_prompt = template.system_prompt
                if template.model_id:
                    model_id = template.model_id

        if not system_prompt:
            system_prompt = service.build_system_prompt()

        conversation = AIConversation(
            user_id=current_user.id,
            title=request.messages[0].content[:50] if request.messages else "New Chat",
            model_id=model_id,
            system_prompt=system_prompt
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)

    # Prepare messages
    messages = [{"role": m.role, "content": m.content} for m in request.messages]

    # Add previous conversation messages for context
    if conversation:
        prev_messages = db.query(AIMessage).filter(
            AIMessage.conversation_id == conversation.id
        ).order_by(AIMessage.created_at).all()

        for msg in prev_messages:
            messages.insert(0, {"role": msg.role, "content": msg.content})

    # Save user message
    user_msg = AIMessage(
        conversation_id=conversation.id,
        role="user",
        content=request.messages[-1].content if request.messages else ""
    )
    db.add(user_msg)
    db.commit()

    # Get tools if requested
    tools = None
    if request.use_tools:
        tools = service.TOOLS

    # Call LLM
    result = await service.chat(
        messages=messages,
        model_id=conversation.model_id,
        temperature=request.temperature,
        tools=tools,
        system_prompt=conversation.system_prompt
    )

    # Log usage
    service.log_usage(
        user_id=current_user.id,
        model_id=conversation.model_id,
        conversation_id=conversation.id,
        prompt_tokens=result.get("prompt_tokens", 0),
        completion_tokens=result.get("completion_tokens", 0),
        latency_ms=result.get("latency_ms", 0),
        endpoint="chat",
        success=result.get("success", False),
        error_message=result.get("error")
    )

    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["error"])

    # Handle tool calls
    if result.get("tool_calls"):
        tool_results = []
        for tool_call in result["tool_calls"]:
            tool_name = tool_call.get("function", {}).get("name")
            arguments = json.loads(tool_call.get("function", {}).get("arguments", "{}"))
            tool_result = await service.execute_tool(tool_name, arguments)
            tool_results.append({"tool": tool_name, "result": tool_result})

        # Add tool results to messages and call again
        messages.append({"role": "assistant", "content": result["content"], "tool_calls": result["tool_calls"]})
        for tr in tool_results:
            messages.append({"role": "tool", "content": json.dumps(tr["result"]), "name": tr["tool"]})

        # Second call with tool results
        result = await service.chat(
            messages=messages,
            model_id=conversation.model_id,
            temperature=request.temperature,
            system_prompt=conversation.system_prompt
        )

    # Save assistant message
    assistant_msg = AIMessage(
        conversation_id=conversation.id,
        role="assistant",
        content=result["content"],
        model_id=result["model"],
        tokens_used=result.get("total_tokens"),
        latency_ms=result.get("latency_ms")
    )
    db.add(assistant_msg)
    db.commit()

    # Update conversation
    conversation.updated_at = datetime.utcnow()
    db.commit()

    log_activity(db, user_id=current_user.id, action="ai_chat", entity_type="ai_conversation", entity_id=conversation.id)

    return {
        "conversation_id": conversation.id,
        "message": {
            "role": "assistant",
            "content": result["content"],
            "model": result["model"],
            "tokens_used": result.get("total_tokens"),
            "latency_ms": result.get("latency_ms")
        },
        "tool_results": tool_results if 'tool_results' in dir() else None
    }

@router.post("/chat/stream")
async def stream_chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Stream chat response from LLM."""
    service = LLMService(db)

    model_id = request.model_id or service.default_model
    system_prompt = request.system_prompt or service.build_system_prompt()

    messages = [{"role": m.role, "content": m.content} for m in request.messages]

    async def event_generator():
        full_content = ""
        start_time = datetime.utcnow()

        async for chunk in service.stream_chat(
            messages=messages,
            model_id=model_id,
            temperature=request.temperature,
            system_prompt=system_prompt
        ):
            data = json.loads(chunk)
            if data.get("type") == "content":
                full_content += data.get("content", "")
                yield f"data: {json.dumps({'type': 'content', 'content': data.get('content', '')})}\n\n"
            elif data.get("type") == "done":
                # Save to conversation
                conversation = AIConversation(
                    user_id=current_user.id,
                    title=messages[0]["content"][:50] if messages else "Stream Chat",
                    model_id=model_id,
                    system_prompt=system_prompt
                )
                db.add(conversation)
                db.commit()
                db.refresh(conversation)

                # Save messages
                for msg in messages:
                    db.add(AIMessage(conversation_id=conversation.id, role=msg["role"], content=msg["content"]))
                db.add(AIMessage(
                    conversation_id=conversation.id,
                    role="assistant",
                    content=full_content,
                    model_id=model_id
                ))
                db.commit()

                # Log usage
                service.log_usage(
                    user_id=current_user.id,
                    model_id=model_id,
                    conversation_id=conversation.id,
                    prompt_tokens=data.get("prompt_tokens", 0),
                    completion_tokens=data.get("completion_tokens", 0),
                    total_tokens=data.get("total_tokens", 0),
                    endpoint="chat_stream",
                    success=True
                )

                yield f"data: {json.dumps({'type': 'done', 'conversation_id': conversation.id, 'total_tokens': data.get('total_tokens', 0)})}\n\n"
            elif data.get("type") == "error":
                yield f"data: {json.dumps({'type': 'error', 'error': data.get('error')})}\n\n"

        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )

# ==================== CONVERSATIONS ====================

@router.get("/conversations")
def list_conversations(
    archived: bool = False,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List user's AI conversations."""
    conversations = db.query(AIConversation).filter(
        AIConversation.user_id == current_user.id,
        AIConversation.is_archived == archived
    ).order_by(AIConversation.updated_at.desc()).all()

    return [
        {
            "id": c.id,
            "title": c.title,
            "model_id": c.model_id,
            "message_count": len(c.messages),
            "created_at": c.created_at.isoformat() if c.created_at else None,
            "updated_at": c.updated_at.isoformat() if c.updated_at else None
        }
        for c in conversations
    ]

@router.get("/conversations/{conversation_id}")
def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get conversation with messages."""
    conversation = db.query(AIConversation).filter(
        AIConversation.id == conversation_id,
        AIConversation.user_id == current_user.id
    ).first()

    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return {
        "id": conversation.id,
        "title": conversation.title,
        "model_id": conversation.model_id,
        "system_prompt": conversation.system_prompt,
        "messages": [
            {
                "id": m.id,
                "role": m.role,
                "content": m.content,
                "model_id": m.model_id,
                "tokens_used": m.tokens_used,
                "created_at": m.created_at.isoformat() if m.created_at else None
            }
            for m in conversation.messages
        ],
        "created_at": conversation.created_at.isoformat() if conversation.created_at else None,
        "updated_at": conversation.updated_at.isoformat() if conversation.updated_at else None
    }

@router.post("/conversations")
def create_conversation(
    data: ConversationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new conversation."""
    service = LLMService(db)
    model_id = data.model_id or service.default_model
    system_prompt = data.system_prompt or service.build_system_prompt()

    conversation = AIConversation(
        user_id=current_user.id,
        title=data.title or "New Conversation",
        model_id=model_id,
        system_prompt=system_prompt
    )
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation

@router.put("/conversations/{conversation_id}/archive")
def archive_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Archive a conversation."""
    conversation = db.query(AIConversation).filter(
        AIConversation.id == conversation_id,
        AIConversation.user_id == current_user.id
    ).first()

    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    conversation.is_archived = True
    db.commit()
    return {"message": "Conversation archived"}

@router.delete("/conversations/{conversation_id}")
def delete_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a conversation."""
    conversation = db.query(AIConversation).filter(
        AIConversation.id == conversation_id,
        AIConversation.user_id == current_user.id
    ).first()

    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    db.delete(conversation)
    db.commit()
    return {"message": "Conversation deleted"}

# ==================== TEMPLATES ====================

@router.get("/templates")
def list_templates(
    category: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List AI prompt templates."""
    query = db.query(AIPromptTemplate).filter(AIPromptTemplate.is_active == True)
    if category:
        query = query.filter(AIPromptTemplate.category == category)
    return query.all()

@router.get("/templates/{template_name}")
def get_template(
    template_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get specific template."""
    template = db.query(AIPromptTemplate).filter(
        AIPromptTemplate.name == template_name,
        AIPromptTemplate.is_active == True
    ).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template

@router.post("/templates")
def create_template(
    data: TemplateCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Create a new prompt template. Admin only."""
    existing = db.query(AIPromptTemplate).filter(AIPromptTemplate.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Template name already exists")

    template = AIPromptTemplate(**data.dict(), created_by=current_user.id)
    db.add(template)
    db.commit()
    db.refresh(template)
    log_activity(db, user_id=current_user.id, action="template_created", entity_type="ai_template", entity_id=template.id)
    return template

@router.delete("/templates/{template_id}")
def delete_template(
    template_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Delete a template. Admin only."""
    template = db.query(AIPromptTemplate).filter(AIPromptTemplate.id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    db.delete(template)
    db.commit()
    return {"message": "Template deleted"}

# ==================== ANALYTICS ====================

@router.get("/analytics/usage")
def get_usage_analytics(
    days: int = Query(default=30, ge=1, le=365),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get LLM usage analytics."""
    from datetime import datetime, timedelta
    from sqlalchemy import func

    start_date = datetime.utcnow() - timedelta(days=days)

    # Total usage
    total = db.query(LLMUsage).filter(LLMUsage.created_at >= start_date).count()
    total_tokens = db.query(func.sum(LLMUsage.total_tokens)).filter(LLMUsage.created_at >= start_date).scalar() or 0
    total_prompt = db.query(func.sum(LLMUsage.prompt_tokens)).filter(LLMUsage.created_at >= start_date).scalar() or 0
    total_completion = db.query(func.sum(LLMUsage.completion_tokens)).filter(LLMUsage.created_at >= start_date).scalar() or 0
    avg_latency = db.query(func.avg(LLMUsage.latency_ms)).filter(LLMUsage.created_at >= start_date).scalar() or 0

    # By model
    by_model = db.query(
        LLMUsage.model_id,
        func.count(LLMUsage.id).label("count"),
        func.sum(LLMUsage.total_tokens).label("tokens"),
        func.avg(LLMUsage.latency_ms).label("avg_latency")
    ).filter(LLMUsage.created_at >= start_date).group_by(LLMUsage.model_id).all()

    # By day
    by_day = db.query(
        func.date(LLMUsage.created_at).label("date"),
        func.count(LLMUsage.id).label("count"),
        func.sum(LLMUsage.total_tokens).label("tokens")
    ).filter(LLMUsage.created_at >= start_date).group_by(func.date(LLMUsage.created_at)).order_by("date").all()

    # By endpoint
    by_endpoint = db.query(
        LLMUsage.endpoint,
        func.count(LLMUsage.id).label("count"),
        func.sum(LLMUsage.total_tokens).label("tokens")
    ).filter(LLMUsage.created_at >= start_date).group_by(LLMUsage.endpoint).all()

    # Error rate
    errors = db.query(LLMUsage).filter(
        LLMUsage.created_at >= start_date,
        LLMUsage.success == False
    ).count()

    return {
        "period_days": days,
        "total_requests": total,
        "total_tokens": int(total_tokens),
        "prompt_tokens": int(total_prompt),
        "completion_tokens": int(total_completion),
        "avg_latency_ms": round(float(avg_latency), 2) if avg_latency else 0,
        "error_rate": (errors / total * 100) if total > 0 else 0,
        "by_model": [
            {"model": m.model_id, "requests": m.count, "tokens": int(m.tokens or 0), "avg_latency_ms": round(float(m.avg_latency or 0), 2)}
            for m in by_model
        ],
        "by_day": [
            {"date": str(d.date), "requests": d.count, "tokens": int(d.tokens or 0)}
            for d in by_day
        ],
        "by_endpoint": [
            {"endpoint": e.endpoint, "requests": e.count, "tokens": int(e.tokens or 0)}
            for e in by_endpoint
        ]
    }

@router.get("/analytics/conversations")
def get_conversation_analytics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get conversation analytics."""
    from sqlalchemy import func

    total_conversations = db.query(AIConversation).count()
    total_messages = db.query(AIMessage).count()
    avg_messages_per_conv = total_messages / total_conversations if total_conversations > 0 else 0

    # Most active users
    top_users = db.query(
        AIMessage.conversation_id,
        func.count(AIMessage.id).label("msg_count")
    ).group_by(AIMessage.conversation_id).order_by(func.count(AIMessage.id).desc()).limit(10).all()

    return {
        "total_conversations": total_conversations,
        "total_messages": total_messages,
        "avg_messages_per_conversation": round(avg_messages_per_conv, 2),
        "top_conversations": [
            {"conversation_id": t.conversation_id, "message_count": t.msg_count}
            for t in top_users
        ]
    }

from datetime import datetime

## File: backend/app/routers/websocket.py

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from typing import Dict, List
import json
import asyncio

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        if client_id not in self.active_connections:
            self.active_connections[client_id] = []
        self.active_connections[client_id].append(websocket)

    def disconnect(self, websocket: WebSocket, client_id: str):
        if client_id in self.active_connections:
            self.active_connections[client_id].remove(websocket)
            if not self.active_connections[client_id]:
                del self.active_connections[client_id]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, client_id: str = None):
        if client_id and client_id in self.active_connections:
            for connection in self.active_connections[client_id]:
                await connection.send_text(message)
        else:
            for connections in self.active_connections.values():
                for connection in connections:
                    await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)

            if message.get("type") == "ping":
                await manager.send_personal_message(
                    json.dumps({"type": "pong", "timestamp": str(asyncio.get_event_loop().time())}),
                    websocket
                )
            elif message.get("type") == "subscribe":
                channel = message.get("channel", "general")
                await manager.send_personal_message(
                    json.dumps({"type": "subscribed", "channel": channel}),
                    websocket
                )
            else:
                await manager.broadcast(
                    json.dumps({"type": "message", "data": message, "from": client_id}),
                    message.get("channel", client_id)
                )
    except WebSocketDisconnect:
        manager.disconnect(websocket, client_id)
    except Exception:
        manager.disconnect(websocket, client_id)

@router.post("/broadcast")
async def broadcast_message(message: dict):
    await manager.broadcast(json.dumps(message))
    return {"status": "sent"}

## File: backend/app/routers/permissions.py

from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models import User, Role, Permission, RolePermission, UserRole, FieldPermission, DataPolicy
from app.auth import get_current_user, require_admin, require_superadmin, has_permission, get_user_permissions
from app.services.activity_log import log_activity

router = APIRouter(prefix="/api/v1/permissions", tags=["Permissions & RBAC"])

# Schemas
class RoleCreate(BaseModel):
    name: str
    display_name: str
    description: Optional[str] = None

class RoleUpdate(BaseModel):
    display_name: Optional[str] = None
    description: Optional[str] = None

class PermissionAssign(BaseModel):
    permission_ids: List[int]

class UserRoleAssign(BaseModel):
    role_ids: List[int]

class FieldPermissionCreate(BaseModel):
    role_id: int
    resource: str
    field_name: str
    access_level: str = "read"  # read, write, hidden

class DataPolicyCreate(BaseModel):
    name: str
    resource: str
    role_id: int
    condition: Optional[Dict[str, Any]] = None
    effect: str = "allow"  # allow, deny
    priority: int = 100

class PermissionResponse(BaseModel):
    id: int
    name: str
    resource: str
    action: str
    description: Optional[str]

    class Config:
        from_attributes = True

class RoleResponse(BaseModel):
    id: int
    name: str
    display_name: str
    description: Optional[str]
    is_system: bool
    permissions: List[PermissionResponse] = []

    class Config:
        from_attributes = True

class FieldPermissionResponse(BaseModel):
    id: int
    role_id: int
    resource: str
    field_name: str
    access_level: str

    class Config:
        from_attributes = True

class DataPolicyResponse(BaseModel):
    id: int
    name: str
    resource: str
    role_id: int
    condition: Optional[Dict[str, Any]]
    effect: str
    priority: int
    is_active: bool

    class Config:
        from_attributes = True

# ==================== ROLES ====================

@router.get("/roles", response_model=List[RoleResponse])
def list_roles(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """List all roles with their permissions. Admin only."""
    roles = db.query(Role).all()
    result = []
    for role in roles:
        role_data = RoleResponse(
            id=role.id,
            name=role.name,
            display_name=role.display_name,
            description=role.description,
            is_system=role.is_system,
            permissions=[
                PermissionResponse(id=p.id, name=p.name, resource=p.resource, action=p.action, description=p.description)
                for p in role.permissions
            ]
        )
        result.append(role_data)
    return result

@router.post("/roles", response_model=RoleResponse)
def create_role(
    data: RoleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Create a new role. Admin only."""
    existing = db.query(Role).filter(Role.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Role name already exists")

    role = Role(name=data.name, display_name=data.display_name, description=data.description)
    db.add(role)
    db.commit()
    db.refresh(role)

    log_activity(db, user_id=current_user.id, action="role_created", entity_type="role", entity_id=role.id)
    return RoleResponse(id=role.id, name=role.name, display_name=role.display_name, description=role.description, is_system=role.is_system)

@router.get("/roles/{role_id}", response_model=RoleResponse)
def get_role(
    role_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Get role details with permissions. Admin only."""
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    return RoleResponse(
        id=role.id,
        name=role.name,
        display_name=role.display_name,
        description=role.description,
        is_system=role.is_system,
        permissions=[
            PermissionResponse(id=p.id, name=p.name, resource=p.resource, action=p.action, description=p.description)
            for p in role.permissions
        ]
    )

@router.put("/roles/{role_id}", response_model=RoleResponse)
def update_role(
    role_id: int,
    data: RoleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Update role details. Admin only. System roles cannot be modified."""
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    if role.is_system:
        raise HTTPException(status_code=400, detail="Cannot modify system roles")

    if data.display_name:
        role.display_name = data.display_name
    if data.description is not None:
        role.description = data.description

    db.commit()
    db.refresh(role)
    return RoleResponse(id=role.id, name=role.name, display_name=role.display_name, description=role.description, is_system=role.is_system)

@router.delete("/roles/{role_id}")
def delete_role(
    role_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_superadmin)
):
    """Delete a role. Superadmin only. System roles cannot be deleted."""
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    if role.is_system:
        raise HTTPException(status_code=400, detail="Cannot delete system roles")

    db.delete(role)
    db.commit()
    log_activity(db, user_id=current_user.id, action="role_deleted", entity_type="role", entity_id=role_id)
    return {"message": "Role deleted"}

# ==================== PERMISSIONS ====================

@router.get("/permissions", response_model=List[PermissionResponse])
def list_permissions(
    resource: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """List all permissions. Admin only."""
    query = db.query(Permission)
    if resource:
        query = query.filter(Permission.resource == resource)
    return query.all()

@router.post("/roles/{role_id}/permissions")
def assign_permissions_to_role(
    role_id: int,
    data: PermissionAssign,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Assign permissions to a role. Admin only."""
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    # Clear existing and add new
    db.query(RolePermission).filter(RolePermission.role_id == role_id).delete()

    for perm_id in data.permission_ids:
        perm = db.query(Permission).filter(Permission.id == perm_id).first()
        if perm:
            rp = RolePermission(role_id=role_id, permission_id=perm_id)
            db.add(rp)

    db.commit()
    log_activity(db, user_id=current_user.id, action="permissions_assigned", entity_type="role", entity_id=role_id, details={"permission_ids": data.permission_ids})
    return {"message": f"Assigned {len(data.permission_ids)} permissions to role"}

# ==================== USER ROLES ====================

@router.get("/users/{user_id}/roles")
def get_user_roles(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Get roles assigned to a user. Admin only."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user_id": user_id,
        "roles": [
            {"id": r.id, "name": r.name, "display_name": r.display_name}
            for r in user.roles
        ]
    }

@router.post("/users/{user_id}/roles")
def assign_roles_to_user(
    user_id: int,
    data: UserRoleAssign,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Assign roles to a user. Admin only."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Clear existing roles (except system default)
    db.query(UserRole).filter(UserRole.user_id == user_id).delete()

    for role_id in data.role_ids:
        role = db.query(Role).filter(Role.id == role_id).first()
        if role:
            ur = UserRole(user_id=user_id, role_id=role_id)
            db.add(ur)

    db.commit()
    log_activity(db, user_id=current_user.id, action="roles_assigned", entity_type="user", entity_id=user_id, details={"role_ids": data.role_ids})
    return {"message": f"Assigned {len(data.role_ids)} roles to user"}

# ==================== FIELD PERMISSIONS ====================

@router.get("/field-permissions", response_model=List[FieldPermissionResponse])
def list_field_permissions(
    role_id: Optional[int] = None,
    resource: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """List field-level permissions. Admin only."""
    query = db.query(FieldPermission)
    if role_id:
        query = query.filter(FieldPermission.role_id == role_id)
    if resource:
        query = query.filter(FieldPermission.resource == resource)
    return query.all()

@router.post("/field-permissions", response_model=FieldPermissionResponse)
def create_field_permission(
    data: FieldPermissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Create a field-level permission. Admin only."""
    role = db.query(Role).filter(Role.id == data.role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    # Check if already exists
    existing = db.query(FieldPermission).filter(
        FieldPermission.role_id == data.role_id,
        FieldPermission.resource == data.resource,
        FieldPermission.field_name == data.field_name
    ).first()

    if existing:
        existing.access_level = data.access_level
        db.commit()
        db.refresh(existing)
        return existing

    fp = FieldPermission(**data.dict())
    db.add(fp)
    db.commit()
    db.refresh(fp)

    log_activity(db, user_id=current_user.id, action="field_permission_created", entity_type="field_permission", entity_id=fp.id)
    return fp

@router.delete("/field-permissions/{fp_id}")
def delete_field_permission(
    fp_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Delete a field permission. Admin only."""
    fp = db.query(FieldPermission).filter(FieldPermission.id == fp_id).first()
    if not fp:
        raise HTTPException(status_code=404, detail="Field permission not found")
    db.delete(fp)
    db.commit()
    return {"message": "Field permission deleted"}

# ==================== DATA POLICIES ====================

@router.get("/data-policies", response_model=List[DataPolicyResponse])
def list_data_policies(
    resource: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """List data policies (row-level access). Admin only."""
    query = db.query(DataPolicy)
    if resource:
        query = query.filter(DataPolicy.resource == resource)
    return query.all()

@router.post("/data-policies", response_model=DataPolicyResponse)
def create_data_policy(
    data: DataPolicyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Create a data policy. Admin only."""
    role = db.query(Role).filter(Role.id == data.role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    policy = DataPolicy(**data.dict())
    db.add(policy)
    db.commit()
    db.refresh(policy)

    log_activity(db, user_id=current_user.id, action="data_policy_created", entity_type="data_policy", entity_id=policy.id)
    return policy

@router.put("/data-policies/{policy_id}/toggle")
def toggle_data_policy(
    policy_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Toggle a data policy active/inactive. Admin only."""
    policy = db.query(DataPolicy).filter(DataPolicy.id == policy_id).first()
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    policy.is_active = not policy.is_active
    db.commit()
    db.refresh(policy)
    return policy

@router.delete("/data-policies/{policy_id}")
def delete_data_policy(
    policy_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Delete a data policy. Admin only."""
    policy = db.query(DataPolicy).filter(DataPolicy.id == policy_id).first()
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    db.delete(policy)
    db.commit()
    return {"message": "Data policy deleted"}

# ==================== MY PERMISSIONS ====================

@router.get("/me")
def get_my_permissions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get current user's permissions and roles."""
    permissions = get_user_permissions(current_user, db)
    roles = [r.name for r in current_user.roles]

    # Get field permissions for all resources
    field_perms = {}
    for role in current_user.roles:
        for fp in role.field_permissions:
            key = f"{fp.resource}.{fp.field_name}"
            if key not in field_perms:
                field_perms[key] = fp.access_level
            else:
                # Higher access wins
                levels = {"hidden": 0, "read": 1, "write": 2}
                if levels.get(fp.access_level, 0) > levels.get(field_perms[key], 0):
                    field_perms[key] = fp.access_level

    return {
        "user_id": current_user.id,
        "email": current_user.email,
        "roles": roles,
        "permissions": permissions,
        "field_permissions": field_perms,
        "is_admin": "admin" in roles or "superadmin" in roles,
        "is_superadmin": "superadmin" in roles
    }

## File: backend/app/routers/ai.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
import httpx
import json

from app.database import get_db
from app.models import Contact, Company, Deal, Product, Invoice, Project, Task
from app.auth import get_current_user
from app.config import settings
from app.services.activity_log import log_activity

router = APIRouter()

class ChatMessage(BaseModel):
    message: str
    context: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    sources: Optional[List[str]] = None

async def query_ollama(prompt: str, model: str = None) -> str:
    model = model or settings.OLLAMA_MODEL
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{settings.OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            if response.status_code == 200:
                data = response.json()
                return data.get("response", "No response from AI")
            return f"AI service unavailable (status: {response.status_code})"
    except Exception as e:
        return f"AI service error: {str(e)}"

@router.post("/chat", response_model=ChatResponse)
async def chat(
    message: ChatMessage,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # Gather business context
    context_data = {}

    # Recent contacts
    context_data["contacts_count"] = db.query(Contact).count()
    context_data["recent_contacts"] = [
        {"name": f"{c.first_name} {c.last_name}", "status": c.status}
        for c in db.query(Contact).order_by(Contact.created_at.desc()).limit(5).all()
    ]

    # Pipeline
    deals = db.query(Deal).all()
    pipeline_value = sum(d.value or 0 for d in deals if d.stage != "closed_lost")
    context_data["pipeline_value"] = float(pipeline_value)
    context_data["deals_by_stage"] = {}
    for stage in ["prospect", "qualification", "proposal", "negotiation", "closed_won", "closed_lost"]:
        stage_deals = [d for d in deals if d.stage == stage]
        context_data["deals_by_stage"][stage] = {
            "count": len(stage_deals),
            "value": float(sum(d.value or 0 for d in stage_deals))
        }

    # Inventory
    products = db.query(Product).all()
    low_stock = [p for p in products if p.quantity_in_stock <= p.reorder_level]
    context_data["total_products"] = len(products)
    context_data["low_stock_count"] = len(low_stock)
    context_data["low_stock_items"] = [
        {"name": p.name, "stock": p.quantity_in_stock, "reorder": p.reorder_level}
        for p in low_stock[:5]
    ]

    # Projects
    tasks = db.query(Task).all()
    context_data["total_tasks"] = len(tasks)
    context_data["overdue_tasks"] = len([t for t in tasks if t.due_date and t.status != "done"])

    prompt = f"""You are an AI business assistant for an ERP system. Answer the user's question concisely and helpfully.

Business Context:
{json.dumps(context_data, indent=2, default=str)}

User Question: {message.message}

Provide a helpful, data-driven response. If you don't have specific data, say so."""

    response_text = await query_ollama(prompt)

    log_activity(db, user_id=current_user.id, action="ai_chat", entity_type="ai", details={"query": message.message[:200]})

    return ChatResponse(response=response_text)

@router.get("/insights")
async def get_ai_insights(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    from sqlalchemy import func
    from datetime import datetime, timedelta

    # Revenue insights
    last_month = datetime.now() - timedelta(days=30)
    invoices = db.query(Invoice).filter(Invoice.created_at >= last_month).all()
    revenue = sum(i.total or 0 for i in invoices)

    # Churn risk
    inactive_contacts = db.query(Contact).filter(
        Contact.last_activity < datetime.now() - timedelta(days=90)
    ).all()

    # Stock alerts
    low_stock = db.query(Product).filter(Product.quantity_in_stock <= Product.reorder_level).all()

    insights = []

    if revenue > 0:
        insights.append({
            "category": "revenue",
            "priority": "medium",
            "message": f"Revenue in last 30 days: ${revenue:,.2f}"
        })

    if inactive_contacts:
        insights.append({
            "category": "growth",
            "priority": "high",
            "message": f"{len(inactive_contacts)} contacts have been inactive for 90+ days. Consider re-engagement campaigns."
        })

    if low_stock:
        insights.append({
            "category": "operations",
            "priority": "high",
            "message": f"{len(low_stock)} products are below reorder level. Restock recommended."
        })

    # Get AI-generated summary
    prompt = f"""Analyze this business data and provide 3-5 actionable insights:
- Revenue last 30 days: ${revenue:,.2f}
- Inactive contacts: {len(inactive_contacts)}
- Low stock products: {len(low_stock)}
- Total deals: {db.query(Deal).count()}
- Active projects: {db.query(Project).filter(Project.status == 'active').count()}

Format as JSON with fields: category, priority, message."""

    ai_response = await query_ollama(prompt)

    return {
        "insights": insights,
        "ai_summary": ai_response,
        "health_score": "good" if len([i for i in insights if i["priority"] == "high"]) < 3 else "fair"
    }

@router.get("/forecast/revenue")
async def forecast_revenue(
    months: int = 3,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    from datetime import datetime, timedelta
    from sqlalchemy import func

    # Get last 6 months of paid invoices
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)

    monthly_data = db.query(
        func.extract('month', Invoice.created_at).label('month'),
        func.extract('year', Invoice.created_at).label('year'),
        func.sum(Invoice.total).label('total')
    ).filter(
        Invoice.created_at >= start_date,
        Invoice.status == "paid"
    ).group_by('year', 'month').order_by('year', 'month').all()

    if not monthly_data:
        return {"forecast": [], "message": "Insufficient data for forecasting"}

    values = [float(m.total) for m in monthly_data]
    avg_growth = sum((values[i] - values[i-1]) / values[i-1] * 100 for i in range(1, len(values))) / max(1, len(values) - 1) if len(values) > 1 else 0

    forecast = []
    last_value = values[-1] if values else 0

    for i in range(1, months + 1):
        predicted = last_value * (1 + avg_growth / 100) ** i
        forecast.append({
            "month": i,
            "predicted_revenue": round(predicted, 2),
            "confidence_low": round(predicted * 0.8, 2),
            "confidence_high": round(predicted * 1.2, 2),
            "growth_rate": round(avg_growth, 2)
        })

    return {
        "historical": [{"month": f"{m.year}-{m.month}", "revenue": float(m.total)} for m in monthly_data],
        "forecast": forecast,
        "trend": "increasing" if avg_growth > 0 else "decreasing" if avg_growth < 0 else "stable",
        "confidence": "medium"
    }

## File: backend/app/routers/admin.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, Dict, Any

from app.database import get_db
from app.models import User, Setting, ActivityLog, Notification
from app.auth import get_current_user, require_admin

router = APIRouter()

class SettingCreate(BaseModel):
    key: str
    value: str
    category: str = "general"
    is_encrypted: bool = False
    description: Optional[str] = None

@router.get("/settings")
def get_settings(
    category: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    query = db.query(Setting)
    if category:
        query = query.filter(Setting.category == category)
    return query.all()

@router.post("/settings")
def create_setting(data: SettingCreate, db: Session = Depends(get_db), current_user = Depends(require_admin)):
    existing = db.query(Setting).filter(Setting.key == data.key).first()
    if existing:
        existing.value = data.value
        existing.category = data.category
        existing.is_encrypted = data.is_encrypted
        db.commit()
        db.refresh(existing)
        return existing

    setting = Setting(**data.dict())
    db.add(setting)
    db.commit()
    db.refresh(setting)
    return setting

@router.delete("/settings/{key}")
def delete_setting(key: str, db: Session = Depends(get_db), current_user = Depends(require_admin)):
    setting = db.query(Setting).filter(Setting.key == key).first()
    if not setting:
        raise HTTPException(status_code=404, detail="Setting not found")
    db.delete(setting)
    db.commit()
    return {"message": "Setting deleted"}

@router.get("/activity-logs")
def get_activity_logs(
    skip: int = 0,
    limit: int = 100,
    user_id: Optional[int] = None,
    entity_type: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    query = db.query(ActivityLog)
    if user_id:
        query = query.filter(ActivityLog.user_id == user_id)
    if entity_type:
        query = query.filter(ActivityLog.entity_type == entity_type)
    return query.order_by(ActivityLog.created_at.desc()).offset(skip).limit(limit).all()

@router.get("/notifications")
def get_notifications(
    unread_only: bool = False,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = db.query(Notification).filter(Notification.user_id == current_user.id)
    if unread_only:
        query = query.filter(Notification.is_read == False)
    return query.order_by(Notification.created_at.desc()).all()

@router.put("/notifications/{notif_id}/read")
def mark_read(notif_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    notif = db.query(Notification).filter(Notification.id == notif_id, Notification.user_id == current_user.id).first()
    if notif:
        notif.is_read = True
        db.commit()
    return notif

@router.get("/stats")
def admin_stats(db: Session = Depends(get_db), current_user = Depends(require_admin)):
    from sqlalchemy import func
    return {
        "total_users": db.query(User).count(),
        "active_users": db.query(User).filter(User.is_active == True).count(),
        "total_activity": db.query(ActivityLog).count(),
        "today_activity": db.query(ActivityLog).filter(
            func.date(ActivityLog.created_at) == func.date(func.now())
        ).count()
    }

## File: backend/app/routers/integrations.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, Dict, Any
import httpx
import hmac
import hashlib
import json

from app.database import get_db
from app.models import Integration, Webhook, WebhookDelivery
from app.auth import get_current_user
from app.config import settings
from app.services.activity_log import log_activity

router = APIRouter()

class IntegrationCreate(BaseModel):
    name: str
    provider: str
    config: Dict[str, Any]

class WebhookCreate(BaseModel):
    name: str
    url: str
    events: list[str]
    secret: Optional[str] = None

@router.post("/integrations")
def create_integration(data: IntegrationCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    integration = Integration(**data.dict(), created_by=current_user.id)
    db.add(integration)
    db.commit()
    db.refresh(integration)
    return integration

@router.get("/integrations")
def list_integrations(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.query(Integration).all()

@router.post("/webhooks")
def create_webhook(data: WebhookCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    webhook = Webhook(**data.dict(), created_by=current_user.id)
    db.add(webhook)
    db.commit()
    db.refresh(webhook)
    return webhook

@router.get("/webhooks")
def list_webhooks(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.query(Webhook).all()

@router.post("/webhooks/{webhook_id}/test")
async def test_webhook(webhook_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    webhook = db.query(Webhook).filter(Webhook.id == webhook_id).first()
    if not webhook:
        raise HTTPException(status_code=404, detail="Webhook not found")

    payload = {"event": "test", "timestamp": str(datetime.now()), "data": {"message": "Test webhook delivery"}}

    headers = {"Content-Type": "application/json"}
    if webhook.secret:
        signature = hmac.new(webhook.secret.encode(), json.dumps(payload).encode(), hashlib.sha256).hexdigest()
        headers["X-Webhook-Signature"] = f"sha256={signature}"

    delivery = WebhookDelivery(
        webhook_id=webhook_id,
        event="test",
        payload=payload,
        attempt=1
    )
    db.add(delivery)

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(webhook.url, json=payload, headers=headers)
            delivery.response_status = response.status_code
            delivery.response_body = response.text[:1000]
            delivery.status = "delivered" if response.status_code < 400 else "failed"
    except Exception as e:
        delivery.status = "failed"
        delivery.response_body = str(e)[:1000]

    db.commit()
    db.refresh(delivery)
    return delivery

@router.get("/webhooks/{webhook_id}/deliveries")
def get_deliveries(webhook_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.query(WebhookDelivery).filter(WebhookDelivery.webhook_id == webhook_id).order_by(WebhookDelivery.created_at.desc()).all()

from datetime import datetime

## File: backend/app/routers/projects.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

from app.database import get_db
from app.models import Project, Task
from app.auth import get_current_user
from app.services.activity_log import log_activity

router = APIRouter()

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    status: str = "planning"
    priority: str = "medium"
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    budget: Optional[float] = None
    client_id: Optional[int] = None

class TaskCreate(BaseModel):
    project_id: int
    title: str
    description: Optional[str] = None
    status: str = "todo"
    priority: str = "medium"
    assigned_to: Optional[int] = None
    due_date: Optional[date] = None
    estimated_hours: Optional[float] = None
    parent_task_id: Optional[int] = None

@router.post("/projects")
def create_project(data: ProjectCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    project = Project(**data.dict(), manager_id=current_user.id)
    db.add(project)
    db.commit()
    db.refresh(project)
    log_activity(db, user_id=current_user.id, action="project_created", entity_type="project", entity_id=project.id)
    return project

@router.get("/projects")
def list_projects(
    status: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = db.query(Project)
    if status:
        query = query.filter(Project.status == status)
    return query.all()

@router.get("/projects/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/projects/{project_id}")
def update_project(project_id: int, data: ProjectCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    for key, value in data.dict().items():
        setattr(project, key, value)
    project.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(project)
    return project

@router.post("/tasks")
def create_task(data: TaskCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == data.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    task = Task(**data.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    log_activity(db, user_id=current_user.id, action="task_created", entity_type="task", entity_id=task.id)
    return task

@router.get("/projects/{project_id}/tasks")
def list_project_tasks(project_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.query(Task).filter(Task.project_id == project_id).all()

@router.put("/tasks/{task_id}")
def update_task(task_id: int, data: dict, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in data.items():
        if hasattr(task, key):
            setattr(task, key, value)
    task.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(task)
    return task

@router.get("/dashboard")
def projects_dashboard(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    from sqlalchemy import func
    total_projects = db.query(Project).count()
    active_projects = db.query(Project).filter(Project.status == "active").count()
    total_tasks = db.query(Task).count()
    completed_tasks = db.query(Task).filter(Task.status == "done").count()

    return {
        "total_projects": total_projects,
        "active_projects": active_projects,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "completion_rate": (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    }

## File: backend/app/services/__init__.py

## File: backend/app/services/activity_log.py

from sqlalchemy.orm import Session
from app.models import ActivityLog
from typing import Optional, Dict, Any

def log_activity(
    db: Session,
    user_id: Optional[int] = None,
    action: str = "",
    entity_type: Optional[str] = None,
    entity_id: Optional[int] = None,
    details: Optional[Dict[str, Any]] = None,
    ip_address: Optional[str] = None,
    user_agent: Optional[str] = None
):
    """Log an activity to the database."""
    log = ActivityLog(
        user_id=user_id,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        details=details,
        ip_address=ip_address,
        user_agent=user_agent
    )
    db.add(log)
    db.commit()
    return log

## File: backend/app/services/llm_service.py

import json
import time
from typing import AsyncGenerator, Dict, Any, List, Optional, Callable
from datetime import datetime
import httpx
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import LLMModel, AIConversation, AIMessage, LLMUsage, Contact, Company, Deal, Product, Invoice, Project, Task
from app.config import settings

class LLMService:
    """Service for managing LLM interactions with multi-model support."""

    def __init__(self, db: Session = None):
        self.db = db
        self.ollama_base = settings.OLLAMA_BASE_URL
        self.default_model = settings.OLLAMA_MODEL

    async def get_available_models(self) -> List[Dict[str, Any]]:
        """Get list of available models from Ollama."""
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(f"{self.ollama_base}/api/tags")
                if response.status_code == 200:
                    data = response.json()
                    models = data.get("models", [])
                    return [
                        {
                            "name": m.get("name"),
                            "size": m.get("size"),
                            "modified_at": m.get("modified_at"),
                            "digest": m.get("digest")
                        }
                        for m in models
                    ]
                return []
        except Exception:
            return []

    async def chat(
        self,
        messages: List[Dict[str, str]],
        model_id: str = None,
        stream: bool = False,
        temperature: float = 0.7,
        tools: List[Dict[str, Any]] = None,
        system_prompt: str = None
    ) -> Dict[str, Any]:
        """Send chat completion request to LLM."""
        model_id = model_id or self.default_model

        # Build request payload
        payload = {
            "model": model_id,
            "messages": messages,
            "stream": stream,
            "options": {
                "temperature": temperature
            }
        }

        if system_prompt:
            # Prepend system message
            payload["messages"] = [{"role": "system", "content": system_prompt}] + messages

        if tools:
            payload["tools"] = tools

        start_time = time.time()

        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                response = await client.post(
                    f"{self.ollama_base}/api/chat",
                    json=payload
                )

                latency_ms = int((time.time() - start_time) * 1000)

                if response.status_code != 200:
                    return {
                        "success": False,
                        "error": f"LLM API error: {response.status_code}",
                        "latency_ms": latency_ms
                    }

                data = response.json()

                # Extract response
                message = data.get("message", {})
                content = message.get("content", "")

                # Extract token usage if available
                prompt_tokens = data.get("prompt_eval_count", 0)
                completion_tokens = data.get("eval_count", 0)
                total_tokens = prompt_tokens + completion_tokens

                # Check for tool calls
                tool_calls = None
                if message.get("tool_calls"):
                    tool_calls = message["tool_calls"]

                return {
                    "success": True,
                    "content": content,
                    "model": model_id,
                    "prompt_tokens": prompt_tokens,
                    "completion_tokens": completion_tokens,
                    "total_tokens": total_tokens,
                    "latency_ms": latency_ms,
                    "tool_calls": tool_calls,
                    "done": data.get("done", True)
                }

        except httpx.TimeoutException:
            return {
                "success": False,
                "error": "LLM request timed out",
                "latency_ms": int((time.time() - start_time) * 1000)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "latency_ms": int((time.time() - start_time) * 1000)
            }

    async def stream_chat(
        self,
        messages: List[Dict[str, str]],
        model_id: str = None,
        temperature: float = 0.7,
        system_prompt: str = None
    ) -> AsyncGenerator[str, None]:
        """Stream chat completion from LLM."""
        model_id = model_id or self.default_model

        payload = {
            "model": model_id,
            "messages": messages,
            "stream": True,
            "options": {
                "temperature": temperature
            }
        }

        if system_prompt:
            payload["messages"] = [{"role": "system", "content": system_prompt}] + messages

        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                async with client.stream(
                    "POST",
                    f"{self.ollama_base}/api/chat",
                    json=payload
                ) as response:
                    async for line in response.aiter_lines():
                        if line.strip():
                            try:
                                data = json.loads(line)
                                if "message" in data and "content" in data["message"]:
                                    content = data["message"]["content"]
                                    if content:
                                        yield json.dumps({
                                            "type": "content",
                                            "content": content,
                                            "done": data.get("done", False)
                                        }) + "\n"

                                if data.get("done"):
                                    yield json.dumps({
                                        "type": "done",
                                        "prompt_tokens": data.get("prompt_eval_count", 0),
                                        "completion_tokens": data.get("eval_count", 0),
                                        "total_tokens": (data.get("prompt_eval_count", 0) + data.get("eval_count", 0))
                                    }) + "\n"

                            except json.JSONDecodeError:
                                continue

        except Exception as e:
            yield json.dumps({"type": "error", "error": str(e)}) + "\n"

    def log_usage(
        self,
        user_id: int,
        model_id: str,
        conversation_id: int = None,
        prompt_tokens: int = 0,
        completion_tokens: int = 0,
        latency_ms: int = 0,
        endpoint: str = "chat",
        success: bool = True,
        error_message: str = None
    ):
        """Log LLM usage for analytics."""
        if not self.db:
            return

        usage = LLMUsage(
            user_id=user_id,
            model_id=model_id,
            conversation_id=conversation_id,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens,
            latency_ms=latency_ms,
            endpoint=endpoint,
            success=success,
            error_message=error_message
        )
        self.db.add(usage)
        self.db.commit()

    def get_business_context(self) -> Dict[str, Any]:
        """Gather current business data for AI context."""
        if not self.db:
            return {}

        from sqlalchemy import func

        context = {}

        # CRM
        context["contacts_count"] = self.db.query(Contact).count()
        context["companies_count"] = self.db.query(Company).count()
        context["deals_count"] = self.db.query(Deal).count()
        context["pipeline_value"] = float(self.db.query(func.sum(Deal.value)).filter(Deal.stage != "closed_lost").scalar() or 0)

        # Inventory
        context["products_count"] = self.db.query(Product).count()
        low_stock = self.db.query(Product).filter(Product.quantity_in_stock <= Product.reorder_level).count()
        context["low_stock_count"] = low_stock

        # Finance
        context["invoices_count"] = self.db.query(Invoice).count()
        context["total_revenue"] = float(self.db.query(func.sum(Invoice.amount_paid)).filter(Invoice.status == "paid").scalar() or 0)

        # Projects
        context["projects_count"] = self.db.query(Project).count()
        context["tasks_count"] = self.db.query(Task).count()

        return context

    def build_system_prompt(self, template_name: str = None, custom_context: Dict[str, Any] = None) -> str:
        """Build system prompt with business context."""
        if template_name and self.db:
            template = self.db.query(AIPromptTemplate).filter(
                AIPromptTemplate.name == template_name,
                AIPromptTemplate.is_active == True
            ).first()
            if template:
                return template.system_prompt

        base_prompt = """You are an AI business assistant for an Enterprise Resource Planning (ERP) system. You have access to business data including CRM, HR, Inventory, Finance, and Projects.

Guidelines:
- Be concise and data-driven in your responses
- When analyzing data, provide specific numbers and trends
- Suggest actionable next steps when appropriate
- If you don't have access to specific data, say so clearly
- Maintain a professional but friendly tone
- Format responses with markdown when helpful"""

        # Add business context
        context = custom_context or self.get_business_context()
        if context:
            context_str = "\n\nCurrent Business Context:\n"
            for key, value in context.items():
                context_str += f"- {key}: {value}\n"
            base_prompt += context_str

        return base_prompt

    # Tool definitions for AI agent
    TOOLS = [
        {
            "type": "function",
            "function": {
                "name": "get_contacts",
                "description": "Get list of contacts from CRM",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "limit": {"type": "integer", "description": "Maximum number of contacts to return"},
                        "status": {"type": "string", "description": "Filter by status: lead, prospect, customer, churned"}
                    }
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_deals",
                "description": "Get sales deals and pipeline data",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "stage": {"type": "string", "description": "Filter by stage: prospect, qualification, proposal, negotiation, closed_won, closed_lost"},
                        "limit": {"type": "integer", "description": "Maximum number of deals to return"}
                    }
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_products",
                "description": "Get inventory products and stock levels",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "low_stock": {"type": "boolean", "description": "Only show products below reorder level"},
                        "limit": {"type": "integer", "description": "Maximum number of products to return"}
                    }
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_invoices",
                "description": "Get invoices and payment status",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string", "description": "Filter by status: draft, sent, paid, overdue, cancelled"},
                        "limit": {"type": "integer", "description": "Maximum number of invoices to return"}
                    }
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_projects",
                "description": "Get projects and tasks",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string", "description": "Filter by status: planning, active, on_hold, completed, cancelled"},
                        "limit": {"type": "integer", "description": "Maximum number of projects to return"}
                    }
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "create_contact",
                "description": "Create a new contact in CRM",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string", "description": "Contact first name"},
                        "last_name": {"type": "string", "description": "Contact last name"},
                        "email": {"type": "string", "description": "Contact email address"},
                        "company": {"type": "string", "description": "Company name"},
                        "status": {"type": "string", "description": "Contact status: lead, prospect, customer"}
                    },
                    "required": ["first_name", "last_name"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "create_task",
                "description": "Create a new task in a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "integer", "description": "Project ID"},
                        "title": {"type": "string", "description": "Task title"},
                        "description": {"type": "string", "description": "Task description"},
                        "priority": {"type": "string", "description": "Priority: low, medium, high"}
                    },
                    "required": ["project_id", "title"]
                }
            }
        }
    ]

    async def execute_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a tool function and return results."""
        if not self.db:
            return {"error": "Database not available"}

        try:
            if tool_name == "get_contacts":
                limit = arguments.get("limit", 10)
                status = arguments.get("status")
                query = self.db.query(Contact)
                if status:
                    query = query.filter(Contact.status == status)
                contacts = query.limit(limit).all()
                return {
                    "contacts": [
                        {"id": c.id, "name": f"{c.first_name} {c.last_name}", "email": c.email, "status": c.status, "company": c.company.name if c.company else None}
                        for c in contacts
                    ]
                }

            elif tool_name == "get_deals":
                limit = arguments.get("limit", 10)
                stage = arguments.get("stage")
                query = self.db.query(Deal)
                if stage:
                    query = query.filter(Deal.stage == stage)
                deals = query.limit(limit).all()
                return {
                    "deals": [
                        {"id": d.id, "title": d.title, "value": float(d.value or 0), "stage": d.stage, "probability": d.probability}
                        for d in deals
                    ]
                }

            elif tool_name == "get_products":
                limit = arguments.get("limit", 10)
                low_stock = arguments.get("low_stock", False)
                query = self.db.query(Product)
                if low_stock:
                    query = query.filter(Product.quantity_in_stock <= Product.reorder_level)
                products = query.limit(limit).all()
                return {
                    "products": [
                        {"id": p.id, "name": p.name, "sku": p.sku, "stock": p.quantity_in_stock, "reorder_level": p.reorder_level, "price": float(p.unit_price or 0)}
                        for p in products
                    ]
                }

            elif tool_name == "get_invoices":
                limit = arguments.get("limit", 10)
                status = arguments.get("status")
                query = self.db.query(Invoice)
                if status:
                    query = query.filter(Invoice.status == status)
                invoices = query.limit(limit).all()
                return {
                    "invoices": [
                        {"id": i.id, "number": i.invoice_number, "total": float(i.total or 0), "status": i.status, "due_date": str(i.due_date) if i.due_date else None}
                        for i in invoices
                    ]
                }

            elif tool_name == "get_projects":
                limit = arguments.get("limit", 10)
                status = arguments.get("status")
                query = self.db.query(Project)
                if status:
                    query = query.filter(Project.status == status)
                projects = query.limit(limit).all()
                return {
                    "projects": [
                        {"id": p.id, "name": p.name, "status": p.status, "progress": p.progress, "budget": float(p.budget or 0)}
                        for p in projects
                    ]
                }

            elif tool_name == "create_contact":
                contact = Contact(
                    first_name=arguments["first_name"],
                    last_name=arguments["last_name"],
                    email=arguments.get("email"),
                    status=arguments.get("status", "lead")
                )
                self.db.add(contact)
                self.db.commit()
                return {"success": True, "contact_id": contact.id, "message": f"Created contact {contact.first_name} {contact.last_name}"}

            elif tool_name == "create_task":
                task = Task(
                    project_id=arguments["project_id"],
                    title=arguments["title"],
                    description=arguments.get("description"),
                    priority=arguments.get("priority", "medium")
                )
                self.db.add(task)
                self.db.commit()
                return {"success": True, "task_id": task.id, "message": f"Created task: {task.title}"}

            else:
                return {"error": f"Unknown tool: {tool_name}"}

        except Exception as e:
            return {"error": str(e)}

## File: backend/app/services/permissions.py

from functools import wraps
from typing import List, Optional, Dict, Any, Callable
from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.database import get_db
from app.models import User, Role, Permission, FieldPermission, DataPolicy
from app.auth import get_current_user

class PermissionDenied(Exception):
    pass

def has_permission(user: User, resource: str, action: str, db: Session) -> bool:
    """Check if user has a specific permission through any of their roles."""
    if not user or not user.is_active:
        return False

    # Superadmin bypass
    if any(r.name == "superadmin" for r in user.roles):
        return True

    # Check all user roles for the permission
    for role in user.roles:
        for perm in role.permissions:
            if perm.resource == resource and perm.action == action:
                return True

    return False

def require_permission(resource: str, action: str):
    """Dependency factory to require a specific permission."""
    def checker(
        request: Request,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
    ) -> User:
        if not has_permission(current_user, resource, action, db):
            raise HTTPException(
                status_code=403,
                detail=f"Permission denied: {resource}.{action}"
            )
        return current_user
    return checker

def get_user_permissions(user: User, db: Session) -> List[str]:
    """Get all permission names for a user."""
    permissions = set()
    for role in user.roles:
        for perm in role.permissions:
            permissions.add(f"{perm.resource}.{perm.action}")
    return list(permissions)

def get_field_permissions(user: User, resource: str, db: Session) -> Dict[str, str]:
    """Get field-level access map for a user on a resource."""
    field_map = {}
    for role in user.roles:
        for fp in role.field_permissions:
            if fp.resource == resource:
                # Higher access wins: write > read > hidden
                existing = field_map.get(fp.field_name, "hidden")
                levels = {"hidden": 0, "read": 1, "write": 2}
                if levels.get(fp.access_level, 0) > levels.get(existing, 0):
                    field_map[fp.field_name] = fp.access_level
    return field_map

def filter_fields(data: Any, user: User, resource: str, db: Session) -> Any:
    """Filter out hidden fields from data based on user's field permissions."""
    field_map = get_field_permissions(user, resource, db)

    if isinstance(data, dict):
        return {k: v for k, v in data.items() if field_map.get(k) != "hidden"}
    elif isinstance(data, list):
        return [filter_fields(item, user, resource, db) for item in data]
    elif hasattr(data, '__dict__'):
        # SQLAlchemy model
        result = {}
        for col in data.__table__.columns:
            if field_map.get(col.name) != "hidden":
                val = getattr(data, col.name)
                result[col.name] = val
        return result
    return data

def check_data_policy(user: User, resource: str, record: Any, db: Session) -> bool:
    """Check if user can access a specific record based on data policies."""
    for role in user.roles:
        policies = db.query(DataPolicy).filter(
            and_(
                DataPolicy.role_id == role.id,
                DataPolicy.resource == resource,
                DataPolicy.is_active == True
            )
        ).order_by(DataPolicy.priority).all()

        for policy in policies:
            if policy.effect == "deny":
                # Check if record matches deny condition
                if policy.condition and matches_condition(record, policy.condition):
                    return False
            elif policy.effect == "allow":
                if policy.condition and matches_condition(record, policy.condition):
                    return True

    return True  # Default allow if no policies match

def matches_condition(record: Any, condition: Dict[str, Any]) -> bool:
    """Simple condition matcher for data policies."""
    if not condition:
        return True

    record_dict = record
    if hasattr(record, '__dict__'):
        record_dict = {c.name: getattr(record, c.name) for c in record.__table__.columns}

    for key, value in condition.items():
        if key == "_and":
            if not all(matches_condition(record, v) for v in value):
                return False
        elif key == "_or":
            if not any(matches_condition(record, v) for v in value):
                return False
        elif key.startswith("_"):
            continue
        else:
            record_val = record_dict.get(key) if isinstance(record_dict, dict) else getattr(record, key, None)
            if isinstance(value, dict):
                # Operator conditions: {"eq": 5}, {"gt": 10}, etc.
                for op, op_val in value.items():
                    if op == "eq" and record_val != op_val:
                        return False
                    elif op == "ne" and record_val == op_val:
                        return False
                    elif op == "gt" and (record_val is None or record_val <= op_val):
                        return False
                    elif op == "gte" and (record_val is None or record_val < op_val):
                        return False
                    elif op == "lt" and (record_val is None or record_val >= op_val):
                        return False
                    elif op == "lte" and (record_val is None or record_val > op_val):
                        return False
                    elif op == "in" and record_val not in op_val:
                        return False
            else:
                if record_val != value:
                    return False

    return True

def permission_required(resource: str, action: str):
    """Decorator for permission checking on route handlers."""
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Extract current_user and db from kwargs
            current_user = kwargs.get('current_user')
            db = kwargs.get('db')

            if not current_user or not has_permission(current_user, resource, action, db):
                raise HTTPException(status_code=403, detail=f"Permission denied: {resource}.{action}")

            return await func(*args, **kwargs)
        return wrapper
    return decorator

## File: backend/app/services/search_service.py

import os
import re
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func, or_, and_, text
from sqlalchemy.dialects.postgresql import array
import httpx

from app.models import SearchIndex, SearchQuery, SearchSuggestion, Contact, Company, Product, Employee, Project, Invoice, Document
from app.config import settings

class SearchService:
    """Advanced search service with PostgreSQL full-text search and Elasticsearch support."""

    def __init__(self, db: Session, use_elasticsearch: bool = False):
        self.db = db
        self.use_elasticsearch = use_elasticsearch
        self.es_url = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")

    # ==================== INDEXING ====================

    def index_entity(self, entity_type: str, entity_id: int, title: str, content: str, metadata: Dict[str, Any] = None, tags: List[str] = None):
        """Index or update an entity in the search index."""
        # Build searchable text
        searchable = f"{title} {content}"
        if metadata:
            for key, value in metadata.items():
                if isinstance(value, (str, int, float)):
                    searchable += f" {value}"

        # Check if already indexed
        existing = self.db.query(SearchIndex).filter(
            SearchIndex.entity_type == entity_type,
            SearchIndex.entity_id == entity_id
        ).first()

        if existing:
            existing.title = title
            existing.content = content
            existing.searchable_text = searchable
            existing.metadata = metadata or {}
            existing.tags = tags or []
            existing.updated_at = datetime.utcnow()
        else:
            index = SearchIndex(
                entity_type=entity_type,
                entity_id=entity_id,
                title=title,
                content=content,
                searchable_text=searchable,
                metadata=metadata or {},
                tags=tags or []
            )
            self.db.add(index)

        self.db.commit()

    def remove_from_index(self, entity_type: str, entity_id: int):
        """Remove an entity from the search index."""
        self.db.query(SearchIndex).filter(
            SearchIndex.entity_type == entity_type,
            SearchIndex.entity_id == entity_id
        ).delete()
        self.db.commit()

    def index_all_contacts(self):
        """Index all contacts."""
        contacts = self.db.query(Contact).all()
        for c in contacts:
            self.index_entity(
                "contact",
                c.id,
                f"{c.first_name} {c.last_name}",
                f"{c.email or ''} {c.phone or ''} {c.title or ''} {c.notes or ''}",
                metadata={
                    "email": c.email,
                    "phone": c.phone,
                    "status": c.status,
                    "company_id": c.company_id,
                    "assigned_to": c.assigned_to
                },
                tags=[c.status, "contact"]
            )

    def index_all_companies(self):
        """Index all companies."""
        companies = self.db.query(Company).all()
        for c in companies:
            self.index_entity(
                "company",
                c.id,
                c.name,
                f"{c.industry or ''} {c.website or ''} {c.address or ''} {c.phone or ''}",
                metadata={
                    "industry": c.industry,
                    "size": c.size,
                    "website": c.website
                },
                tags=[c.industry, "company"] if c.industry else ["company"]
            )

    def index_all_products(self):
        """Index all products."""
        products = self.db.query(Product).all()
        for p in products:
            self.index_entity(
                "product",
                p.id,
                p.name,
                f"{p.sku} {p.description or ''} {p.category or ''} {p.supplier or ''}",
                metadata={
                    "sku": p.sku,
                    "category": p.category,
                    "price": float(p.unit_price) if p.unit_price else 0,
                    "stock": p.quantity_in_stock,
                    "status": p.status
                },
                tags=[p.category, p.status, "product"] if p.category else [p.status, "product"]
            )

    def index_all_employees(self):
        """Index all employees."""
        employees = self.db.query(Employee).all()
        for e in employees:
            self.index_entity(
                "employee",
                e.id,
                e.employee_code,
                f"{e.job_title or ''} {e.address or ''} {e.emergency_contact or ''}",
                metadata={
                    "code": e.employee_code,
                    "department_id": e.department_id,
                    "status": e.status,
                    "employment_type": e.employment_type
                },
                tags=[e.status, e.employment_type, "employee"]
            )

    def index_all_documents(self):
        """Index all documents."""
        documents = self.db.query(Document).all()
        for d in documents:
            self.index_entity(
                "document",
                d.id,
                d.title,
                f"{d.filename} {d.extracted_text or ''} {d.mime_type or ''}",
                metadata={
                    "filename": d.filename,
                    "mime_type": d.mime_type,
                    "entity_type": d.entity_type,
                    "file_size": d.file_size
                },
                tags=[d.mime_type, d.entity_type, "document"] if d.mime_type else ["document"]
            )

    def reindex_all(self):
        """Reindex all entities."""
        # Clear existing index
        self.db.query(SearchIndex).delete()
        self.db.commit()

        # Index all entities
        self.index_all_contacts()
        self.index_all_companies()
        self.index_all_products()
        self.index_all_employees()
        self.index_all_documents()

        return {
            "contacts": self.db.query(SearchIndex).filter(SearchIndex.entity_type == "contact").count(),
            "companies": self.db.query(SearchIndex).filter(SearchIndex.entity_type == "company").count(),
            "products": self.db.query(SearchIndex).filter(SearchIndex.entity_type == "product").count(),
            "employees": self.db.query(SearchIndex).filter(SearchIndex.entity_type == "employee").count(),
            "documents": self.db.query(SearchIndex).filter(SearchIndex.entity_type == "document").count(),
        }

    # ==================== SEARCH ====================

    def search(
        self,
        query: str,
        entity_types: List[str] = None,
        filters: Dict[str, Any] = None,
        limit: int = 20,
        offset: int = 0
    ) -> Tuple[List[Dict[str, Any]], int]:
        """Full-text search with PostgreSQL."""
        start_time = datetime.utcnow()

        # Build base query
        base_query = self.db.query(SearchIndex)

        # Apply text search
        if query and query.strip():
            # Normalize query for PostgreSQL tsvector search
            search_terms = query.strip().split()
            tsquery = " & ".join([f"{term}:*" for term in search_terms])

            base_query = base_query.filter(
                text("to_tsvector('english', searchable_text) @@ to_tsquery('english', :query)")
                .bindparams(query=tsquery)
            )

        # Filter by entity types
        if entity_types:
            base_query = base_query.filter(SearchIndex.entity_type.in_(entity_types))

        # Apply metadata filters
        if filters:
            for key, value in filters.items():
                if key == "tags" and isinstance(value, list):
                    base_query = base_query.filter(
                        SearchIndex.tags.op("&&")(array(value))
                    )
                elif key.startswith("metadata."):
                    meta_key = key.replace("metadata.", "")
                    base_query = base_query.filter(
                        SearchIndex.metadata[meta_key].astext == str(value)
                    )

        # Get total count
        total = base_query.count()

        # Get results with ordering
        results = base_query.order_by(
            SearchIndex.updated_at.desc()
        ).offset(offset).limit(limit).all()

        # Format results
        formatted = []
        for r in results:
            formatted.append({
                "id": r.id,
                "entity_type": r.entity_type,
                "entity_id": r.entity_id,
                "title": r.title,
                "content_preview": r.content[:200] if r.content else "",
                "metadata": r.metadata or {},
                "tags": r.tags or [],
                "updated_at": r.updated_at.isoformat() if r.updated_at else None
            })

        execution_time = int((datetime.utcnow() - start_time).total_seconds() * 1000)

        return formatted, total, execution_time

    def get_facets(self, query: str = None, entity_types: List[str] = None) -> Dict[str, Any]:
        """Get facet counts for search results."""
        base_query = self.db.query(SearchIndex)

        if query and query.strip():
            search_terms = query.strip().split()
            tsquery = " & ".join([f"{term}:*" for term in search_terms])
            base_query = base_query.filter(
                text("to_tsvector('english', searchable_text) @@ to_tsquery('english', :query)")
                .bindparams(query=tsquery)
            )

        if entity_types:
            base_query = base_query.filter(SearchIndex.entity_type.in_(entity_types))

        # Entity type facets
        type_counts = self.db.query(
            SearchIndex.entity_type,
            func.count(SearchIndex.id).label("count")
        ).filter(
            SearchIndex.id.in_(base_query.with_entities(SearchIndex.id))
        ).group_by(SearchIndex.entity_type).all()

        # Tag facets
        tag_counts = {}
        all_tags = self.db.query(SearchIndex.tags).filter(
            SearchIndex.id.in_(base_query.with_entities(SearchIndex.id))
        ).all()
        for tags_row in all_tags:
            if tags_row[0]:
                for tag in tags_row[0]:
                    tag_counts[tag] = tag_counts.get(tag, 0) + 1

        return {
            "entity_types": [
                {"value": t.entity_type, "count": t.count}
                for t in type_counts
            ],
            "tags": [
                {"value": tag, "count": count}
                for tag, count in sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:20]
            ]
        }

    # ==================== SUGGESTIONS ====================

    def get_suggestions(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get autocomplete suggestions."""
        if not query or len(query) < 2:
            return []

        # Search in suggestions table
        suggestions = self.db.query(SearchSuggestion).filter(
            SearchSuggestion.query_text.ilike(f"%{query}%")
        ).order_by(
            SearchSuggestion.frequency.desc()
        ).limit(limit).all()

        # Also search in indexed titles
        title_matches = self.db.query(SearchIndex).filter(
            SearchIndex.title.ilike(f"%{query}%")
        ).distinct(SearchIndex.title).limit(5).all()

        result = []
        seen = set()

        for s in suggestions:
            if s.query_text not in seen:
                seen.add(s.query_text)
                result.append({
                    "text": s.query_text,
                    "type": s.suggestion_type,
                    "entity_type": s.entity_type,
                    "frequency": s.frequency
                })

        for t in title_matches:
            if t.title and t.title not in seen:
                seen.add(t.title)
                result.append({
                    "text": t.title,
                    "type": "title",
                    "entity_type": t.entity_type,
                    "frequency": 0
                })

        return result[:limit]

    def record_suggestion(self, query: str, entity_type: str = None, entity_id: int = None):
        """Record a search query for suggestion building."""
        existing = self.db.query(SearchSuggestion).filter(
            SearchSuggestion.query_text == query.lower().strip(),
            SearchSuggestion.entity_type == entity_type
        ).first()

        if existing:
            existing.frequency += 1
            existing.last_used = datetime.utcnow()
        else:
            suggestion = SearchSuggestion(
                query_text=query.lower().strip(),
                entity_type=entity_type,
                entity_id=entity_id,
                frequency=1
            )
            self.db.add(suggestion)

        self.db.commit()

    # ==================== ANALYTICS ====================

    def log_query(self, user_id: int, query: str, filters: Dict[str, Any] = None, results_count: int = 0, execution_time_ms: int = 0, clicked_results: List[int] = None):
        """Log a search query for analytics."""
        sq = SearchQuery(
            user_id=user_id,
            query=query,
            filters=filters or {},
            results_count=results_count,
            execution_time_ms=execution_time_ms,
            clicked_results=clicked_results or []
        )
        self.db.add(sq)
        self.db.commit()

    def get_search_analytics(self, days: int = 30) -> Dict[str, Any]:
        """Get search analytics."""
        from datetime import datetime, timedelta

        start_date = datetime.utcnow() - timedelta(days=days)

        # Total queries
        total_queries = self.db.query(SearchQuery).filter(
            SearchQuery.created_at >= start_date
        ).count()

        # Top queries
        top_queries = self.db.query(
            SearchQuery.query,
            func.count(SearchQuery.id).label("count")
        ).filter(
            SearchQuery.created_at >= start_date
        ).group_by(SearchQuery.query).order_by(func.count(SearchQuery.id).desc()).limit(20).all()

        # Queries with no results
        no_results = self.db.query(SearchQuery).filter(
            SearchQuery.created_at >= start_date,
            SearchQuery.results_count == 0
        ).count()

        # Average execution time
        avg_time = self.db.query(func.avg(SearchQuery.execution_time_ms)).filter(
            SearchQuery.created_at >= start_date
        ).scalar() or 0

        # Daily query volume
        daily = self.db.query(
            func.date(SearchQuery.created_at).label("date"),
            func.count(SearchQuery.id).label("count")
        ).filter(
            SearchQuery.created_at >= start_date
        ).group_by(func.date(SearchQuery.created_at)).order_by("date").all()

        # Popular filters
        filter_usage = {}
        queries_with_filters = self.db.query(SearchQuery).filter(
            SearchQuery.created_at >= start_date,
            SearchQuery.filters != None
        ).all()
        for q in queries_with_filters:
            if q.filters:
                for key in q.filters.keys():
                    filter_usage[key] = filter_usage.get(key, 0) + 1

        return {
            "period_days": days,
            "total_queries": total_queries,
            "no_results_queries": no_results,
            "no_results_rate": (no_results / total_queries * 100) if total_queries > 0 else 0,
            "avg_execution_time_ms": round(float(avg_time), 2),
            "top_queries": [
                {"query": q.query, "count": q.count}
                for q in top_queries
            ],
            "daily_volume": [
                {"date": str(d.date), "queries": d.count}
                for d in daily
            ],
            "popular_filters": [
                {"filter": k, "count": v}
                for k, v in sorted(filter_usage.items(), key=lambda x: x[1], reverse=True)
            ]
        }

## File: backend/alembic/versions/002_add_rbac_permissions.py

"""Add RBAC permissions system

Revision ID: 002
Revises: 001
Create Date: 2024-06-15 10:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '002'
down_revision: Union[str, None] = '001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Roles table
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('display_name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('is_system', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )

    # Permissions table
    op.create_table(
        'permissions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('resource', sa.String(length=100), nullable=False),
        sa.Column('action', sa.String(length=50), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )

    # Role-Permission junction
    op.create_table(
        'role_permissions',
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.Column('permission_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('role_id', 'permission_id')
    )

    # User-Role junction (many-to-many)
    op.create_table(
        'user_roles',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('user_id', 'role_id')
    )

    # Field-level permissions
    op.create_table(
        'field_permissions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.Column('resource', sa.String(length=100), nullable=False),
        sa.Column('field_name', sa.String(length=100), nullable=False),
        sa.Column('access_level', sa.String(length=20), nullable=False, server_default='read'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('role_id', 'resource', 'field_name', name='uq_field_permission')
    )

    # Data policies (row-level access)
    op.create_table(
        'data_policies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('resource', sa.String(length=100), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.Column('condition', postgresql.JSONB(), nullable=True),
        sa.Column('effect', sa.String(length=20), nullable=False, server_default='allow'),
        sa.Column('priority', sa.Integer(), nullable=False, server_default='100'),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # Insert default roles
    op.execute("""
        INSERT INTO roles (name, display_name, description, is_system) VALUES
        ('superadmin', 'Super Administrator', 'Full system access', true),
        ('admin', 'Administrator', 'Admin access to all modules', true),
        ('manager', 'Manager', 'Can manage team data and view reports', true),
        ('user', 'Standard User', 'Can create and edit own records', true),
        ('viewer', 'Viewer', 'Read-only access to assigned data', true)
    """)

    # Insert default permissions
    op.execute("""
        INSERT INTO permissions (name, resource, action, description) VALUES
        ('users.read', 'users', 'read', 'View user profiles'),
        ('users.create', 'users', 'create', 'Create new users'),
        ('users.update', 'users', 'update', 'Edit user profiles'),
        ('users.delete', 'users', 'delete', 'Delete users'),
        ('contacts.read', 'contacts', 'read', 'View contacts'),
        ('contacts.create', 'contacts', 'create', 'Create contacts'),
        ('contacts.update', 'contacts', 'update', 'Edit contacts'),
        ('contacts.delete', 'contacts', 'delete', 'Delete contacts'),
        ('companies.read', 'companies', 'read', 'View companies'),
        ('companies.create', 'companies', 'create', 'Create companies'),
        ('companies.update', 'companies', 'update', 'Edit companies'),
        ('companies.delete', 'companies', 'delete', 'Delete companies'),
        ('deals.read', 'deals', 'read', 'View deals'),
        ('deals.create', 'deals', 'create', 'Create deals'),
        ('deals.update', 'deals', 'update', 'Edit deals'),
        ('deals.delete', 'deals', 'delete', 'Delete deals'),
        ('products.read', 'products', 'read', 'View products'),
        ('products.create', 'products', 'create', 'Create products'),
        ('products.update', 'products', 'update', 'Edit products'),
        ('products.delete', 'products', 'delete', 'Delete products'),
        ('invoices.read', 'invoices', 'read', 'View invoices'),
        ('invoices.create', 'invoices', 'create', 'Create invoices'),
        ('invoices.update', 'invoices', 'update', 'Edit invoices'),
        ('invoices.delete', 'invoices', 'delete', 'Delete invoices'),
        ('employees.read', 'employees', 'read', 'View employees'),
        ('employees.create', 'employees', 'create', 'Create employees'),
        ('employees.update', 'employees', 'update', 'Edit employees'),
        ('employees.delete', 'employees', 'delete', 'Delete employees'),
        ('projects.read', 'projects', 'read', 'View projects'),
        ('projects.create', 'projects', 'create', 'Create projects'),
        ('projects.update', 'projects', 'update', 'Edit projects'),
        ('projects.delete', 'projects', 'delete', 'Delete projects'),
        ('reports.read', 'reports', 'read', 'View reports'),
        ('reports.create', 'reports', 'create', 'Create reports'),
        ('settings.read', 'settings', 'read', 'View settings'),
        ('settings.update', 'settings', 'update', 'Edit settings'),
        ('workflows.read', 'workflows', 'read', 'View workflows'),
        ('workflows.create', 'workflows', 'create', 'Create workflows'),
        ('workflows.update', 'workflows', 'update', 'Edit workflows'),
        ('workflows.delete', 'workflows', 'delete', 'Delete workflows'),
        ('admin.access', 'admin', 'access', 'Access admin panel'),
        ('bulk.import', 'bulk', 'import', 'Import data'),
        ('bulk.export', 'bulk', 'export', 'Export data'),
        ('migrations.manage', 'migrations', 'manage', 'Manage database migrations')
    """)

    # Assign all permissions to superadmin
    op.execute("""
        INSERT INTO role_permissions (role_id, permission_id)
        SELECT r.id, p.id FROM roles r, permissions p WHERE r.name = 'superadmin'
    """)

    # Assign permissions to admin (all except migrations.manage)
    op.execute("""
        INSERT INTO role_permissions (role_id, permission_id)
        SELECT r.id, p.id FROM roles r, permissions p
        WHERE r.name = 'admin' AND p.name != 'migrations.manage'
    """)

    # Assign basic permissions to manager
    op.execute("""
        INSERT INTO role_permissions (role_id, permission_id)
        SELECT r.id, p.id FROM roles r, permissions p
        WHERE r.name = 'manager' AND p.action IN ('read', 'create', 'update') AND p.resource NOT IN ('users', 'settings', 'migrations')
    """)

    # Assign read-only to viewer
    op.execute("""
        INSERT INTO role_permissions (role_id, permission_id)
        SELECT r.id, p.id FROM roles r, permissions p
        WHERE r.name = 'viewer' AND p.action = 'read'
    """)

    # Assign basic permissions to user
    op.execute("""
        INSERT INTO role_permissions (role_id, permission_id)
        SELECT r.id, p.id FROM roles r, permissions p
        WHERE r.name = 'user' AND p.action IN ('read', 'create', 'update') AND p.resource NOT IN ('users', 'settings', 'migrations', 'admin')
    """)

    # Insert default field permissions (hide salary from non-managers)
    op.execute("""
        INSERT INTO field_permissions (role_id, resource, field_name, access_level)
        SELECT r.id, 'employees', 'salary', 'hidden'
        FROM roles r WHERE r.name IN ('user', 'viewer')
    """)

    op.execute("""
        INSERT INTO field_permissions (role_id, resource, field_name, access_level)
        SELECT r.id, 'employees', 'cost_price', 'hidden'
        FROM roles r WHERE r.name IN ('user', 'viewer')
    """)

    op.execute("""
        INSERT INTO field_permissions (role_id, resource, field_name, access_level)
        SELECT r.id, 'contacts', 'lifetime_value', 'hidden'
        FROM roles r WHERE r.name = 'viewer'
    """)

def downgrade() -> None:
    op.drop_table('data_policies')
    op.drop_table('field_permissions')
    op.drop_table('user_roles')
    op.drop_table('role_permissions')
    op.drop_table('permissions')
    op.drop_table('roles')

## File: backend/alembic/versions/003_add_llm_integration.py

"""Add LLM integration tables

Revision ID: 003
Revises: 002
Create Date: 2024-06-15 11:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '003'
down_revision: Union[str, None] = '002'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # LLM Models table
    op.create_table(
        'llm_models',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('provider', sa.String(length=50), nullable=False, server_default='ollama'),
        sa.Column('model_id', sa.String(length=100), nullable=False),
        sa.Column('display_name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('parameters', postgresql.JSONB(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('is_default', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('supports_streaming', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('supports_tools', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('context_window', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('model_id')
    )

    # AI Conversations table
    op.create_table(
        'ai_conversations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=True),
        sa.Column('model_id', sa.String(length=100), nullable=False),
        sa.Column('system_prompt', sa.Text(), nullable=True),
        sa.Column('context', postgresql.JSONB(), nullable=True),
        sa.Column('is_archived', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_ai_conversations_user_id', 'ai_conversations', ['user_id'], unique=False)

    # AI Messages table
    op.create_table(
        'ai_messages',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('conversation_id', sa.Integer(), nullable=False),
        sa.Column('role', sa.String(length=50), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('model_id', sa.String(length=100), nullable=True),
        sa.Column('tokens_used', sa.Integer(), nullable=True),
        sa.Column('latency_ms', sa.Integer(), nullable=True),
        sa.Column('tool_calls', postgresql.JSONB(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['conversation_id'], ['ai_conversations.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_ai_messages_conversation_id', 'ai_messages', ['conversation_id'], unique=False)

    # LLM Usage Analytics table
    op.create_table(
        'llm_usage',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('model_id', sa.String(length=100), nullable=False),
        sa.Column('conversation_id', sa.Integer(), nullable=True),
        sa.Column('prompt_tokens', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('completion_tokens', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('total_tokens', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('latency_ms', sa.Integer(), nullable=True),
        sa.Column('endpoint', sa.String(length=100), nullable=True),
        sa.Column('success', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('error_message', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_llm_usage_created_at', 'llm_usage', ['created_at'], unique=False)

    # AI Prompt Templates table
    op.create_table(
        'ai_prompt_templates',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('display_name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('system_prompt', sa.Text(), nullable=False),
        sa.Column('user_prompt_template', sa.Text(), nullable=True),
        sa.Column('variables', postgresql.JSONB(), nullable=True),
        sa.Column('model_id', sa.String(length=100), nullable=True),
        sa.Column('category', sa.String(length=50), nullable=False, server_default='general'),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_by', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['created_by'], ['users.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )

    # Insert default LLM models
    op.execute("""
        INSERT INTO llm_models (name, provider, model_id, display_name, description, parameters, is_active, is_default, supports_streaming, supports_tools, context_window) VALUES
        ('qwen3.6', 'ollama', 'qwen3.6', 'Qwen 3.6', 'Alibaba Qwen 3.6 - General purpose business AI', '{"temperature": 0.7, "top_p": 0.9}', true, true, true, true, 32768),
        ('llama3.1', 'ollama', 'llama3.1', 'Llama 3.1', 'Meta Llama 3.1 - Open source LLM', '{"temperature": 0.7, "top_p": 0.9}', true, false, true, true, 128000),
        ('mistral', 'ollama', 'mistral', 'Mistral', 'Mistral AI - Fast and efficient', '{"temperature": 0.7, "top_p": 0.9}', true, false, true, false, 32768),
        ('codellama', 'ollama', 'codellama', 'Code Llama', 'Meta Code Llama - Code generation specialist', '{"temperature": 0.2, "top_p": 0.95}', true, false, true, false, 16384)
    """)

    # Insert default prompt templates
    op.execute("""
        INSERT INTO ai_prompt_templates (name, display_name, description, system_prompt, category, is_active) VALUES
        ('business_analyst', 'Business Analyst', 'Analyze business data and provide insights', 'You are a senior business analyst. Analyze the provided data and give actionable insights with specific numbers and trends. Be concise and data-driven.', 'analytics', true),
        ('email_writer', 'Email Writer', 'Draft professional business emails', 'You are a professional business communications specialist. Draft clear, concise, and professional emails. Maintain a friendly but professional tone.', 'communication', true),
        ('proposal_generator', 'Proposal Generator', 'Generate business proposals and quotes', 'You are a business development expert. Create compelling proposals that highlight value, include pricing structure, and address client needs. Use professional formatting.', 'sales', true),
        ('report_summarizer', 'Report Summarizer', 'Summarize long reports and documents', 'You are an executive assistant. Summarize reports into key points, action items, and recommendations. Use bullet points and keep it to one page.', 'productivity', true),
        ('data_extractor', 'Data Extractor', 'Extract structured data from unstructured text', 'You are a data extraction specialist. Extract structured information from text and return it in a clear format. Identify key entities, dates, amounts, and relationships.', 'data', true)
    """)

def downgrade() -> None:
    op.drop_table('ai_prompt_templates')
    op.drop_index('ix_llm_usage_created_at', table_name='llm_usage')
    op.drop_table('llm_usage')
    op.drop_index('ix_ai_messages_conversation_id', table_name='ai_messages')
    op.drop_table('ai_messages')
    op.drop_index('ix_ai_conversations_user_id', table_name='ai_conversations')
    op.drop_table('ai_conversations')
    op.drop_table('llm_models')

## File: backend/alembic/versions/004_add_elasticsearch_search.py

"""Add Elasticsearch search integration tables

Revision ID: 004
Revises: 003
Create Date: 2024-06-15 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '004'
down_revision: Union[str, None] = '003'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Search indexes table
    op.create_table(
        'search_indexes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('entity_type', sa.String(length=100), nullable=False),
        sa.Column('entity_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=500), nullable=True),
        sa.Column('content', sa.Text(), nullable=True),
        sa.Column('searchable_text', sa.Text(), nullable=False),
        sa.Column('metadata', postgresql.JSONB(), nullable=True),
        sa.Column('tags', postgresql.JSONB(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('entity_type', 'entity_id', name='uq_search_index_entity')
    )
    op.create_index('ix_search_indexes_entity_type', 'search_indexes', ['entity_type'], unique=False)
    op.create_index('ix_search_indexes_searchable_text', 'search_indexes', ['searchable_text'], unique=False, postgresql_using='gin')

    # Search queries analytics table
    op.create_table(
        'search_queries',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('query', sa.Text(), nullable=False),
        sa.Column('filters', postgresql.JSONB(), nullable=True),
        sa.Column('results_count', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('execution_time_ms', sa.Integer(), nullable=True),
        sa.Column('clicked_results', postgresql.JSONB(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_search_queries_created_at', 'search_queries', ['created_at'], unique=False)
    op.create_index('ix_search_queries_query', 'search_queries', ['query'], unique=False)

    # Search suggestions table
    op.create_table(
        'search_suggestions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('query_text', sa.String(length=255), nullable=False),
        sa.Column('suggestion_type', sa.String(length=50), nullable=False, server_default='autocomplete'),
        sa.Column('entity_type', sa.String(length=100), nullable=True),
        sa.Column('entity_id', sa.Integer(), nullable=True),
        sa.Column('frequency', sa.Integer(), nullable=False, server_default='1'),
        sa.Column('last_used', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('query_text', 'suggestion_type', 'entity_type', name='uq_search_suggestion')
    )

def downgrade() -> None:
    op.drop_table('search_suggestions')
    op.drop_index('ix_search_queries_query', table_name='search_queries')
    op.drop_index('ix_search_queries_created_at', table_name='search_queries')
    op.drop_table('search_queries')
    op.drop_index('ix_search_indexes_searchable_text', table_name='search_indexes')
    op.drop_index('ix_search_indexes_entity_type', table_name='search_indexes')
    op.drop_table('search_indexes')

## File: frontend-react/tailwind.config.js

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eef2ff',
          100: '#e0e7ff',
          200: '#c7d2fe',
          300: '#a5b4fc',
          400: '#818cf8',
          500: '#6366f1',
          600: '#4f46e5',
          700: '#4338ca',
          800: '#3730a3',
          900: '#312e81',
        }
      }
    },
  },
  plugins: [],
}

## File: frontend-react/vite.config.js

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      manifest: false,
      workbox: {
        globPatterns: ['**/*.{js,css,html,ico,png,svg}'],
        runtimeCaching: [
          {
            urlPattern: /^https:\/\/localhost:8000\/api\/.*/i,
            handler: 'NetworkFirst',
            options: {
              cacheName: 'api-cache',
              expiration: {
                maxEntries: 100,
                maxAgeSeconds: 60 * 60 * 24
              }
            }
          }
        ]
      }
    })
  ],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  },
  build: {
    outDir: 'dist',
    sourcemap: true
  }
})

## File: frontend-react/index.html

## File: frontend-react/nginx.conf

server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

## File: frontend-react/postcss.config.js

export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}

## File: frontend-react/package.json

{
  "name": "ai-erp-frontend",
  "private": true,
  "version": "1.8.0",
  "type": "module",
  "scripts": {
    "dev": "vite --host",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.21.0",
    "axios": "^1.6.2",
    "lucide-react": "^0.294.0",
    "react-dropzone": "^14.2.3",
    "recharts": "^2.10.3",
    "date-fns": "^3.0.6",
    "clsx": "^2.0.0",
    "tailwind-merge": "^2.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32",
    "tailwindcss": "^3.4.0",
    "vite": "^5.0.8",
    "vite-plugin-pwa": "^0.17.4"
  }
}

## File: frontend-react/Dockerfile

FROM node:20-alpine AS builder

WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

## File: frontend-react/src/index.css

@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --color-bg: #f9fafb;
    --color-card: #ffffff;
    --color-text: #111827;
    --color-text-secondary: #6b7280;
    --color-border: #e5e7eb;
    --color-primary: #4f46e5;
    --color-primary-light: #eef2ff;
    --color-primary-dark: #4338ca;
    --color-success: #10b981;
    --color-warning: #f59e0b;
    --color-danger: #ef4444;
    --color-info: #3b82f6;
    --color-muted: #f3f4f6;
  }

  .dark {
    --color-bg: #0f172a;
    --color-card: #1e293b;
    --color-text: #f1f5f9;
    --color-text-secondary: #94a3b8;
    --color-border: #334155;
    --color-primary: #818cf8;
    --color-primary-light: #1e1b4b;
    --color-primary-dark: #a5b4fc;
    --color-success: #34d399;
    --color-warning: #fbbf24;
    --color-danger: #f87171;
    --color-info: #60a5fa;
    --color-muted: #1e293b;
  }

  body {
    @apply antialiased;
    background-color: var(--color-bg);
    color: var(--color-text);
  }
}

@layer components {
  .card {
    @apply bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-700 shadow-sm;
    background-color: var(--color-card);
    border-color: var(--color-border);
  }

  .btn-primary {
    @apply px-4 py-2 rounded-lg font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed;
    background-color: var(--color-primary);
    color: white;
  }
  .btn-primary:hover:not(:disabled) {
    background-color: var(--color-primary-dark);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
  }

  .btn-secondary {
    @apply px-4 py-2 bg-white dark:bg-gray-800 border rounded-lg font-medium transition-all duration-200;
    border-color: var(--color-border);
    color: var(--color-text-secondary);
  }
  .btn-secondary:hover {
    background-color: var(--color-muted);
  }

  .input-field {
    @apply w-full px-4 py-2 border rounded-lg outline-none transition-all duration-200;
    border-color: var(--color-border);
    background-color: var(--color-card);
    color: var(--color-text);
  }
  .input-field:focus {
    @apply ring-2 ring-indigo-500 border-indigo-500;
  }

  .badge {
    @apply inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium;
  }

  .badge-green {
    @apply bg-green-100 dark:bg-green-900/30 text-green-800 dark:text-green-300;
  }
  .badge-blue {
    @apply bg-blue-100 dark:bg-blue-900/30 text-blue-800 dark:text-blue-300;
  }
  .badge-amber {
    @apply bg-amber-100 dark:bg-amber-900/30 text-amber-800 dark:text-amber-300;
  }
  .badge-red {
    @apply bg-red-100 dark:bg-red-900/30 text-red-800 dark:text-red-300;
  }
  .badge-gray {
    @apply bg-gray-100 dark:bg-gray-800 text-gray-800 dark:text-gray-300;
  }
  .badge-indigo {
    @apply bg-indigo-100 dark:bg-indigo-900/30 text-indigo-800 dark:text-indigo-300;
  }

  .animate-in {
    animation: animateIn 0.2s ease-out;
  }
  .slide-in-from-right-full {
    animation: slideInRight 0.3s ease-out;
  }
  .zoom-in-95 {
    animation: zoomIn 0.2s ease-out;
  }
  .fade-in {
    animation: fadeIn 0.2s ease-out;
  }

  @keyframes animateIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }
  @keyframes slideInRight {
    from { opacity: 0; transform: translateX(100%); }
    to { opacity: 1; transform: translateX(0); }
  }
  @keyframes zoomIn {
    from { opacity: 0; transform: scale(0.95); }
    to { opacity: 1; transform: scale(1); }
  }
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .line-clamp-3 {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
}

@layer utilities {
  .text-balance {
    text-wrap: balance;
  }
}

## File: frontend-react/src/main.jsx

import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App.jsx'
import { ThemeProvider } from './contexts/ThemeContext.jsx'
import { ToastProvider } from './contexts/ToastContext.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <ThemeProvider>
        <ToastProvider>
          <App />
        </ToastProvider>
      </ThemeProvider>
    </BrowserRouter>
  </React.StrictMode>,
)

// Register service worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then((registration) => {
        console.log('SW registered:', registration.scope);
      })
      .catch((error) => {
        console.log('SW registration failed:', error);
      });
  });
}

## File: frontend-react/src/App.jsx

import React, { useState, useEffect } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import CRM from './pages/CRM';
import HR from './pages/HR';
import Inventory from './pages/Inventory';
import Finance from './pages/Finance';
import Projects from './pages/Projects';
import Reports from './pages/Reports';
import Analytics from './pages/Analytics';
import AIChat from './pages/AIChat';
import Documents from './pages/Documents';
import Workflows from './pages/Workflows';
import Integrations from './pages/Integrations';
import Settings from './pages/Settings';
import BulkImportExport from './pages/BulkImportExport';
import MigrationManager from './pages/MigrationManager';
import Permissions from './pages/Permissions';
import LLMManager from './pages/LLMManager';
import Search from './pages/Search';

function App() {
  const [token, setToken] = useState(localStorage.getItem('token'));

  useEffect(() => {
    const handleStorage = () => {
      setToken(localStorage.getItem('token'));
    };
    window.addEventListener('storage', handleStorage);
    return () => window.removeEventListener('storage', handleStorage);
  }, []);

  if (!token) {
    return <Login onLogin={(t) => { localStorage.setItem('token', t); setToken(t); }} />;
  }

  return (
    <Layout onLogout={() => { localStorage.removeItem('token'); setToken(null); }}>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/crm" element={<CRM />} />
        <Route path="/hr" element={<HR />} />
        <Route path="/inventory" element={<Inventory />} />
        <Route path="/finance" element={<Finance />} />
        <Route path="/projects" element={<Projects />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/ai-chat" element={<AIChat />} />
        <Route path="/documents" element={<Documents />} />
        <Route path="/workflows" element={<Workflows />} />
        <Route path="/integrations" element={<Integrations />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/bulk-import" element={<BulkImportExport />} />
        <Route path="/migrations" element={<MigrationManager />} />
        <Route path="/permissions" element={<Permissions />} />
        <Route path="/llm-manager" element={<LLMManager />} />
        <Route path="/search" element={<Search />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Layout>
  );
}

export default App;

## File: frontend-react/src/pages/Finance.jsx

import React, { useState, useEffect } from 'react';
import { Receipt, DollarSign, Plus, CheckCircle, Clock, AlertCircle } from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function Finance() {
  const [invoices, setInvoices] = useState([]);
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => {
    axios.get(`${API_URL}/api/v1/finance/invoices`, axiosConfig).then(r => setInvoices(r.data));
  }, []);

  const statusColors = {
    draft: 'bg-gray-100 text-gray-800',
    sent: 'bg-blue-100 text-blue-800',
    paid: 'bg-green-100 text-green-800',
    overdue: 'bg-red-100 text-red-800',
    cancelled: 'bg-gray-100 text-gray-500',
  };

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-3xl font-bold text-gray-900">Finance</h1>
        <button className="btn-primary flex items-center gap-2"><Plus className="w-4 h-4" /> New Invoice</button>
      </div>
      <div className="card overflow-hidden">
        <table className="min-w-full text-sm">
          <thead className="bg-gray-50"><tr>
            <th className="px-4 py-3 text-left font-medium">Invoice #</th>
            <th className="px-4 py-3 text-left font-medium">Date</th>
            <th className="px-4 py-3 text-left font-medium">Due</th>
            <th className="px-4 py-3 text-left font-medium">Total</th>
            <th className="px-4 py-3 text-left font-medium">Paid</th>
            <th className="px-4 py-3 text-left font-medium">Status</th>
          </tr></thead>
          <tbody className="divide-y">
            {invoices.map(inv => (
              <tr key={inv.id} className="hover:bg-gray-50">
                <td className="px-4 py-3 font-mono font-medium text-indigo-600">{inv.invoice_number}</td>
                <td className="px-4 py-3 text-gray-600">{inv.issue_date}</td>
                <td className="px-4 py-3 text-gray-600">{inv.due_date}</td>
                <td className="px-4 py-3 font-medium">${Number(inv.total).toFixed(2)}</td>
                <td className="px-4 py-3 text-gray-600">${Number(inv.amount_paid || 0).toFixed(2)}</td>
                <td className="px-4 py-3"><span className={`px-2 py-1 rounded-full text-xs font-medium ${statusColors[inv.status] || 'bg-gray-100'}`}>{inv.status}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

## File: frontend-react/src/pages/HR.jsx

import React, { useState, useEffect } from 'react';
import { Users, Building, Briefcase, DollarSign, Plus } from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function HR() {
  const [employees, setEmployees] = useState([]);
  const [departments, setDepartments] = useState([]);
  const [activeTab, setActiveTab] = useState('employees');
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => {
    axios.get(`${API_URL}/api/v1/hr/employees`, axiosConfig).then(r => setEmployees(r.data));
    axios.get(`${API_URL}/api/v1/hr/departments`, axiosConfig).then(r => setDepartments(r.data));
  }, []);

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Human Resources</h1>
      <div className="flex gap-1 mb-6 bg-gray-100 p-1 rounded-lg w-fit">
        {[{id:'employees',label:'Employees',icon:Users},{id:'departments',label:'Departments',icon:Building}].map(t => (
          <button key={t.id} onClick={()=>setActiveTab(t.id)} className={`flex items-center gap-2 px-4 py-2 rounded-md font-medium transition-all ${activeTab===t.id?'bg-white text-indigo-600 shadow-sm':'text-gray-600'}`}><t.icon className="w-4 h-4"/>{t.label}</button>
        ))}
      </div>
      {activeTab === 'employees' && (
        <div className="card overflow-hidden">
          <table className="min-w-full text-sm">
            <thead className="bg-gray-50"><tr>
              <th className="px-4 py-3 text-left font-medium">Code</th>
              <th className="px-4 py-3 text-left font-medium">Name</th>
              <th className="px-4 py-3 text-left font-medium">Title</th>
              <th className="px-4 py-3 text-left font-medium">Department</th>
              <th className="px-4 py-3 text-left font-medium">Status</th>
              <th className="px-4 py-3 text-left font-medium">Salary</th>
            </tr></thead>
            <tbody className="divide-y">
              {employees.map(e => (
                <tr key={e.id} className="hover:bg-gray-50">
                  <td className="px-4 py-3 font-mono text-gray-600">{e.employee_code}</td>
                  <td className="px-4 py-3 font-medium">{e.full_name || e.employee_code}</td>
                  <td className="px-4 py-3 text-gray-600">{e.job_title}</td>
                  <td className="px-4 py-3 text-gray-600">{e.department?.name || '—'}</td>
                  <td className="px-4 py-3"><span className={`px-2 py-1 rounded-full text-xs ${e.status==='active'?'bg-green-100 text-green-800':'bg-gray-100 text-gray-800'}`}>{e.status}</span></td>
                  <td className="px-4 py-3 text-gray-900">{e.salary ? `$${Number(e.salary).toLocaleString()}` : '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      {activeTab === 'departments' && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {departments.map(d => (
            <div key={d.id} className="card p-5">
              <h3 className="font-semibold text-gray-900">{d.name}</h3>
              <p className="text-sm text-gray-500 mt-1">{d.description}</p>
              {d.budget && <p className="text-sm font-medium text-gray-900 mt-2">Budget: ${Number(d.budget).toLocaleString()}</p>}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

## File: frontend-react/src/pages/Login.jsx

import React, { useState } from 'react';
import { LogIn, UserPlus, Loader } from 'lucide-react';
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function Login({ onLogin }) {
  const [isRegister, setIsRegister] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      if (isRegister) {
        await axios.post(`${API_URL}/api/v1/auth/register`, {
          email, password, full_name: fullName
        });
        // Auto login after register
        const res = await axios.post(`${API_URL}/api/v1/auth/login`, {
          username: email, password
        }, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } });
        onLogin(res.data.access_token);
      } else {
        const res = await axios.post(`${API_URL}/api/v1/auth/login`, {
          username: email, password
        }, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } });
        onLogin(res.data.access_token);
      }
    } catch (err) {
      setError(err.response?.data?.detail || 'Authentication failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-50 to-blue-100 p-4">
      <div className="w-full max-w-md">
        <div className="bg-white rounded-2xl shadow-xl p-8">
          <div className="text-center mb-8">
            <div className="w-16 h-16 bg-indigo-600 rounded-xl flex items-center justify-center mx-auto mb-4">
              <span className="text-white font-bold text-2xl">AI</span>
            </div>
            <h1 className="text-2xl font-bold text-gray-900">AI-ERP System</h1>
            <p className="text-gray-500 mt-1">Enterprise Resource Planning</p>
          </div>

          {error && (
            <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            {isRegister && (
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
                <input
                  type="text"
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                  className="input-field"
                  placeholder="John Doe"
                  required
                />
              </div>
            )}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="input-field"
                placeholder="you@company.com"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Password</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="input-field"
                placeholder="••••••••"
                required
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full btn-primary flex items-center justify-center gap-2 py-3"
            >
              {loading ? <Loader className="w-4 h-4 animate-spin" /> : (
                <>{isRegister ? <UserPlus className="w-4 h-4" /> : <LogIn className="w-4 h-4" />}
                {isRegister ? 'Create Account' : 'Sign In'}</>
              )}
            </button>
          </form>

          <div className="mt-6 text-center">
            <button
              onClick={() => { setIsRegister(!isRegister); setError(''); }}
              className="text-sm text-indigo-600 hover:text-indigo-700 font-medium"
            >
              {isRegister ? 'Already have an account? Sign in' : "Don't have an account? Register"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

## File: frontend-react/src/pages/Analytics.jsx

import React, { useState, useEffect } from 'react';
import { BarChart3, TrendingUp, Users, Package, DollarSign, Activity, Calendar, ArrowUpRight, ArrowDownRight } from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function Analytics() {
  const [data, setData] = useState(null);
  const [trends, setTrends] = useState(null);
  const [forecast, setForecast] = useState(null);
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => {
    axios.get(`${API_URL}/api/v1/analytics/dashboard`, axiosConfig).then(r => setData(r.data));
    axios.get(`${API_URL}/api/v1/analytics/monthly-trends`, axiosConfig).then(r => setTrends(r.data));
    axios.get(`${API_URL}/api/v1/ai/forecast/revenue`, axiosConfig).then(r => setForecast(r.data)).catch(() => {});
  }, []);

  if (!data) return <div className="p-6 text-center">Loading analytics...</div>;

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Analytics</h1>

      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
        <div className="card p-5">
          <div className="flex items-center gap-3 mb-2">
            <DollarSign className="w-5 h-5 text-green-600" />
            <p className="text-sm text-gray-500">Revenue</p>
          </div>
          <p className="text-2xl font-bold">${Number(data.revenue?.total || 0).toLocaleString()}</p>
          <p className="text-xs text-gray-400 mt-1">{data.revenue?.collection_rate?.toFixed(1)}% collection rate</p>
        </div>
        <div className="card p-5">
          <div className="flex items-center gap-3 mb-2">
            <Users className="w-5 h-5 text-blue-600" />
            <p className="text-sm text-gray-500">Contacts</p>
          </div>
          <p className="text-2xl font-bold">{data.crm?.contacts || 0}</p>
          <p className="text-xs text-gray-400 mt-1">{data.crm?.deals || 0} deals</p>
        </div>
        <div className="card p-5">
          <div className="flex items-center gap-3 mb-2">
            <Package className="w-5 h-5 text-amber-600" />
            <p className="text-sm text-gray-500">Products</p>
          </div>
          <p className="text-2xl font-bold">{data.inventory?.total_products || 0}</p>
          <p className="text-xs text-gray-400 mt-1">{data.inventory?.low_stock || 0} low stock</p>
        </div>
        <div className="card p-5">
          <div className="flex items-center gap-3 mb-2">
            <Activity className="w-5 h-5 text-red-600" />
            <p className="text-sm text-gray-500">Projects</p>
          </div>
          <p className="text-2xl font-bold">{data.projects?.active_projects || 0}</p>
          <p className="text-xs text-gray-400 mt-1">{data.projects?.tasks?.total || 0} total tasks</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="card p-6">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <TrendingUp className="w-5 h-5 text-indigo-600" /> Monthly Trends
          </h2>
          <div className="space-y-3">
            {trends?.revenue?.map((r, i) => (
              <div key={i} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                <span className="font-medium">{r.period}</span>
                <span className="text-gray-900 font-medium">${Number(r.amount).toLocaleString()}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="card p-6">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <BarChart3 className="w-5 h-5 text-indigo-600" /> AI Revenue Forecast
          </h2>
          {forecast ? (
            <div className="space-y-3">
              <div className="flex items-center gap-2 mb-3">
                <span className={`px-2 py-1 rounded text-xs font-medium ${forecast.trend === 'increasing' ? 'bg-green-100 text-green-800' : forecast.trend === 'decreasing' ? 'bg-red-100 text-red-800' : 'bg-gray-100 text-gray-800'}`}>
                  {forecast.trend} trend
                </span>
              </div>
              {forecast.forecast?.map((f, i) => (
                <div key={i} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                  <span className="font-medium">Month +{f.month}</span>
                  <div className="text-right">
                    <p className="font-medium text-gray-900">${Number(f.predicted_revenue).toLocaleString()}</p>
                    <p className="text-xs text-gray-500">${Number(f.confidence_low).toLocaleString()} - ${Number(f.confidence_high).toLocaleString()}</p>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-gray-500 text-center py-8">Forecast data unavailable</p>
          )}
        </div>
      </div>

      <div className="card p-6 mt-6">
        <h2 className="text-lg font-semibold mb-4">Recent Activity</h2>
        <div className="space-y-3">
          {data.recent_activity?.slice(0, 10).map((a, i) => (
            <div key={i} className="flex items-center gap-3 p-3 bg-gray-50 rounded-lg">
              <div className="w-2 h-2 bg-indigo-500 rounded-full" />
              <div className="flex-1">
                <p className="text-sm text-gray-900 capitalize">{a.action.replace(/_/g, ' ')}</p>
                <p className="text-xs text-gray-500">{a.entity_type} • {a.created_at ? new Date(a.created_at).toLocaleString() : ''}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

## File: frontend-react/src/pages/Settings.jsx

import React, { useState, useEffect } from 'react';
import { Settings, Save, Key, Mail, Database, CreditCard, Shield, Bell, Globe, Trash2 } from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function SettingsPage() {
  const [settings, setSettings] = useState([]);
  const [newKey, setNewKey] = useState('');
  const [newValue, setNewValue] = useState('');
  const [newCategory, setNewCategory] = useState('general');
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => {
    fetchSettings();
  }, []);

  const fetchSettings = async () => {
    try {
      const res = await axios.get(`${API_URL}/api/v1/admin/settings`, axiosConfig);
      setSettings(res.data);
    } catch (e) { console.error(e); }
  };

  const addSetting = async () => {
    if (!newKey || !newValue) return;
    try {
      await axios.post(`${API_URL}/api/v1/admin/settings`, {
        key: newKey,
        value: newValue,
        category: newCategory
      }, axiosConfig);
      setNewKey(''); setNewValue(''); setNewCategory('general');
      fetchSettings();
    } catch (e) { console.error(e); }
  };

  const deleteSetting = async (key) => {
    if (!confirm(`Delete setting "${key}"?`)) return;
    try {
      await axios.delete(`${API_URL}/api/v1/admin/settings/${key}`, axiosConfig);
      fetchSettings();
    } catch (e) { console.error(e); }
  };

  const categories = ['general', 'email', 'stripe', 'ai', 'security', 'notifications'];

  const getCategoryIcon = (cat) => {
    if (cat === 'email') return <Mail className="w-4 h-4" />;
    if (cat === 'stripe') return <CreditCard className="w-4 h-4" />;
    if (cat === 'security') return <Shield className="w-4 h-4" />;
    if (cat === 'notifications') return <Bell className="w-4 h-4" />;
    if (cat === 'ai') return <Key className="w-4 h-4" />;
    return <Settings className="w-4 h-4" />;
  };

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-900 mb-6 flex items-center gap-3">
        <Settings className="w-8 h-8 text-indigo-600" /> Settings
      </h1>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 space-y-6">
          <div className="card p-6">
            <h2 className="text-lg font-semibold mb-4">Add New Setting</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
              <input type="text" value={newKey} onChange={e => setNewKey(e.target.value)} placeholder="Key (e.g., app.name)" className="input-field" />
              <input type="text" value={newValue} onChange={e => setNewValue(e.target.value)} placeholder="Value" className="input-field" />
              <select value={newCategory} onChange={e => setNewCategory(e.target.value)} className="input-field">
                {categories.map(c => <option key={c} value={c}>{c}</option>)}
              </select>
            </div>
            <button onClick={addSetting} className="mt-3 btn-primary flex items-center gap-2">
              <Save className="w-4 h-4" /> Save Setting
            </button>
          </div>

          <div className="card overflow-hidden">
            <table className="min-w-full text-sm">
              <thead className="bg-gray-50"><tr>
                <th className="px-4 py-3 text-left font-medium">Key</th>
                <th className="px-4 py-3 text-left font-medium">Value</th>
                <th className="px-4 py-3 text-left font-medium">Category</th>
                <th className="px-4 py-3 text-left font-medium"></th>
              </tr></thead>
              <tbody className="divide-y">
                {settings.map(s => (
                  <tr key={s.id} className="hover:bg-gray-50">
                    <td className="px-4 py-3 font-mono text-indigo-600">{s.key}</td>
                    <td className="px-4 py-3 text-gray-600">{s.value}</td>
                    <td className="px-4 py-3">
                      <span className="flex items-center gap-1 px-2 py-1 bg-gray-100 rounded text-xs text-gray-600 w-fit">
                        {getCategoryIcon(s.category)} {s.category}
                      </span>
                    </td>
                    <td className="px-4 py-3">
                      <button onClick={() => deleteSetting(s.key)} className="p-1.5 text-red-500 hover:bg-red-50 rounded">
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        <div className="space-y-6">
          <div className="card p-5">
            <h3 className="font-semibold text-gray-900 mb-3 flex items-center gap-2">
              <Database className="w-5 h-5 text-indigo-600" /> System Info
            </h3>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between"><span className="text-gray-500">Version</span><span className="font-medium">v1.8.0</span></div>
              <div className="flex justify-between"><span className="text-gray-500">Environment</span><span className="font-medium">Production</span></div>
              <div className="flex justify-between"><span className="text-gray-500">Database</span><span className="font-medium">PostgreSQL</span></div>
            </div>
          </div>

          <div className="card p-5">
            <h3 className="font-semibold text-gray-900 mb-3 flex items-center gap-2">
              <Shield className="w-5 h-5 text-indigo-600" /> Security
            </h3>
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">2FA Required</span>
                <button className="relative inline-flex h-5 w-9 items-center rounded-full bg-gray-200">
                  <span className="inline-block h-3 w-3 transform rounded-full bg-white translate-x-1" />
                </button>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">API Rate Limiting</span>
                <button className="relative inline-flex h-5 w-9 items-center rounded-full bg-indigo-600">
                  <span className="inline-block h-3 w-3 transform rounded-full bg-white translate-x-5" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

## File: frontend-react/src/pages/AIChat.jsx

import React, { useState, useRef, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import {
  MessageSquare, Send, Loader, Bot, User, Lightbulb, Sparkles,
  ChevronLeft, Plus, Clock, Zap, Settings, Trash2, Archive,
  Cpu, BarChart3, Wrench, FileText, ArrowRight, Copy, Check
} from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function AIChat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [streaming, setStreaming] = useState(false);
  const [conversationId, setConversationId] = useState(null);
  const [conversations, setConversations] = useState([]);
  const [models, setModels] = useState([]);
  const [selectedModel, setSelectedModel] = useState('');
  const [templates, setTemplates] = useState([]);
  const [showSidebar, setShowSidebar] = useState(true);
  const [copied, setCopied] = useState(false);
  const messagesEndRef = useRef(null);
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };
  const navigate = useNavigate();

  useEffect(() => {
    fetchConversations();
    fetchModels();
    fetchTemplates();
  }, []);

  const fetchConversations = async () => {
    try {
      const res = await axios.get(`${API_URL}/api/v1/llm/conversations`, axiosConfig);
      setConversations(res.data);
    } catch (e) {}
  };

  const fetchModels = async () => {
    try {
      const res = await axios.get(`${API_URL}/api/v1/llm/models`, axiosConfig);
      setModels(res.data.models || []);
      const defaultModel = res.data.models?.find(m => m.is_default);
      if (defaultModel) setSelectedModel(defaultModel.model_id);
    } catch (e) {}
  };

  const fetchTemplates = async () => {
    try {
      const res = await axios.get(`${API_URL}/api/v1/llm/templates`, axiosConfig);
      setTemplates(res.data);
    } catch (e) {}
  };

  const loadConversation = async (id) => {
    try {
      const res = await axios.get(`${API_URL}/api/v1/llm/conversations/${id}`, axiosConfig);
      const conv = res.data;
      setConversationId(conv.id);
      setMessages(conv.messages.map(m => ({ role: m.role, content: m.content })));
      if (conv.model_id) setSelectedModel(conv.model_id);
    } catch (e) {}
  };

  const newConversation = () => {
    setConversationId(null);
    setMessages([]);
    setInput('');
  };

  const deleteConversation = async (id, e) => {
    e.stopPropagation();
    if (!confirm('Delete this conversation?')) return;
    try {
      await axios.delete(`${API_URL}/api/v1/llm/conversations/${id}`, axiosConfig);
      if (conversationId === id) newConversation();
      fetchConversations();
    } catch (e) {}
  };

  const archiveConversation = async (id, e) => {
    e.stopPropagation();
    try {
      await axios.put(`${API_URL}/api/v1/llm/conversations/${id}/archive`, {}, axiosConfig);
      if (conversationId === id) newConversation();
      fetchConversations();
    } catch (e) {}
  };

  const scrollToBottom = () => messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  useEffect(() => { scrollToBottom(); }, [messages]);

  const sendMessage = async (useStream = false) => {
    if (!input.trim() || loading || streaming) return;
    const userMsg = input.trim();
    setMessages(prev => [...prev, { role: 'user', content: userMsg }]);
    setInput('');
    setLoading(true);

    if (useStream) {
      await streamResponse(userMsg);
    } else {
      await regularResponse(userMsg);
    }
  };

  const regularResponse = async (userMsg) => {
    try {
      const res = await axios.post(`${API_URL}/api/v1/llm/chat`, {
        messages: [...messages, { role: 'user', content: userMsg }].map(m => ({ role: m.role, content: m.content })),
        model_id: selectedModel,
        conversation_id: conversationId,
        use_tools: true
      }, axiosConfig);

      const assistantContent = res.data.message?.content || 'No response';
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: assistantContent,
        model: res.data.message?.model,
        tokens: res.data.message?.tokens_used,
        latency: res.data.message?.latency_ms
      }]);

      if (res.data.conversation_id && !conversationId) {
        setConversationId(res.data.conversation_id);
        fetchConversations();
      }
    } catch (e) {
      setMessages(prev => [...prev, { role: 'assistant', content: 'Error: ' + (e.response?.data?.detail || e.message) }]);
    } finally {
      setLoading(false);
    }
  };

  const streamResponse = async (userMsg) => {
    setStreaming(true);
    setMessages(prev => [...prev, { role: 'assistant', content: '', streaming: true }]);

    try {
      const response = await fetch(`${API_URL}/api/v1/llm/chat/stream`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          messages: [...messages, { role: 'user', content: userMsg }].map(m => ({ role: m.role, content: m.content })),
          model_id: selectedModel
        })
      });

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let fullContent = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const data = JSON.parse(line.slice(6));
              if (data.type === 'content') {
                fullContent += data.content;
                setMessages(prev => {
                  const newMessages = [...prev];
                  const lastMsg = newMessages[newMessages.length - 1];
                  if (lastMsg.role === 'assistant' && lastMsg.streaming) {
                    lastMsg.content = fullContent;
                  }
                  return newMessages;
                });
              } else if (data.type === 'done') {
                setMessages(prev => {
                  const newMessages = [...prev];
                  const lastMsg = newMessages[newMessages.length - 1];
                  if (lastMsg.streaming) {
                    delete lastMsg.streaming;
                    lastContent.tokens = data.total_tokens;
                  }
                  return newMessages;
                });
              }
            } catch (e) {}
          }
        }
      }

      fetchConversations();
    } catch (e) {
      setMessages(prev => {
        const newMessages = [...prev];
        const lastMsg = newMessages[newMessages.length - 1];
        if (lastMsg.streaming) {
          lastMsg.content = 'Error: Streaming failed';
          delete lastMsg.streaming;
        }
        return newMessages;
      });
    } finally {
      setStreaming(false);
      setLoading(false);
    }
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const applyTemplate = (template) => {
    setInput(template.user_prompt_template || '');
  };

  const quickQuestions = [
    'What is my total pipeline value?',
    'Which products are low on stock?',
    'Show me revenue trends',
    'Who are my top customers?',
    'Create a summary of all active projects'
  ];

  return (
    <div className="flex h-[calc(100vh-4rem)]">
      {/* Sidebar */}
      {showSidebar && (
        <div className="w-72 bg-white border-r border-gray-200 flex flex-col">
          <div className="p-4 border-b border-gray-200">
            <button onClick={newConversation} className="w-full btn-primary flex items-center justify-center gap-2 py-2.5">
              <Plus className="w-4 h-4" /> New Chat
            </button>
          </div>

          <div className="flex-1 overflow-y-auto p-2">
            <p className="text-xs font-medium text-gray-500 uppercase tracking-wider px-2 mb-2">Recent Conversations</p>
            {conversations.map(conv => (
              <div
                key={conv.id}
                onClick={() => loadConversation(conv.id)}
                className={`group flex items-center gap-2 px-3 py-2.5 rounded-lg cursor-pointer text-sm mb-1 transition-colors ${
                  conversationId === conv.id ? 'bg-indigo-50 text-indigo-700' : 'hover:bg-gray-50 text-gray-700'
                }`}
              >
                <MessageSquare className="w-4 h-4 flex-shrink-0" />
                <span className="truncate flex-1">{conv.title || 'Untitled'}</span>
                <div className="flex gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                  <button onClick={(e) => archiveConversation(conv.id, e)} className="p-1 hover:bg-gray-200 rounded">
                    <Archive className="w-3 h-3 text-gray-400" />
                  </button>
                  <button onClick={(e) => deleteConversation(conv.id, e)} className="p-1 hover:bg-red-100 rounded">
                    <Trash2 className="w-3 h-3 text-red-400" />
                  </button>
                </div>
              </div>
            ))}
            {conversations.length === 0 && (
              <p className="text-sm text-gray-400 px-2 py-4 text-center">No conversations yet</p>
            )}
          </div>

          <div className="p-3 border-t border-gray-200">
            <p className="text-xs font-medium text-gray-500 uppercase tracking-wider mb-2">Templates</p>
            <div className="space-y-1">
              {templates.slice(0, 5).map(t => (
                <button
                  key={t.id}
                  onClick={() => applyTemplate(t)}
                  className="w-full text-left px-2 py-1.5 text-xs text-gray-600 hover:bg-gray-50 rounded flex items-center gap-1.5"
                >
                  <FileText className="w-3 h-3" />
                  {t.display_name}
                </button>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col bg-white">
        {/* Header */}
        <div className="h-14 border-b border-gray-200 flex items-center justify-between px-4">
          <div className="flex items-center gap-3">
            <button onClick={() => setShowSidebar(!showSidebar)} className="p-1.5 hover:bg-gray-100 rounded-lg text-gray-500">
              <ChevronLeft className={`w-5 h-5 transition-transform ${!showSidebar ? 'rotate-180' : ''}`} />
            </button>
            <div className="flex items-center gap-2">
              <Bot className="w-5 h-5 text-indigo-600" />
              <h2 className="font-semibold text-gray-900">AI Assistant</h2>
            </div>
          </div>

          <div className="flex items-center gap-3">
            {/* Model Selector */}
            <select
              value={selectedModel}
              onChange={(e) => setSelectedModel(e.target.value)}
              className="text-sm border border-gray-300 rounded-lg px-3 py-1.5 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
            >
              {models.map(m => (
                <option key={m.model_id} value={m.model_id}>
                  {m.display_name} {m.is_default ? '(Default)' : ''}
                </option>
              ))}
            </select>

            <button onClick={() => navigate('/llm-manager')} className="p-1.5 hover:bg-gray-100 rounded-lg text-gray-500" title="LLM Manager">
              <Settings className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.length === 0 && (
            <div className="flex flex-col items-center justify-center h-full text-center">
              <div className="w-16 h-16 bg-indigo-100 rounded-2xl flex items-center justify-center mb-4">
                <Sparkles className="w-8 h-8 text-indigo-600" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-2">How can I help you today?</h3>
              <p className="text-gray-500 max-w-md mb-6">Ask about your business data, get insights, or use templates for specific tasks.</p>
              <div className="flex flex-wrap gap-2 justify-center max-w-lg">
                {quickQuestions.map((q, i) => (
                  <button
                    key={i}
                    onClick={() => { setInput(q); }}
                    className="px-4 py-2 bg-gray-100 text-gray-600 rounded-full text-sm hover:bg-gray-200 transition-colors"
                  >
                    {q}
                  </button>
                ))}
              </div>
            </div>
          )}

          {messages.map((msg, i) => (
            <div key={i} className={`flex gap-3 ${msg.role === 'user' ? 'justify-end' : ''}`}>
              {msg.role === 'assistant' && (
                <div className="w-8 h-8 bg-indigo-100 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                  <Sparkles className="w-4 h-4 text-indigo-600" />
                </div>
              )}
              <div className={`max-w-[80%] ${msg.role === 'user' ? 'bg-indigo-600 text-white' : 'bg-gray-100 text-gray-800'} rounded-lg p-3`}>
                <div className="text-sm whitespace-pre-wrap">{msg.content || (msg.streaming ? <span className="animate-pulse">▋</span> : '')}</div>

                {msg.role === 'assistant' && !msg.streaming && (
                  <div className="flex items-center gap-2 mt-2 pt-2 border-t border-gray-200/50">
                    {msg.model && <span className="text-xs text-gray-400">{msg.model}</span>}
                    {msg.tokens && <span className="text-xs text-gray-400">{msg.tokens} tokens</span>}
                    {msg.latency && <span className="text-xs text-gray-400">{msg.latency}ms</span>}
                    <button onClick={() => copyToClipboard(msg.content)} className="ml-auto p-1 hover:bg-gray-200 rounded">
                      {copied ? <Check className="w-3 h-3 text-green-500" /> : <Copy className="w-3 h-3 text-gray-400" />}
                    </button>
                  </div>
                )}
              </div>
              {msg.role === 'user' && (
                <div className="w-8 h-8 bg-gray-200 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                  <User className="w-4 h-4 text-gray-600" />
                </div>
              )}
            </div>
          ))}

          {loading && !streaming && (
            <div className="flex gap-3">
              <div className="w-8 h-8 bg-indigo-100 rounded-full flex items-center justify-center">
                <Loader className="w-4 h-4 text-indigo-600 animate-spin" />
              </div>
              <div className="bg-gray-100 p-3 rounded-lg">
                <p className="text-sm text-gray-500">Thinking...</p>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <div className="p-4 border-t border-gray-200">
          <div className="flex gap-2 mb-3">
            {templates.slice(0, 3).map(t => (
              <button
                key={t.id}
                onClick={() => applyTemplate(t)}
                className="px-3 py-1.5 bg-gray-100 text-gray-600 rounded-full text-xs hover:bg-gray-200 transition-colors flex items-center gap-1"
              >
                <Lightbulb className="w-3 h-3" />
                {t.display_name}
              </button>
            ))}
          </div>
          <div className="flex gap-2">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault();
                  sendMessage(e.metaKey || e.ctrlKey);
                }
              }}
              placeholder="Ask about your business... (Cmd+Enter to stream)"
              className="flex-1 input-field"
              disabled={loading || streaming}
            />
            <button
              onClick={() => sendMessage(true)}
              disabled={loading || streaming || !input.trim()}
              className="btn-primary px-4 flex items-center gap-2"
              title="Stream response"
            >
              <Zap className="w-4 h-4" />
            </button>
            <button
              onClick={() => sendMessage(false)}
              disabled={loading || streaming || !input.trim()}
              className="btn-primary px-4"
            >
              <Send className="w-4 h-4" />
            </button>
          </div>
          <p className="text-xs text-gray-400 mt-2">Press Enter to send, Cmd+Enter to stream • Model: {selectedModel}</p>
        </div>
      </div>
    </div>
  );
}

## File: frontend-react/src/pages/Reports.jsx

import React, { useState, useEffect } from 'react';
import { FileText, BarChart3, Download, TrendingUp, PieChart, Activity } from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function Reports() {
  const [revenue, setRevenue] = useState(null);
  const [pipeline, setPipeline] = useState(null);
  const [inventory, setInventory] = useState(null);
  const [activeReport, setActiveReport] = useState('revenue');
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => {
    if (activeReport === 'revenue') axios.get(`${API_URL}/api/v1/reports/revenue`, axiosConfig).then(r => setRevenue(r.data));
    if (activeReport === 'pipeline') axios.get(`${API_URL}/api/v1/reports/pipeline`, axiosConfig).then(r => setPipeline(r.data));
    if (activeReport === 'inventory') axios.get(`${API_URL}/api/v1/reports/inventory`, axiosConfig).then(r => setInventory(r.data));
  }, [activeReport]);

  const reports = [
    { id: 'revenue', label: 'Revenue Report', icon: TrendingUp },
    { id: 'pipeline', label: 'Sales Pipeline', icon: PieChart },
    { id: 'inventory', label: 'Inventory Status', icon: Activity },
  ];

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Reports</h1>
      <div className="flex gap-2 mb-6">
        {reports.map(r => (
          <button key={r.id} onClick={() => setActiveReport(r.id)}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition-all ${activeReport === r.id ? 'bg-indigo-600 text-white' : 'bg-white border text-gray-600 hover:bg-gray-50'}`}>
            <r.icon className="w-4 h-4" />{r.label}
          </button>
        ))}
      </div>
      <div className="card p-6">
        {activeReport === 'revenue' && revenue && (
          <div>
            <div className="grid grid-cols-3 gap-4 mb-6">
              <div className="p-4 bg-gray-50 rounded-lg"><p className="text-sm text-gray-500">Total Revenue</p><p className="text-2xl font-bold">${Number(revenue.total_revenue).toLocaleString()}</p></div>
              <div className="p-4 bg-gray-50 rounded-lg"><p className="text-sm text-gray-500">Total Paid</p><p className="text-2xl font-bold">${Number(revenue.total_paid).toLocaleString()}</p></div>
              <div className="p-4 bg-gray-50 rounded-lg"><p className="text-sm text-gray-500">Outstanding</p><p className="text-2xl font-bold">${Number(revenue.outstanding).toLocaleString()}</p></div>
            </div>
            <h3 className="font-semibold mb-3">Monthly Breakdown</h3>
            <div className="space-y-2">
              {revenue.monthly_breakdown?.map((m, i) => (
                <div key={i} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                  <span className="font-medium">{m.month}</span>
                  <span className="text-gray-900">${Number(m.revenue).toLocaleString()} ({m.count} invoices)</span>
                </div>
              ))}
            </div>
          </div>
        )}
        {activeReport === 'pipeline' && pipeline && (
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
            {Object.entries(pipeline).map(([stage, data]) => (
              <div key={stage} className="p-4 bg-gray-50 rounded-lg">
                <p className="text-sm text-gray-500 capitalize">{stage.replace(/_/g, ' ')}</p>
                <p className="text-2xl font-bold">{data.count}</p>
                <p className="text-sm text-gray-600">${Number(data.value).toLocaleString()}</p>
              </div>
            ))}
          </div>
        )}
        {activeReport === 'inventory' && inventory && (
          <div>
            <div className="grid grid-cols-3 gap-4 mb-6">
              <div className="p-4 bg-gray-50 rounded-lg"><p className="text-sm text-gray-500">Total Products</p><p className="text-2xl font-bold">{inventory.total_products}</p></div>
              <div className="p-4 bg-gray-50 rounded-lg"><p className="text-sm text-gray-500">Stock Value</p><p className="text-2xl font-bold">${Number(inventory.total_stock_value).toLocaleString()}</p></div>
              <div className="p-4 bg-gray-50 rounded-lg"><p className="text-sm text-gray-500">Low Stock</p><p className="text-2xl font-bold text-red-600">{inventory.low_stock_count}</p></div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

## File: frontend-react/src/pages/LLMManager.jsx

import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Cpu, BarChart3, FileText, Plus, Trash2, ToggleLeft, ToggleRight,
  Download, CheckCircle, AlertTriangle, Clock, Zap, TrendingUp,
  Database, ArrowLeft, RefreshCw, Settings, MessageSquare, Layers
} from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function LLMManager() {
  const [activeTab, setActiveTab] = useState('models');
  const [models, setModels] = useState([]);
  const [availableModels, setAvailableModels] = useState([]);
  const [templates, setTemplates] = useState([]);
  const [usage, setUsage] = useState(null);
  const [conversations, setConversations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);
  const [pulling, setPulling] = useState(false);
  const navigate = useNavigate();
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => {
    fetchAllData();
  }, []);

  const fetchAllData = async () => {
    setLoading(true);
    try {
      const [modelsRes, templatesRes, usageRes, convRes] = await Promise.all([
        axios.get(`${API_URL}/api/v1/llm/models`, axiosConfig),
        axios.get(`${API_URL}/api/v1/llm/templates`, axiosConfig),
        axios.get(`${API_URL}/api/v1/llm/analytics/usage?days=30`, axiosConfig),
        axios.get(`${API_URL}/api/v1/llm/analytics/conversations`, axiosConfig),
      ]);
      setModels(modelsRes.data.models || []);
      setAvailableModels(modelsRes.data.available_from_provider || []);
      setTemplates(templatesRes.data);
      setUsage(usageRes.data);
      setConversations(convRes.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to load LLM data');
    } finally {
      setLoading(false);
    }
  };

  const pullModel = async (modelId) => {
    setPulling(true);
    try {
      await axios.post(`${API_URL}/api/v1/llm/models/${modelId}/pull`, {}, axiosConfig);
      setSuccess(`Model ${modelId} pulled successfully`);
      fetchAllData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to pull model');
    } finally {
      setPulling(false);
    }
  };

  const toggleModel = async (modelId) => {
    try {
      const model = models.find(m => m.model_id === modelId);
      await axios.put(`${API_URL}/api/v1/llm/models/${modelId}`, {
        is_active: !model.is_active
      }, axiosConfig);
      fetchAllData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to toggle model');
    }
  };

  const setDefault = async (modelId) => {
    try {
      await axios.put(`${API_URL}/api/v1/llm/models/${modelId}`, {
        is_default: true
      }, axiosConfig);
      fetchAllData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to set default');
    }
  };

  const deleteTemplate = async (id) => {
    if (!confirm('Delete this template?')) return;
    try {
      await axios.delete(`${API_URL}/api/v1/llm/templates/${id}`, axiosConfig);
      setSuccess('Template deleted');
      fetchAllData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to delete template');
    }
  };

  if (loading) return <div className="p-6 text-center">Loading LLM Manager...</div>;

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <button onClick={() => navigate('/ai-chat')} className="p-2 hover:bg-gray-100 rounded-lg text-gray-500">
            <ArrowLeft className="w-5 h-5" />
          </button>
          <h1 className="text-3xl font-bold text-gray-900 flex items-center gap-3">
            <Cpu className="w-8 h-8 text-indigo-600" />
            LLM Manager
          </h1>
        </div>
      </div>

      {success && (
        <div className="mb-6 p-4 bg-green-50 border border-green-200 rounded-xl flex items-center gap-3">
          <CheckCircle className="w-5 h-5 text-green-600" />
          <p className="text-sm text-green-700">{success}</p>
        </div>
      )}

      {error && (
        <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-xl flex items-center gap-3">
          <AlertTriangle className="w-5 h-5 text-red-600" />
          <p className="text-sm text-red-700">{error}</p>
        </div>
      )}

      {/* Stats Cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
        <div className="card p-5">
          <div className="flex items-center gap-3 mb-2">
            <MessageSquare className="w-5 h-5 text-indigo-600" />
            <p className="text-sm text-gray-500">Total Requests</p>
          </div>
          <p className="text-2xl font-bold">{usage?.total_requests?.toLocaleString() || 0}</p>
          <p className="text-xs text-gray-400 mt-1">Last 30 days</p>
        </div>
        <div className="card p-5">
          <div className="flex items-center gap-3 mb-2">
            <Database className="w-5 h-5 text-green-600" />
            <p className="text-sm text-gray-500">Total Tokens</p>
          </div>
          <p className="text-2xl font-bold">{usage?.total_tokens?.toLocaleString() || 0}</p>
          <p className="text-xs text-gray-400 mt-1">Prompt + Completion</p>
        </div>
        <div className="card p-5">
          <div className="flex items-center gap-3 mb-2">
            <Clock className="w-5 h-5 text-amber-600" />
            <p className="text-sm text-gray-500">Avg Latency</p>
          </div>
          <p className="text-2xl font-bold">{usage?.avg_latency_ms?.toFixed(0) || 0}ms</p>
          <p className="text-xs text-gray-400 mt-1">Per request</p>
        </div>
        <div className="card p-5">
          <div className="flex items-center gap-3 mb-2">
            <Layers className="w-5 h-5 text-purple-600" />
            <p className="text-sm text-gray-500">Conversations</p>
          </div>
          <p className="text-2xl font-bold">{conversations?.total_conversations || 0}</p>
          <p className="text-xs text-gray-400 mt-1">{conversations?.total_messages || 0} messages</p>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex gap-1 mb-6 bg-gray-100 p-1 rounded-lg w-fit">
        {[
          { id: 'models', label: 'Models', icon: Cpu },
          { id: 'templates', label: 'Templates', icon: FileText },
          { id: 'usage', label: 'Usage Analytics', icon: BarChart3 },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => { setActiveTab(tab.id); setError(null); setSuccess(null); }}
            className={`flex items-center gap-2 px-4 py-2 rounded-md font-medium transition-all ${
              activeTab === tab.id ? 'bg-white text-indigo-600 shadow-sm' : 'text-gray-600 hover:text-gray-900'
            }`}
          >
            <tab.icon className="w-4 h-4" />
            {tab.label}
          </button>
        ))}
      </div>

      {/* Models Tab */}
      {activeTab === 'models' && (
        <div className="space-y-6">
          <div className="card p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
              <Cpu className="w-5 h-5 text-indigo-600" />
              Configured Models
            </h2>
            <div className="space-y-3">
              {models.map(model => (
                <div key={model.id} className={`flex items-center justify-between p-4 rounded-lg border ${model.is_default ? 'border-indigo-200 bg-indigo-50/50' : 'border-gray-200'}`}>
                  <div className="flex items-center gap-4">
                    <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${model.is_available ? 'bg-green-100 text-green-600' : 'bg-gray-100 text-gray-400'}`}>
                      <Cpu className="w-5 h-5" />
                    </div>
                    <div>
                      <div className="flex items-center gap-2">
                        <h3 className="font-semibold text-gray-900">{model.display_name}</h3>
                        {model.is_default && <span className="px-2 py-0.5 bg-indigo-100 text-indigo-700 rounded text-xs font-medium">Default</span>}
                        {model.is_available ? <span className="px-2 py-0.5 bg-green-100 text-green-700 rounded text-xs font-medium">Available</span> : <span className="px-2 py-0.5 bg-red-100 text-red-700 rounded text-xs font-medium">Not Pulled</span>}
                      </div>
                      <p className="text-sm text-gray-500">{model.model_id} • {model.provider} • {model.context_window?.toLocaleString()} context</p>
                      <p className="text-sm text-gray-400">{model.description}</p>
                      <div className="flex gap-2 mt-1">
                        {model.supports_streaming && <span className="text-xs text-gray-500 flex items-center gap-1"><Zap className="w-3 h-3" /> Streaming</span>}
                        {model.supports_tools && <span className="text-xs text-gray-500 flex items-center gap-1"><Settings className="w-3 h-3" /> Tools</span>}
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    {!model.is_available && (
                      <button
                        onClick={() => pullModel(model.model_id)}
                        disabled={pulling}
                        className="px-3 py-1.5 bg-indigo-600 text-white rounded-lg text-sm hover:bg-indigo-700 disabled:opacity-50 flex items-center gap-1"
                      >
                        <Download className="w-4 h-4" />
                        {pulling ? 'Pulling...' : 'Pull'}
                      </button>
                    )}
                    {!model.is_default && model.is_active && (
                      <button onClick={() => setDefault(model.model_id)} className="px-3 py-1.5 text-sm text-indigo-600 hover:bg-indigo-50 rounded-lg">
                        Set Default
                      </button>
                    )}
                    <button onClick={() => toggleModel(model.model_id)} className="p-2 hover:bg-gray-100 rounded-lg">
                      {model.is_active ? <ToggleRight className="w-5 h-5 text-green-600" /> : <ToggleLeft className="w-5 h-5 text-gray-400" />}
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="card p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
              <RefreshCw className="w-5 h-5 text-indigo-600" />
              Available from Ollama
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
              {availableModels.filter(am => !models.some(m => m.model_id === am.name)).map(am => (
                <div key={am.name} className="p-3 bg-gray-50 rounded-lg flex items-center justify-between">
                  <div>
                    <p className="font-medium text-gray-900">{am.name}</p>
                    <p className="text-xs text-gray-500">{(am.size / 1024 / 1024 / 1024).toFixed(1)} GB</p>
                  </div>
                </div>
              ))}
              {availableModels.filter(am => !models.some(m => m.model_id === am.name)).length === 0 && (
                <p className="text-sm text-gray-500 col-span-full">All available models are configured</p>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Templates Tab */}
      {activeTab === 'templates' && (
        <div className="space-y-6">
          <div className="card p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
              <FileText className="w-5 h-5 text-indigo-600" />
              Prompt Templates
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {templates.map(t => (
                <div key={t.id} className="p-4 bg-gray-50 rounded-lg">
                  <div className="flex items-start justify-between">
                    <div>
                      <h3 className="font-semibold text-gray-900">{t.display_name}</h3>
                      <p className="text-sm text-gray-500">{t.description}</p>
                      <span className="inline-block mt-2 px-2 py-0.5 bg-gray-200 text-gray-600 rounded text-xs capitalize">{t.category}</span>
                    </div>
                    <button onClick={() => deleteTemplate(t.id)} className="p-1.5 hover:bg-red-50 text-red-500 rounded">
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                  <div className="mt-3 p-2 bg-white rounded border border-gray-200 text-xs font-mono text-gray-600 line-clamp-3">
                    {t.system_prompt}
                  </div>
                </div>
              ))}
            </div>
            {templates.length === 0 && (
              <div className="text-center py-8 text-gray-500">
                <FileText className="w-12 h-12 mx-auto mb-3 text-gray-300" />
                <p>No templates configured</p>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Usage Analytics Tab */}
      {activeTab === 'usage' && usage && (
        <div className="space-y-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="card p-6">
              <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
                <TrendingUp className="w-5 h-5 text-indigo-600" />
                Usage by Model
              </h2>
              <div className="space-y-3">
                {usage.by_model?.map(m => (
                  <div key={m.model} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                    <div>
                      <p className="font-medium text-gray-900">{m.model}</p>
                      <p className="text-sm text-gray-500">{m.requests} requests</p>
                    </div>
                    <div className="text-right">
                      <p className="font-medium text-gray-900">{m.tokens?.toLocaleString()} tokens</p>
                      <p className="text-sm text-gray-500">{m.avg_latency_ms?.toFixed(0)}ms avg</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div className="card p-6">
              <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
                <BarChart3 className="w-5 h-5 text-indigo-600" />
                Daily Usage
              </h2>
              <div className="space-y-2">
                {usage.by_day?.slice(-14).map(d => (
                  <div key={d.date} className="flex items-center gap-3">
                    <span className="text-sm text-gray-500 w-24">{d.date}</span>
                    <div className="flex-1 h-6 bg-gray-100 rounded overflow-hidden">
                      <div
                        className="h-full bg-indigo-500 rounded"
                        style={{ width: `${Math.min((d.tokens / (usage.total_tokens || 1)) * 100 * 7, 100)}%` }}
                      />
                    </div>
                    <span className="text-sm text-gray-700 w-20 text-right">{d.tokens?.toLocaleString()}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <div className="card p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Endpoint Breakdown</h2>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              {usage.by_endpoint?.map(e => (
                <div key={e.endpoint} className="p-3 bg-gray-50 rounded-lg text-center">
                  <p className="text-sm text-gray-500 capitalize">{e.endpoint?.replace(/_/g, ' ')}</p>
                  <p className="text-xl font-bold text-gray-900">{e.requests}</p>
                  <p className="text-xs text-gray-400">{e.tokens?.toLocaleString()} tokens</p>
                </div>
              ))}
            </div>
          </div>

          <div className="grid grid-cols-3 gap-4">
            <div className="card p-4">
              <p className="text-sm text-gray-500">Prompt Tokens</p>
              <p className="text-xl font-bold">{usage.prompt_tokens?.toLocaleString()}</p>
            </div>
            <div className="card p-4">
              <p className="text-sm text-gray-500">Completion Tokens</p>
              <p className="text-xl font-bold">{usage.completion_tokens?.toLocaleString()}</p>
            </div>
            <div className="card p-4">
              <p className="text-sm text-gray-500">Error Rate</p>
              <p className="text-xl font-bold">{usage.error_rate?.toFixed(1)}%</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

## File: frontend-react/src/pages/CRM.jsx

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Users, Building2, DollarSign, Plus, Search, Filter, Phone, Mail } from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function CRM() {
  const [activeTab, setActiveTab] = useState('contacts');
  const [contacts, setContacts] = useState([]);
  const [companies, setCompanies] = useState([]);
  const [deals, setDeals] = useState([]);
  const [pipeline, setPipeline] = useState({});
  const [loading, setLoading] = useState(true);
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => { fetchData(); }, [activeTab]);
  const fetchData = async () => {
    setLoading(true);
    try {
      if (activeTab === 'contacts') {
        const res = await axios.get(`${API_URL}/api/v1/crm/contacts`, axiosConfig);
        setContacts(res.data);
      } else if (activeTab === 'companies') {
        const res = await axios.get(`${API_URL}/api/v1/crm/companies`, axiosConfig);
        setCompanies(res.data);
      } else if (activeTab === 'deals') {
        const res = await axios.get(`${API_URL}/api/v1/crm/deals`, axiosConfig);
        setDeals(res.data);
      } else if (activeTab === 'pipeline') {
        const res = await axios.get(`${API_URL}/api/v1/crm/deals/pipeline`, axiosConfig);
        setPipeline(res.data);
      }
    } catch (e) { console.error(e); }
    finally { setLoading(false); }
  };

  const tabs = [
    { id: 'contacts', label: 'Contacts', icon: Users },
    { id: 'companies', label: 'Companies', icon: Building2 },
    { id: 'deals', label: 'Deals', icon: DollarSign },
    { id: 'pipeline', label: 'Pipeline', icon: Filter },
  ];

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-3xl font-bold text-gray-900">CRM</h1>
        <button className="btn-primary flex items-center gap-2"><Plus className="w-4 h-4" /> New</button>
      </div>
      <div className="flex gap-1 mb-6 bg-gray-100 p-1 rounded-lg w-fit">
        {tabs.map(t => (
          <button key={t.id} onClick={() => setActiveTab(t.id)}
            className={`flex items-center gap-2 px-4 py-2 rounded-md font-medium transition-all ${activeTab === t.id ? 'bg-white text-indigo-600 shadow-sm' : 'text-gray-600'}`}>
            <t.icon className="w-4 h-4" />{t.label}
          </button>
        ))}
      </div>
      {loading ? <div className="text-center py-12 text-gray-500">Loading...</div> : (
        <>
          {activeTab === 'contacts' && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {contacts.map(c => (
                <div key={c.id} className="card p-5">
                  <div className="flex items-start justify-between">
                    <div>
                      <h3 className="font-semibold text-gray-900">{c.first_name} {c.last_name}</h3>
                      <p className="text-sm text-gray-500">{c.title}</p>
                    </div>
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${c.status === 'customer' ? 'bg-green-100 text-green-800' : c.status === 'lead' ? 'bg-blue-100 text-blue-800' : 'bg-gray-100 text-gray-800'}`}>{c.status}</span>
                  </div>
                  <div className="mt-3 space-y-1">
                    {c.email && <div className="flex items-center gap-2 text-sm text-gray-600"><Mail className="w-4 h-4" />{c.email}</div>}
                    {c.phone && <div className="flex items-center gap-2 text-sm text-gray-600"><Phone className="w-4 h-4" />{c.phone}</div>}
                  </div>
                </div>
              ))}
            </div>
          )}
          {activeTab === 'pipeline' && (
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
              {Object.entries(pipeline).map(([stage, data]) => (
                <div key={stage} className="card p-4">
                  <h3 className="text-sm font-medium text-gray-500 capitalize mb-2">{stage.replace(/_/g, ' ')}</h3>
                  <p className="text-2xl font-bold text-gray-900">{data.count}</p>
                  <p className="text-sm text-gray-600">${Number(data.total_value || 0).toLocaleString()}</p>
                </div>
              ))}
            </div>
          )}
          {activeTab === 'companies' && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {companies.map(c => (
                <div key={c.id} className="card p-5">
                  <h3 className="font-semibold text-gray-900">{c.name}</h3>
                  <p className="text-sm text-gray-500">{c.industry}</p>
                  <p className="text-sm text-gray-400 mt-1">{c.size} employees</p>
                </div>
              ))}
            </div>
          )}
          {activeTab === 'deals' && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {deals.map(d => (
                <div key={d.id} className="card p-5">
                  <div className="flex items-start justify-between">
                    <h3 className="font-semibold text-gray-900">{d.title}</h3>
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${d.stage === 'closed_won' ? 'bg-green-100 text-green-800' : d.stage === 'closed_lost' ? 'bg-red-100 text-red-800' : 'bg-blue-100 text-blue-800'}`}>{d.stage}</span>
                  </div>
                  <p className="text-lg font-bold text-indigo-600 mt-2">${Number(d.value || 0).toLocaleString()}</p>
                  <p className="text-sm text-gray-500">{d.probability}% probability</p>
                </div>
              ))}
            </div>
          )}
        </>
      )}
    </div>
  );
}

## File: frontend-react/src/pages/Permissions.jsx

import React, { useState, useEffect } from 'react';
import {
  Shield, Users, Key, Lock, Eye, EyeOff, FileText, ChevronDown, ChevronUp,
  Plus, Trash2, Save, CheckCircle, AlertTriangle, Search, Filter,
  ToggleLeft, ToggleRight, Settings, UserCheck, Database, ArrowRight
} from 'lucide-react';
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const resources = [
  'contacts', 'companies', 'deals', 'products', 'employees', 'departments',
  'invoices', 'projects', 'tasks', 'reports', 'workflows', 'settings', 'users', 'bulk', 'migrations'
];

const actions = ['read', 'create', 'update', 'delete'];
const accessLevels = [
  { value: 'read', label: 'Read Only', color: 'text-blue-600', bg: 'bg-blue-50' },
  { value: 'write', label: 'Read & Write', color: 'text-green-600', bg: 'bg-green-50' },
  { value: 'hidden', label: 'Hidden', color: 'text-red-600', bg: 'bg-red-50' },
];

export default function PermissionsManager() {
  const [activeTab, setActiveTab] = useState('roles');
  const [roles, setRoles] = useState([]);
  const [permissions, setPermissions] = useState([]);
  const [fieldPermissions, setFieldPermissions] = useState([]);
  const [dataPolicies, setDataPolicies] = useState([]);
  const [users, setUsers] = useState([]);
  const [myPerms, setMyPerms] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  // Form states
  const [newRole, setNewRole] = useState({ name: '', display_name: '', description: '' });
  const [selectedRole, setSelectedRole] = useState(null);
  const [selectedUser, setSelectedUser] = useState(null);
  const [rolePermissions, setRolePermissions] = useState([]);
  const [userRoles, setUserRoles] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => {
    fetchAllData();
  }, []);

  const fetchAllData = async () => {
    setLoading(true);
    try {
      const [rolesRes, permsRes, fpRes, dpRes, myRes] = await Promise.all([
        axios.get(`${API_URL}/api/v1/permissions/roles`, axiosConfig),
        axios.get(`${API_URL}/api/v1/permissions/permissions`, axiosConfig),
        axios.get(`${API_URL}/api/v1/permissions/field-permissions`, axiosConfig),
        axios.get(`${API_URL}/api/v1/permissions/data-policies`, axiosConfig),
        axios.get(`${API_URL}/api/v1/permissions/me`, axiosConfig),
      ]);
      setRoles(rolesRes.data);
      setPermissions(permsRes.data);
      setFieldPermissions(fpRes.data);
      setDataPolicies(dpRes.data);
      setMyPerms(myRes.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to load permissions data');
    } finally {
      setLoading(false);
    }
  };

  const createRole = async () => {
    if (!newRole.name || !newRole.display_name) return;
    try {
      await axios.post(`${API_URL}/api/v1/permissions/roles`, newRole, axiosConfig);
      setNewRole({ name: '', display_name: '', description: '' });
      setSuccess('Role created successfully');
      fetchAllData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to create role');
    }
  };

  const deleteRole = async (id) => {
    if (!confirm('Delete this role?')) return;
    try {
      await axios.delete(`${API_URL}/api/v1/permissions/roles/${id}`, axiosConfig);
      setSuccess('Role deleted');
      fetchAllData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to delete role');
    }
  };

  const togglePolicy = async (id) => {
    try {
      await axios.put(`${API_URL}/api/v1/permissions/data-policies/${id}/toggle`, {}, axiosConfig);
      fetchAllData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to toggle policy');
    }
  };

  const deletePolicy = async (id) => {
    if (!confirm('Delete this policy?')) return;
    try {
      await axios.delete(`${API_URL}/api/v1/permissions/data-policies/${id}`, axiosConfig);
      setSuccess('Policy deleted');
      fetchAllData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to delete policy');
    }
  };

  const assignPermissionsToRole = async (roleId, permIds) => {
    try {
      await axios.post(`${API_URL}/api/v1/permissions/roles/${roleId}/permissions`, { permission_ids: permIds }, axiosConfig);
      setSuccess('Permissions updated');
      fetchAllData();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to assign permissions');
    }
  };

  if (loading) return <div className="p-6 text-center">Loading permissions...</div>;
  if (error) return <div className="p-6 text-center text-red-600">{error}</div>;
  if (!myPerms?.is_admin) return (
    <div className="p-6 max-w-7xl mx-auto">
      <div className="card p-8 text-center">
        <Shield className="w-16 h-16 text-red-400 mx-auto mb-4" />
        <h2 className="text-xl font-bold text-gray-900">Access Denied</h2>
        <p className="text-gray-500 mt-2">You need admin privileges to manage permissions.</p>
      </div>
    </div>
  );

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 flex items-center gap-3">
          <Shield className="w-8 h-8 text-indigo-600" />
          Permissions & RBAC
        </h1>
        <p className="text-gray-600 mt-2">Manage roles, permissions, field-level access, and data policies</p>
      </div>

      {success && (
        <div className="mb-6 p-4 bg-green-50 border border-green-200 rounded-xl flex items-center gap-3">
          <CheckCircle className="w-5 h-5 text-green-600" />
          <p className="text-sm text-green-700">{success}</p>
        </div>
      )}

      {error && (
        <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-xl flex items-center gap-3">
          <AlertTriangle className="w-5 h-5 text-red-600" />
          <p className="text-sm text-red-700">{error}</p>
        </div>
      )}

      {/* My Permissions Card */}
      <div className="card p-5 mb-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-3 flex items-center gap-2">
          <UserCheck className="w-5 h-5 text-indigo-600" />
          Your Access Level
        </h2>
        <div className="flex flex-wrap gap-2">
          {myPerms?.roles?.map(role => (
            <span key={role} className="px-3 py-1 bg-indigo-100 text-indigo-700 rounded-full text-sm font-medium capitalize">
              {role}
            </span>
          ))}
        </div>
        <p className="text-sm text-gray-500 mt-2">{myPerms?.permissions?.length || 0} permissions granted</p>
      </div>

      {/* Tabs */}
      <div className="flex gap-1 mb-6 bg-gray-100 p-1 rounded-lg w-fit">
        {[
          { id: 'roles', label: 'Roles', icon: Users },
          { id: 'permissions', label: 'Permissions', icon: Key },
          { id: 'fields', label: 'Field Access', icon: Eye },
          { id: 'policies', label: 'Data Policies', icon: Database },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => { setActiveTab(tab.id); setError(null); setSuccess(null); }}
            className={`flex items-center gap-2 px-4 py-2 rounded-md font-medium transition-all ${
              activeTab === tab.id ? 'bg-white text-indigo-600 shadow-sm' : 'text-gray-600 hover:text-gray-900'
            }`}
          >
            <tab.icon className="w-4 h-4" />
            {tab.label}
          </button>
        ))}
      </div>

      {/* Roles Tab */}
      {activeTab === 'roles' && (
        <div className="space-y-6">
          <div className="card p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
              <Plus className="w-5 h-5 text-indigo-600" />
              Create New Role
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
              <input
                type="text"
                value={newRole.name}
                onChange={e => setNewRole({...newRole, name: e.target.value})}
                placeholder="Role key (e.g., sales_manager)"
                className="input-field"
              />
              <input
                type="text"
                value={newRole.display_name}
                onChange={e => setNewRole({...newRole, display_name: e.target.value})}
                placeholder="Display name"
                className="input-field"
              />
              <input
                type="text"
                value={newRole.description}
                onChange={e => setNewRole({...newRole, description: e.target.value})}
                placeholder="Description"
                className="input-field"
              />
            </div>
            <button onClick={createRole} className="mt-3 btn-primary flex items-center gap-2">
              <Save className="w-4 h-4" /> Create Role
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {roles.map(role => (
              <div key={role.id} className={`card p-5 ${role.is_system ? 'border-indigo-200' : ''}`}>
                <div className="flex items-start justify-between">
                  <div>
                    <h3 className="font-semibold text-gray-900">{role.display_name}</h3>
                    <p className="text-sm text-gray-500 font-mono">{role.name}</p>
                  </div>
                  {role.is_system && (
                    <span className="px-2 py-1 bg-indigo-100 text-indigo-700 rounded text-xs font-medium">System</span>
                  )}
                </div>
                <p className="text-sm text-gray-600 mt-2">{role.description}</p>
                <div className="mt-3">
                  <p className="text-xs text-gray-500 mb-1">{role.permissions?.length || 0} permissions</p>
                  <div className="flex flex-wrap gap-1">
                    {(role.permissions || []).slice(0, 5).map(p => (
                      <span key={p.id} className="px-2 py-0.5 bg-gray-100 text-gray-600 rounded text-xs">
                        {p.resource}.{p.action}
                      </span>
                    ))}
                    {(role.permissions || []).length > 5 && (
                      <span className="px-2 py-0.5 bg-gray-100 text-gray-500 rounded text-xs">+{(role.permissions || []).length - 5} more</span>
                    )}
                  </div>
                </div>
                {!role.is_system && (
                  <button
                    onClick={() => deleteRole(role.id)}
                    className="mt-3 flex items-center gap-1 text-sm text-red-600 hover:text-red-700"
                  >
                    <Trash2 className="w-4 h-4" /> Delete
                  </button>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Permissions Matrix Tab */}
      {activeTab === 'permissions' && (
        <div className="card overflow-hidden">
          <div className="p-4 border-b border-gray-200">
            <h2 className="text-lg font-semibold text-gray-900 flex items-center gap-2">
              <Key className="w-5 h-5 text-indigo-600" />
              Permission Matrix
            </h2>
          </div>
          <div className="overflow-x-auto">
            <table className="min-w-full text-sm">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-4 py-3 text-left font-medium">Resource</th>
                  <th className="px-4 py-3 text-left font-medium">Action</th>
                  <th className="px-4 py-3 text-left font-medium">Permission Name</th>
                  <th className="px-4 py-3 text-left font-medium">Roles</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-100">
                {permissions.map(p => {
                  const rolesWithPerm = roles.filter(r => r.permissions?.some(rp => rp.id === p.id));
                  return (
                    <tr key={p.id} className="hover:bg-gray-50">
                      <td className="px-4 py-3 capitalize text-gray-900">{p.resource}</td>
                      <td className="px-4 py-3 capitalize text-gray-600">{p.action}</td>
                      <td className="px-4 py-3 font-mono text-indigo-600">{p.name}</td>
                      <td className="px-4 py-3">
                        <div className="flex flex-wrap gap-1">
                          {rolesWithPerm.map(r => (
                            <span key={r.id} className="px-2 py-0.5 bg-gray-100 text-gray-600 rounded text-xs">{r.display_name}</span>
                          ))}
                        </div>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Field Permissions Tab */}
      {activeTab === 'fields' && (
        <div className="space-y-6">
          <div className="card p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
              <Eye className="w-5 h-5 text-indigo-600" />
              Field-Level Access Control
            </h2>
            <p className="text-sm text-gray-600 mb-4">
              Control which fields are visible or editable for each role. Hidden fields are completely masked from the user.
            </p>
            <div className="overflow-x-auto">
              <table className="min-w-full text-sm">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-4 py-3 text-left font-medium">Role</th>
                    <th className="px-4 py-3 text-left font-medium">Resource</th>
                    <th className="px-4 py-3 text-left font-medium">Field</th>
                    <th className="px-4 py-3 text-left font-medium">Access</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-100">
                  {fieldPermissions.map(fp => {
                    const level = accessLevels.find(l => l.value === fp.access_level) || accessLevels[0];
                    return (
                      <tr key={fp.id} className="hover:bg-gray-50">
                        <td className="px-4 py-3 font-medium">{roles.find(r => r.id === fp.role_id)?.display_name || fp.role_id}</td>
                        <td className="px-4 py-3 capitalize text-gray-600">{fp.resource}</td>
                        <td className="px-4 py-3 font-mono text-gray-900">{fp.field_name}</td>
                        <td className="px-4 py-3">
                          <span className={`px-2 py-1 rounded text-xs font-medium ${level.bg} ${level.color}`}>
                            {level.label}
                          </span>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
            {fieldPermissions.length === 0 && (
              <div className="text-center py-8 text-gray-500">
                <EyeOff className="w-12 h-12 mx-auto mb-3 text-gray-300" />
                <p>No field permissions configured yet</p>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Data Policies Tab */}
      {activeTab === 'policies' && (
        <div className="space-y-6">
          <div className="card p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
              <Database className="w-5 h-5 text-indigo-600" />
              Data Policies (Row-Level Access)
            </h2>
            <p className="text-sm text-gray-600 mb-4">
              Define row-level access rules. Policies determine which records a role can see based on conditions.
            </p>
            <div className="space-y-3">
              {dataPolicies.map(policy => (
                <div key={policy.id} className={`p-4 rounded-lg border ${policy.is_active ? 'bg-white border-gray-200' : 'bg-gray-50 border-gray-100'}`}>
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <div className="flex items-center gap-3">
                        <h3 className="font-semibold text-gray-900">{policy.name}</h3>
                        <span className={`px-2 py-0.5 rounded text-xs font-medium ${policy.effect === 'allow' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                          {policy.effect}
                        </span>
                        <span className="px-2 py-0.5 bg-gray-100 text-gray-600 rounded text-xs capitalize">{policy.resource}</span>
                      </div>
                      <p className="text-sm text-gray-500 mt-1">
                        Role: {roles.find(r => r.id === policy.role_id)?.display_name || policy.role_id} • Priority: {policy.priority}
                      </p>
                      {policy.condition && (
                        <div className="mt-2 p-2 bg-gray-50 rounded text-xs font-mono text-gray-600">
                          {JSON.stringify(policy.condition, null, 2)}
                        </div>
                      )}
                    </div>
                    <div className="flex items-center gap-2">
                      <button onClick={() => togglePolicy(policy.id)} className="p-2 hover:bg-gray-100 rounded-lg">
                        {policy.is_active ? <ToggleRight className="w-5 h-5 text-green-600" /> : <ToggleLeft className="w-5 h-5 text-gray-400" />}
                      </button>
                      <button onClick={() => deletePolicy(policy.id)} className="p-2 hover:bg-red-50 text-red-500 rounded-lg">
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </div>
                  </div>
                </div>
              ))}
              {dataPolicies.length === 0 && (
                <div className="text-center py-8 text-gray-500">
                  <Database className="w-12 h-12 mx-auto mb-3 text-gray-300" />
                  <p>No data policies configured yet</p>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

## File: frontend-react/src/pages/Integrations.jsx

import React, { useState, useEffect } from 'react';
import { Plug, Webhook, Plus, Trash2, Send, CheckCircle, Slack, MessageCircle, Zap } from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function Integrations() {
  const [integrations, setIntegrations] = useState([]);
  const [webhooks, setWebhooks] = useState([]);
  const [activeTab, setActiveTab] = useState('integrations');
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => {
    axios.get(`${API_URL}/api/v1/integrations/integrations`, axiosConfig).then(r => setIntegrations(r.data));
    axios.get(`${API_URL}/api/v1/integrations/webhooks`, axiosConfig).then(r => setWebhooks(r.data));
  }, []);

  const testWebhook = async (id) => {
    try {
      const res = await axios.post(`${API_URL}/api/v1/integrations/webhooks/${id}/test`, {}, axiosConfig);
      alert(`Webhook test: ${res.data.status}`);
    } catch (e) { alert('Test failed'); }
  };

  const getProviderIcon = (provider) => {
    if (provider === 'slack') return <Slack className="w-5 h-5" />;
    if (provider === 'teams') return <MessageCircle className="w-5 h-5" />;
    if (provider === 'zapier') return <Zap className="w-5 h-5" />;
    return <Plug className="w-5 h-5" />;
  };

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-900 mb-6 flex items-center gap-3">
        <Plug className="w-8 h-8 text-indigo-600" /> Integrations
      </h1>

      <div className="flex gap-1 mb-6 bg-gray-100 p-1 rounded-lg w-fit">
        {[{id:'integrations',label:'Services',icon:Plug},{id:'webhooks',label:'Webhooks',icon:Webhook}].map(t => (
          <button key={t.id} onClick={()=>setActiveTab(t.id)}
            className={`flex items-center gap-2 px-4 py-2 rounded-md font-medium transition-all ${activeTab===t.id?'bg-white text-indigo-600 shadow-sm':'text-gray-600'}`}>
            <t.icon className="w-4 h-4" />{t.label}
          </button>
        ))}
      </div>

      {activeTab === 'integrations' && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {integrations.map(i => (
            <div key={i.id} className="card p-5">
              <div className="flex items-center gap-3 mb-3">
                <div className="w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center text-indigo-600">
                  {getProviderIcon(i.provider)}
                </div>
                <div>
                  <h3 className="font-semibold text-gray-900">{i.name}</h3>
                  <p className="text-xs text-gray-500 capitalize">{i.provider}</p>
                </div>
              </div>
              <div className="flex items-center justify-between">
                <span className={`px-2 py-1 rounded-full text-xs font-medium ${i.is_active ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'}`}>
                  {i.is_active ? 'Connected' : 'Disconnected'}
                </span>
                {i.last_sync && <p className="text-xs text-gray-400">Last sync: {new Date(i.last_sync).toLocaleDateString()}</p>}
              </div>
            </div>
          ))}
          {integrations.length === 0 && (
            <div className="col-span-full text-center py-12 text-gray-500">
              <Plug className="w-12 h-12 mx-auto mb-3 text-gray-300" />
              <p>No integrations configured yet.</p>
            </div>
          )}
        </div>
      )}

      {activeTab === 'webhooks' && (
        <div className="space-y-4">
          {webhooks.map(w => (
            <div key={w.id} className="card p-5">
              <div className="flex items-center justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-3">
                    <Webhook className="w-5 h-5 text-indigo-600" />
                    <h3 className="font-semibold text-gray-900">{w.name}</h3>
                    <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${w.is_active ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'}`}>
                      {w.is_active ? 'Active' : 'Inactive'}
                    </span>
                  </div>
                  <p className="text-sm text-gray-500 font-mono mt-1 truncate">{w.url}</p>
                  <div className="flex gap-2 mt-2">
                    {w.events?.map((evt, i) => (
                      <span key={i} className="px-2 py-1 bg-gray-100 rounded text-xs text-gray-600">{evt}</span>
                    ))}
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <button onClick={() => testWebhook(w.id)} className="p-2 hover:bg-gray-100 rounded-lg text-indigo-600">
                    <Send className="w-4 h-4" />
                  </button>
                  <button className="p-2 hover:bg-red-50 text-red-500 rounded-lg">
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

## File: frontend-react/src/pages/Inventory.jsx

import React, { useState, useEffect } from 'react';
import { Package, AlertTriangle, Plus, ArrowDown, ArrowUp } from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function Inventory() {
  const [products, setProducts] = useState([]);
  const [lowStock, setLowStock] = useState([]);
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => {
    axios.get(`${API_URL}/api/v1/inventory/products`, axiosConfig).then(r => setProducts(r.data));
    axios.get(`${API_URL}/api/v1/inventory/products?low_stock=true`, axiosConfig).then(r => setLowStock(r.data));
  }, []);

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Inventory</h1>
      {lowStock.length > 0 && (
        <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-xl flex items-center gap-3">
          <AlertTriangle className="w-5 h-5 text-red-600" />
          <p className="text-sm text-red-700">{lowStock.length} products are below reorder level</p>
        </div>
      )}
      <div className="card overflow-hidden">
        <table className="min-w-full text-sm">
          <thead className="bg-gray-50"><tr>
            <th className="px-4 py-3 text-left font-medium">SKU</th>
            <th className="px-4 py-3 text-left font-medium">Product</th>
            <th className="px-4 py-3 text-left font-medium">Stock</th>
            <th className="px-4 py-3 text-left font-medium">Reorder</th>
            <th className="px-4 py-3 text-left font-medium">Price</th>
            <th className="px-4 py-3 text-left font-medium">Status</th>
          </tr></thead>
          <tbody className="divide-y">
            {products.map(p => (
              <tr key={p.id} className="hover:bg-gray-50">
                <td className="px-4 py-3 font-mono text-gray-600">{p.sku}</td>
                <td className="px-4 py-3 font-medium">{p.name}</td>
                <td className="px-4 py-3"><span className={`font-medium ${p.quantity_in_stock <= p.reorder_level ? 'text-red-600' : 'text-green-600'}`}>{p.quantity_in_stock}</span></td>
                <td className="px-4 py-3 text-gray-500">{p.reorder_level}</td>
                <td className="px-4 py-3">${Number(p.unit_price).toFixed(2)}</td>
                <td className="px-4 py-3"><span className={`px-2 py-1 rounded-full text-xs ${p.status==='active'?'bg-green-100 text-green-800':'bg-gray-100'}`}>{p.status}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

## File: frontend-react/src/pages/Workflows.jsx

import React, { useState, useEffect } from 'react';
import { Workflow, Plus, ToggleLeft, ToggleRight, Trash2, Play, GitBranch, Settings2 } from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function Workflows() {
  const [workflows, setWorkflows] = useState([]);
  const [executions, setExecutions] = useState([]);
  const [activeTab, setActiveTab] = useState('workflows');
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => {
    axios.get(`${API_URL}/api/v1/workflows/workflows`, axiosConfig).then(r => setWorkflows(r.data));
    axios.get(`${API_URL}/api/v1/workflows/executions`, axiosConfig).then(r => setExecutions(r.data));
  }, []);

  const toggleWorkflow = async (id) => {
    try {
      await axios.put(`${API_URL}/api/v1/workflows/workflows/${id}/toggle`, {}, axiosConfig);
      setWorkflows(workflows.map(w => w.id === id ? { ...w, is_active: !w.is_active } : w));
    } catch (e) { console.error(e); }
  };

  const deleteWorkflow = async (id) => {
    if (!confirm('Delete this workflow?')) return;
    try {
      await axios.delete(`${API_URL}/api/v1/workflows/workflows/${id}`, axiosConfig);
      setWorkflows(workflows.filter(w => w.id !== id));
    } catch (e) { console.error(e); }
  };

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-3xl font-bold text-gray-900 flex items-center gap-3">
          <Workflow className="w-8 h-8 text-indigo-600" /> Workflow Automation
        </h1>
        <button className="btn-primary flex items-center gap-2">
          <Plus className="w-4 h-4" /> New Workflow
        </button>
      </div>

      <div className="flex gap-1 mb-6 bg-gray-100 p-1 rounded-lg w-fit">
        {[{id:'workflows',label:'Workflows',icon:GitBranch},{id:'executions',label:'Executions',icon:Play}].map(t => (
          <button key={t.id} onClick={()=>setActiveTab(t.id)}
            className={`flex items-center gap-2 px-4 py-2 rounded-md font-medium transition-all ${activeTab===t.id?'bg-white text-indigo-600 shadow-sm':'text-gray-600'}`}>
            <t.icon className="w-4 h-4" />{t.label}
          </button>
        ))}
      </div>

      {activeTab === 'workflows' && (
        <div className="space-y-4">
          {workflows.map(w => (
            <div key={w.id} className="card p-5">
              <div className="flex items-center justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-3">
                    <h3 className="font-semibold text-gray-900">{w.name}</h3>
                    <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${w.is_active ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'}`}>
                      {w.is_active ? 'Active' : 'Inactive'}
                    </span>
                  </div>
                  <p className="text-sm text-gray-500 mt-1">{w.description}</p>
                  <div className="flex gap-2 mt-2">
                    <span className="px-2 py-1 bg-gray-100 rounded text-xs text-gray-600 capitalize">{w.entity_type}</span>
                    <span className="px-2 py-1 bg-gray-100 rounded text-xs text-gray-600 capitalize">{w.trigger_type}</span>
                    <span className="px-2 py-1 bg-gray-100 rounded text-xs text-gray-600">{w.steps?.length || 0} steps</span>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <button onClick={() => toggleWorkflow(w.id)} className="p-2 hover:bg-gray-100 rounded-lg">
                    {w.is_active ? <ToggleRight className="w-6 h-6 text-green-600" /> : <ToggleLeft className="w-6 h-6 text-gray-400" />}
                  </button>
                  <button onClick={() => deleteWorkflow(w.id)} className="p-2 hover:bg-red-50 text-red-500 rounded-lg">
                    <Trash2 className="w-5 h-5" />
                  </button>
                </div>
              </div>
            </div>
          ))}
          {workflows.length === 0 && (
            <div className="text-center py-12 text-gray-500">
              <Workflow className="w-12 h-12 mx-auto mb-3 text-gray-300" />
              <p>No workflows yet. Create your first automation.</p>
            </div>
          )}
        </div>
      )}

      {activeTab === 'executions' && (
        <div className="card overflow-hidden">
          <table className="min-w-full text-sm">
            <thead className="bg-gray-50"><tr>
              <th className="px-4 py-3 text-left font-medium">Workflow</th>
              <th className="px-4 py-3 text-left font-medium">Entity</th>
              <th className="px-4 py-3 text-left font-medium">Status</th>
              <th className="px-4 py-3 text-left font-medium">Step</th>
              <th className="px-4 py-3 text-left font-medium">Started</th>
            </tr></thead>
            <tbody className="divide-y">
              {executions.map(e => (
                <tr key={e.id} className="hover:bg-gray-50">
                  <td className="px-4 py-3 font-medium">{e.workflow?.name || e.workflow_id}</td>
                  <td className="px-4 py-3 text-gray-600">{e.entity_type} #{e.entity_id}</td>
                  <td className="px-4 py-3">
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${e.status === 'completed' ? 'bg-green-100 text-green-800' : e.status === 'failed' ? 'bg-red-100 text-red-800' : 'bg-blue-100 text-blue-800'}`}>
                      {e.status}
                    </span>
                  </td>
                  <td className="px-4 py-3 text-gray-600">Step {e.current_step}</td>
                  <td className="px-4 py-3 text-gray-500">{e.started_at ? new Date(e.started_at).toLocaleString() : '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

## File: frontend-react/src/pages/Projects.jsx

import React, { useState, useEffect } from 'react';
import { FolderKanban, CheckCircle, Clock, AlertCircle, Plus, Calendar, BarChart3 } from 'lucide-react';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function Projects() {
  const [projects, setProjects] = useState([]);
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  useEffect(() => {
    axios.get(`${API_URL}/api/v1/projects/projects`, axiosConfig).then(r => setProjects(r.data));
  }, []);

  const statusColors = {
    planning: 'bg-gray-100 text-gray-800',
    active: 'bg-blue-100 text-blue-800',
    on_hold: 'bg-amber-100 text-amber-800',
    completed: 'bg-green-100 text-green-800',
    cancelled: 'bg-red-100 text-red-800',
  };

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-3xl font-bold text-gray-900">Projects</h1>
        <button className="btn-primary flex items-center gap-2"><Plus className="w-4 h-4" /> New Project</button>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {projects.map(p => (
          <div key={p.id} className="card p-5">
            <div className="flex items-start justify-between mb-3">
              <h3 className="font-semibold text-gray-900">{p.name}</h3>
              <span className={`px-2 py-1 rounded-full text-xs font-medium ${statusColors[p.status] || 'bg-gray-100'}`}>{p.status}</span>
            </div>
            <p className="text-sm text-gray-500 mb-4 line-clamp-2">{p.description}</p>
            <div className="flex items-center gap-4 text-sm text-gray-500 mb-3">
              <div className="flex items-center gap-1"><Calendar className="w-4 h-4" />{p.start_date || 'No date'}</div>
              <div className="flex items-center gap-1"><BarChart3 className="w-4 h-4" />{p.priority}</div>
            </div>
            {p.budget && <p className="text-sm font-medium text-gray-900">Budget: ${Number(p.budget).toLocaleString()}</p>}
            <div className="mt-3">
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div className="bg-indigo-600 h-2 rounded-full" style={{width: `${p.progress || 0}%`}}></div>
              </div>
              <p className="text-xs text-gray-500 mt-1">{p.progress || 0}% complete</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

## File: frontend-react/src/pages/Dashboard.jsx

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import {
  Users, Building2, Package, Receipt, FolderKanban,
  TrendingUp, TrendingDown, AlertTriangle, Activity,
  DollarSign, BarChart3, ArrowUpRight, ArrowDownRight,
  Sparkles, Zap, Clock, Target, Percent
} from 'lucide-react';
import { LineChartComponent, BarChartComponent, AreaChartComponent, Sparkline } from '../components/Charts.jsx';
import { SkeletonStats } from '../components/Skeleton.jsx';
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const statCards = [
  { label: 'Contacts', icon: Users, color: 'bg-blue-500', path: '/crm', key: 'total_contacts', trend: 'contacts_trend' },
  { label: 'Companies', icon: Building2, color: 'bg-indigo-500', path: '/crm', key: 'total_companies' },
  { label: 'Products', icon: Package, color: 'bg-emerald-500', path: '/inventory', key: 'total_products', trend: 'products_trend' },
  { label: 'Revenue', icon: DollarSign, color: 'bg-amber-500', path: '/finance', key: 'total_revenue', format: 'currency', trend: 'revenue_trend' },
];

export default function Dashboard() {
  const [stats, setStats] = useState({});
  const [loading, setLoading] = useState(true);
  const [revenueData, setRevenueData] = useState([]);
  const [pipelineData, setPipelineData] = useState([]);
  const [activityData, setActivityData] = useState([]);
  const token = localStorage.getItem('token');

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      const [analytics, crm, hr, inventory, finance, projects, trends] = await Promise.all([
        axios.get(`${API_URL}/api/v1/analytics/dashboard`, { headers: { Authorization: `Bearer ${token}` } }).catch(() => ({ data: {} })),
        axios.get(`${API_URL}/api/v1/crm/dashboard`, { headers: { Authorization: `Bearer ${token}` } }).catch(() => ({ data: {} })),
        axios.get(`${API_URL}/api/v1/hr/dashboard`, { headers: { Authorization: `Bearer ${token}` } }).catch(() => ({ data: {} })),
        axios.get(`${API_URL}/api/v1/inventory/dashboard`, { headers: { Authorization: `Bearer ${token}` } }).catch(() => ({ data: {} })),
        axios.get(`${API_URL}/api/v1/finance/dashboard`, { headers: { Authorization: `Bearer ${token}` } }).catch(() => ({ data: {} })),
        axios.get(`${API_URL}/api/v1/projects/dashboard`, { headers: { Authorization: `Bearer ${token}` } }).catch(() => ({ data: {} })),
        axios.get(`${API_URL}/api/v1/analytics/monthly-trends`, { headers: { Authorization: `Bearer ${token}` } }).catch(() => ({ data: {} })),
      ]);

      setStats({
        ...analytics.data,
        ...crm.data,
        ...hr.data,
        ...inventory.data,
        ...finance.data,
        ...projects.data,
      });

      // Build chart data
      const monthlyRevenue = trends.data?.revenue?.map(r => ({
        month: r.period,
        revenue: r.amount
      })) || [];
      setRevenueData(monthlyRevenue);

      const pipeline = analytics.data?.crm?.pipeline_value || 0;
      setPipelineData([
        { name: 'Pipeline', value: pipeline, fill: '#4f46e5' },
        { name: 'Won', value: crm.data?.won_deals || 0, fill: '#10b981' },
        { name: 'Lost', value: (crm.data?.total_deals || 0) - (crm.data?.won_deals || 0), fill: '#ef4444' },
      ]);

      const activity = analytics.data?.recent_activity?.slice(0, 7).map((a, i) => ({
        day: `Day ${i + 1}`,
        actions: 1
      })) || [];
      setActivityData(activity);

    } catch (e) { console.error('Dashboard fetch error:', e); }
    finally { setLoading(false); }
  };

  const formatValue = (value, format) => {
    if (value === undefined || value === null) return '—';
    if (format === 'currency') return `$${Number(value).toLocaleString()}`;
    return Number(value).toLocaleString();
  };

  const trendData = [
    { day: 1, value: 120 }, { day: 2, value: 132 }, { day: 3, value: 101 },
    { day: 4, value: 134 }, { day: 5, value: 90 }, { day: 6, value: 230 }, { day: 7, value: 210 }
  ];

  return (
    <div className="p-6 lg:p-8 max-w-7xl mx-auto animate-in fade-in duration-500">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center gap-3 mb-2">
          <h1 className="text-3xl font-bold text-[var(--color-text)]">Dashboard</h1>
          <span className="px-2.5 py-0.5 bg-indigo-100 dark:bg-indigo-900/30 text-indigo-700 dark:text-indigo-300 rounded-full text-xs font-medium">
            v2.2 PRO MAX
          </span>
        </div>
        <p className="text-[var(--color-text-secondary)]">Overview of your business operations</p>
      </div>

      {/* Stats Grid */}
      {loading ? <SkeletonStats count={4} /> : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
          {statCards.map((card) => (
            <Link
              key={card.label}
              to={card.path}
              className="card p-6 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-300 group"
            >
              <div className="flex items-center justify-between mb-4">
                <div>
                  <p className="text-sm font-medium text-[var(--color-text-secondary)]">{card.label}</p>
                  <p className="text-2xl font-bold text-[var(--color-text)] mt-1">
                    {formatValue(stats[card.key], card.format)}
                  </p>
                </div>
                <div className={`${card.color} p-3 rounded-xl group-hover:scale-110 transition-transform duration-300`}>
                  <card.icon className="w-5 h-5 text-white" />
                </div>
              </div>
              {card.trend && (
                <div className="flex items-center gap-2">
                  <Sparkline data={trendData} dataKey="value" color={card.color.replace('bg-', '#').replace('500', '600')} />
                  <span className="text-xs text-green-600 dark:text-green-400 flex items-center gap-0.5">
                    <TrendingUp className="w-3 h-3" /> +12%
                  </span>
                </div>
              )}
            </Link>
          ))}
        </div>
      )}

      {/* Charts Row */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
        {/* Revenue Chart */}
        <div className="card p-6 lg:col-span-2">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-lg font-semibold text-[var(--color-text)] flex items-center gap-2">
              <BarChart3 className="w-5 h-5 text-indigo-600 dark:text-indigo-400" />
              Revenue Trends
            </h2>
            <Link to="/analytics" className="text-sm text-indigo-600 dark:text-indigo-400 hover:underline flex items-center gap-1">
              View All <ArrowUpRight className="w-4 h-4" />
            </Link>
          </div>
          {revenueData.length > 0 ? (
            <AreaChartComponent data={revenueData} xKey="month" yKey="revenue" height={280} />
          ) : (
            <div className="h-[280px] flex items-center justify-center text-[var(--color-text-secondary)]">
              <Activity className="w-8 h-8 mr-2" /> No revenue data yet
            </div>
          )}
        </div>

        {/* Quick Insights */}
        <div className="card p-6">
          <h2 className="text-lg font-semibold text-[var(--color-text)] mb-4 flex items-center gap-2">
            <Zap className="w-5 h-5 text-amber-500" />
            Quick Insights
          </h2>
          <div className="space-y-4">
            <div className="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-800/50 rounded-lg">
              <div className="w-10 h-10 bg-blue-100 dark:bg-blue-900/30 rounded-lg flex items-center justify-center">
                <Target className="w-5 h-5 text-blue-600 dark:text-blue-400" />
              </div>
              <div>
                <p className="text-sm font-medium text-[var(--color-text)]">Conversion Rate</p>
                <p className="text-lg font-bold text-[var(--color-text)]">
                  {stats.conversion_rate ? `${stats.conversion_rate.toFixed(1)}%` : '—'}
                </p>
              </div>
            </div>
            <div className="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-800/50 rounded-lg">
              <div className="w-10 h-10 bg-emerald-100 dark:bg-emerald-900/30 rounded-lg flex items-center justify-center">
                <Percent className="w-5 h-5 text-emerald-600 dark:text-emerald-400" />
              </div>
              <div>
                <p className="text-sm font-medium text-[var(--color-text)]">Collection Rate</p>
                <p className="text-lg font-bold text-[var(--color-text)]">
                  {stats.revenue?.collection_rate ? `${stats.revenue.collection_rate.toFixed(1)}%` : '—'}
                </p>
              </div>
            </div>
            <div className="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-800/50 rounded-lg">
              <div className="w-10 h-10 bg-purple-100 dark:bg-purple-900/30 rounded-lg flex items-center justify-center">
                <Clock className="w-5 h-5 text-purple-600 dark:text-purple-400" />
              </div>
              <div>
                <p className="text-sm font-medium text-[var(--color-text)]">Avg Task Completion</p>
                <p className="text-lg font-bold text-[var(--color-text)]">
                  {stats.projects?.completion_rate ? `${stats.projects.completion_rate.toFixed(1)}%` : '—'}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Alerts & Activity */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Alerts */}
        <div className="card p-6">
          <h2 className="text-lg font-semibold text-[var(--color-text)] mb-4 flex items-center gap-2">
            <AlertTriangle className="w-5 h-5 text-amber-500" />
            Alerts
          </h2>
          <div className="space-y-3">
            {(stats.low_stock || 0) > 0 && (
              <div className="flex items-center gap-3 p-3 bg-red-50 dark:bg-red-900/20 rounded-lg border border-red-100 dark:border-red-800/30">
                <Package className="w-5 h-5 text-red-600 dark:text-red-400" />
                <div className="flex-1">
                  <p className="text-sm font-medium text-red-800 dark:text-red-300">{stats.low_stock} products low on stock</p>
                  <Link to="/inventory" className="text-xs text-red-600 dark:text-red-400 hover:underline">View inventory →</Link>
                </div>
              </div>
            )}
            {(stats.overdue_count || 0) > 0 && (
              <div className="flex items-center gap-3 p-3 bg-amber-50 dark:bg-amber-900/20 rounded-lg border border-amber-100 dark:border-amber-800/30">
                <Receipt className="w-5 h-5 text-amber-600 dark:text-amber-400" />
                <div className="flex-1">
                  <p className="text-sm font-medium text-amber-800 dark:text-amber-300">{stats.overdue_count} overdue invoices</p>
                  <Link to="/finance" className="text-xs text-amber-600 dark:text-amber-400 hover:underline">View finance →</Link>
                </div>
              </div>
            )}
            {(stats.overdue_tasks || 0) > 0 && (
              <div className="flex items-center gap-3 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-100 dark:border-blue-800/30">
                <FolderKanban className="w-5 h-5 text-blue-600 dark:text-blue-400" />
                <div className="flex-1">
                  <p className="text-sm font-medium text-blue-800 dark:text-blue-300">{stats.overdue_tasks} overdue tasks</p>
                  <Link to="/projects" className="text-xs text-blue-600 dark:text-blue-400 hover:underline">View projects →</Link>
                </div>
              </div>
            )}
            {(!stats.low_stock && !stats.overdue_count && !stats.overdue_tasks) && (
              <div className="text-center py-8 text-[var(--color-text-secondary)]">
                <Activity className="w-8 h-8 mx-auto mb-2 text-gray-300 dark:text-gray-600" />
                <p className="text-sm">No alerts at this time</p>
              </div>
            )}
          </div>
        </div>

        {/* Activity Feed */}
        <div className="card p-6 lg:col-span-2">
          <h2 className="text-lg font-semibold text-[var(--color-text)] mb-4 flex items-center gap-2">
            <Activity className="w-5 h-5 text-indigo-600 dark:text-indigo-400" />
            Recent Activity
          </h2>
          <div className="space-y-3">
            {(stats.recent_activity || []).slice(0, 8).map((activity, i) => (
              <div key={i} className="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-800/50 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors">
                <div className="w-2 h-2 bg-indigo-500 rounded-full flex-shrink-0" />
                <div className="flex-1 min-w-0">
                  <p className="text-sm text-[var(--color-text)] capitalize">{activity.action.replace(/_/g, ' ')}</p>
                  <p className="text-xs text-[var(--color-text-secondary)]">{activity.entity_type} • {activity.created_at ? new Date(activity.created_at).toLocaleString() : ''}</p>
                </div>
              </div>
            ))}
            {(!stats.recent_activity || stats.recent_activity.length === 0) && (
              <p className="text-sm text-[var(--color-text-secondary)] text-center py-4">No recent activity</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

## File: frontend-react/src/pages/Documents.jsx

import React, { useState, useEffect, useCallback } from 'react';
import { FileText, Upload, Trash2, Download, Search, File, Image, FileSpreadsheet } from 'lucide-react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function Documents() {
  const [documents, setDocuments] = useState([]);
  const [loading, setLoading] = useState(false);
  const token = localStorage.getItem('token');
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  const onDrop = useCallback(async (acceptedFiles) => {
    for (const file of acceptedFiles) {
      const formData = new FormData();
      formData.append('file', file);
      formData.append('title', file.name);
      try {
        await axios.post(`${API_URL}/api/v1/documents/upload`, formData, {
          headers: { ...axiosConfig.headers, 'Content-Type': 'multipart/form-data' }
        });
      } catch (e) { console.error(e); }
    }
    fetchDocuments();
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { 'application/*': [], 'image/*': [], 'text/*': [] }
  });

  const fetchDocuments = async () => {
    try {
      const res = await axios.get(`${API_URL}/api/v1/documents/documents`, axiosConfig);
      setDocuments(res.data);
    } catch (e) { console.error(e); }
  };

  useEffect(() => { fetchDocuments(); }, []);

  const deleteDoc = async (id) => {
    if (!confirm('Delete this document?')) return;
    try {
      await axios.delete(`${API_URL}/api/v1/documents/documents/${id}`, axiosConfig);
      fetchDocuments();
    } catch (e) { console.error(e); }
  };

  const getFileIcon = (mimeType) => {
    if (mimeType?.includes('image')) return <Image className="w-5 h-5 text-purple-600" />;
    if (mimeType?.includes('spreadsheet') || mimeType?.includes('excel')) return <FileSpreadsheet className="w-5 h-5 text-green-600" />;
    return <FileText className="w-5 h-5 text-indigo-600" />;
  };

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Documents</h1>
      <div {...getRootProps()} className={`border-2 border-dashed rounded-xl p-8 text-center cursor-pointer mb-6 transition-all ${isDragActive ? 'border-indigo-500 bg-indigo-50' : 'border-gray-300 hover:border-gray-400'}`}>
        <input {...getInputProps()} />
        <Upload className="w-10 h-10 text-gray-400 mx-auto mb-2" />
        <p className="text-gray-600">{isDragActive ? 'Drop files here' : 'Drag & drop files or click to browse'}</p>
        <p className="text-sm text-gray-400 mt-1">PDF, Word, Excel, Images, and more</p>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {documents.map(doc => (
          <div key={doc.id} className="card p-4">
            <div className="flex items-start justify-between">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center">
                  {getFileIcon(doc.mime_type)}
                </div>
                <div>
                  <p className="font-medium text-gray-900 truncate max-w-[200px]">{doc.title}</p>
                  <p className="text-xs text-gray-500">{(doc.file_size / 1024).toFixed(1)} KB</p>
                </div>
              </div>
              <button onClick={() => deleteDoc(doc.id)} className="p-1.5 text-red-500 hover:bg-red-50 rounded-lg">
                <Trash2 className="w-4 h-4" />
              </button>
            </div>
            <p className="text-xs text-gray-400 mt-2">{doc.mime_type}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

## File: frontend-react/src/contexts/ToastContext.jsx

import React, { createContext, useContext, useState, useCallback } from 'react';
import { X, CheckCircle, AlertTriangle, Info, AlertCircle } from 'lucide-react';

const ToastContext = createContext(null);

const icons = {
  success: CheckCircle,
  error: AlertCircle,
  warning: AlertTriangle,
  info: Info,
};

const styles = {
  success: 'bg-green-50 dark:bg-green-900/20 border-green-200 dark:border-green-800 text-green-800 dark:text-green-200',
  error: 'bg-red-50 dark:bg-red-900/20 border-red-200 dark:border-red-800 text-red-800 dark:text-red-200',
  warning: 'bg-amber-50 dark:bg-amber-900/20 border-amber-200 dark:border-amber-800 text-amber-800 dark:text-amber-200',
  info: 'bg-blue-50 dark:bg-blue-900/20 border-blue-200 dark:border-blue-800 text-blue-800 dark:text-blue-200',
};

export function ToastProvider({ children }) {
  const [toasts, setToasts] = useState([]);

  const addToast = useCallback((message, type = 'info', duration = 4000) => {
    const id = Date.now() + Math.random();
    setToasts(prev => [...prev, { id, message, type, duration }]);
    if (duration > 0) {
      setTimeout(() => removeToast(id), duration);
    }
  }, []);

  const removeToast = useCallback((id) => {
    setToasts(prev => prev.filter(t => t.id !== id));
  }, []);

  return (
    <ToastContext.Provider value={{ addToast, removeToast }}>
      {children}
      <div className="fixed bottom-4 right-4 z-50 flex flex-col gap-2 max-w-sm">
        {toasts.map(toast => {
          const Icon = icons[toast.type];
          return (
            <div
              key={toast.id}
              className={`flex items-start gap-3 p-4 rounded-xl border shadow-lg animate-in slide-in-from-right-full fade-in duration-300 ${styles[toast.type]}`}
            >
              <Icon className="w-5 h-5 flex-shrink-0 mt-0.5" />
              <p className="text-sm flex-1">{toast.message}</p>
              <button onClick={() => removeToast(toast.id)} className="p-1 hover:bg-black/5 rounded">
                <X className="w-4 h-4" />
              </button>
            </div>
          );
        })}
      </div>
    </ToastContext.Provider>
  );
}

export function useToast() {
  const context = useContext(ToastContext);
  if (!context) throw new Error('useToast must be used within ToastProvider');
  return context;
}

## File: frontend-react/src/contexts/ThemeContext.jsx

import React, { createContext, useContext, useState, useEffect } from 'react';

const ThemeContext = createContext(null);

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState(() => {
    const saved = localStorage.getItem('theme');
    if (saved) return saved;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  });

  useEffect(() => {
    const root = document.documentElement;
    root.classList.remove('light', 'dark');
    root.classList.add(theme);
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = () => setTheme(prev => prev === 'light' ? 'dark' : 'light');

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme, isDark: theme === 'dark' }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) throw new Error('useTheme must be used within ThemeProvider');
  return context;
}

## File: frontend-react/src/components/Charts.jsx

import React from 'react';
import {
  LineChart, Line, BarChart, Bar, PieChart, Pie, Cell,
  AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip,
  Legend, ResponsiveContainer, RadarChart, Radar, PolarGrid,
  PolarAngleAxis, PolarRadiusAxis
} from 'recharts';

const COLORS = ['#4f46e5', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#06b6d4', '#f97316', '#84cc16'];

export function LineChartComponent({ data, xKey, yKey, height = 300, color = '#4f46e5' }) {
  return (
    <ResponsiveContainer width="100%" height={height}>
      <LineChart data={data} margin={{ top: 5, right: 20, left: 10, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="var(--color-border)" />
        <XAxis dataKey={xKey} tick={{ fill: 'var(--color-text-secondary)', fontSize: 12 }} />
        <YAxis tick={{ fill: 'var(--color-text-secondary)', fontSize: 12 }} />
        <Tooltip
          contentStyle={{
            backgroundColor: 'var(--color-card)',
            border: '1px solid var(--color-border)',
            borderRadius: '8px',
            color: 'var(--color-text)'
          }}
        />
        <Line type="monotone" dataKey={yKey} stroke={color} strokeWidth={2} dot={{ fill: color }} />
      </LineChart>
    </ResponsiveContainer>
  );
}

export function BarChartComponent({ data, xKey, yKey, height = 300, color = '#4f46e5' }) {
  return (
    <ResponsiveContainer width="100%" height={height}>
      <BarChart data={data} margin={{ top: 5, right: 20, left: 10, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="var(--color-border)" />
        <XAxis dataKey={xKey} tick={{ fill: 'var(--color-text-secondary)', fontSize: 12 }} />
        <YAxis tick={{ fill: 'var(--color-text-secondary)', fontSize: 12 }} />
        <Tooltip
          contentStyle={{
            backgroundColor: 'var(--color-card)',
            border: '1px solid var(--color-border)',
            borderRadius: '8px',
            color: 'var(--color-text)'
          }}
        />
        <Bar dataKey={yKey} fill={color} radius={[4, 4, 0, 0]} />
      </BarChart>
    </ResponsiveContainer>
  );
}

export function PieChartComponent({ data, nameKey, valueKey, height = 300 }) {
  return (
    <ResponsiveContainer width="100%" height={height}>
      <PieChart>
        <Pie
          data={data}
          cx="50%"
          cy="50%"
          innerRadius={60}
          outerRadius={100}
          paddingAngle={5}
          dataKey={valueKey}
          nameKey={nameKey}
        >
          {data.map((_, index) => (
            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
          ))}
        </Pie>
        <Tooltip
          contentStyle={{
            backgroundColor: 'var(--color-card)',
            border: '1px solid var(--color-border)',
            borderRadius: '8px',
            color: 'var(--color-text)'
          }}
        />
        <Legend />
      </PieChart>
    </ResponsiveContainer>
  );
}

export function AreaChartComponent({ data, xKey, yKey, height = 300, color = '#4f46e5' }) {
  return (
    <ResponsiveContainer width="100%" height={height}>
      <AreaChart data={data} margin={{ top: 5, right: 20, left: 10, bottom: 5 }}>
        <defs>
          <linearGradient id={`gradient-${yKey}`} x1="0" y1="0" x2="0" y2="1">
            <stop offset="5%" stopColor={color} stopOpacity={0.3} />
            <stop offset="95%" stopColor={color} stopOpacity={0} />
          </linearGradient>
        </defs>
        <CartesianGrid strokeDasharray="3 3" stroke="var(--color-border)" />
        <XAxis dataKey={xKey} tick={{ fill: 'var(--color-text-secondary)', fontSize: 12 }} />
        <YAxis tick={{ fill: 'var(--color-text-secondary)', fontSize: 12 }} />
        <Tooltip
          contentStyle={{
            backgroundColor: 'var(--color-card)',
            border: '1px solid var(--color-border)',
            borderRadius: '8px',
            color: 'var(--color-text)'
          }}
        />
        <Area type="monotone" dataKey={yKey} stroke={color} fill={`url(#gradient-${yKey})`} strokeWidth={2} />
      </AreaChart>
    </ResponsiveContainer>
  );
}

export function Sparkline({ data, dataKey, width = 120, height = 40, color = '#4f46e5' }) {
  return (
    <ResponsiveContainer width={width} height={height}>
      <LineChart data={data}>
        <Line type="monotone" dataKey={dataKey} stroke={color} strokeWidth={2} dot={false} />
      </LineChart>
    </ResponsiveContainer>
  );
}

## File: frontend-react/src/components/Skeleton.jsx

import React from 'react';

export function Skeleton({ className = '', count = 1, width, height, circle = false }) {
  const items = Array.from({ length: count }, (_, i) => (
    <div
      key={i}
      className={`animate-pulse bg-gray-200 dark:bg-gray-700 rounded ${circle ? 'rounded-full' : ''} ${className}`}
      style={{ width, height }}
    />
  ));
  return count === 1 ? items[0] : <div className="space-y-2">{items}</div>;
}

export function SkeletonCard({ className = '' }) {
  return (
    <div className={`card p-5 space-y-4 ${className}`}>
      <div className="flex items-center gap-4">
        <Skeleton width={40} height={40} circle />
        <div className="flex-1 space-y-2">
          <Skeleton width="60%" height={20} />
          <Skeleton width="40%" height={14} />
        </div>
      </div>
      <Skeleton width="100%" height={60} />
      <div className="flex gap-2">
        <Skeleton width={80} height={28} />
        <Skeleton width={80} height={28} />
      </div>
    </div>
  );
}

export function SkeletonTable({ rows = 5, columns = 4 }) {
  return (
    <div className="card overflow-hidden">
      <div className="bg-gray-50 dark:bg-gray-800 px-4 py-3 flex gap-4">
        {Array.from({ length: columns }).map((_, i) => (
          <Skeleton key={i} width={`${100 / columns}%`} height={16} />
        ))}
      </div>
      <div className="divide-y divide-gray-100 dark:divide-gray-800">
        {Array.from({ length: rows }).map((_, i) => (
          <div key={i} className="px-4 py-4 flex gap-4">
            {Array.from({ length: columns }).map((_, j) => (
              <Skeleton key={j} width={`${100 / columns}%`} height={16} />
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}

export function SkeletonStats({ count = 4 }) {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      {Array.from({ length: count }).map((_, i) => (
        <div key={i} className="card p-6 space-y-3">
          <div className="flex items-center justify-between">
            <Skeleton width={100} height={14} />
            <Skeleton width={40} height={40} circle />
          </div>
          <Skeleton width="50%" height={32} />
        </div>
      ))}
    </div>
  );
}

export function SkeletonChat() {
  return (
    <div className="space-y-4">
      <div className="flex gap-3">
        <Skeleton width={32} height={32} circle />
        <div className="flex-1 max-w-[80%] space-y-2">
          <Skeleton width="100%" height={60} />
        </div>
      </div>
      <div className="flex gap-3 justify-end">
        <div className="flex-1 max-w-[80%] space-y-2">
          <Skeleton width="100%" height={40} />
        </div>
        <Skeleton width={32} height={32} circle />
      </div>
      <div className="flex gap-3">
        <Skeleton width={32} height={32} circle />
        <div className="flex-1 max-w-[80%] space-y-2">
          <Skeleton width="100%" height={80} />
        </div>
      </div>
    </div>
  );
}

## File: frontend-react/src/components/DataTable.jsx

import React, { useState, useMemo } from 'react';
import { ArrowUpDown, ArrowUp, ArrowDown, ChevronLeft, ChevronRight, Search, SlidersHorizontal, Download } from 'lucide-react';

export default function DataTable({
  data = [],
  columns = [],
  keyField = 'id',
  searchable = true,
  sortable = true,
  paginate = true,
  pageSize = 10,
  exportable = true,
  onRowClick,
  emptyMessage = 'No data available',
  loading = false,
  actions,
}) {
  const [searchQuery, setSearchQuery] = useState('');
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });
  const [currentPage, setCurrentPage] = useState(1);
  const [showFilters, setShowFilters] = useState(false);
  const [filters, setFilters] = useState({});

  // Filter and sort data
  const processedData = useMemo(() => {
    let result = [...data];

    // Apply search
    if (searchQuery) {
      const q = searchQuery.toLowerCase();
      result = result.filter(row =>
        columns.some(col => {
          const val = getValue(row, col.key);
          return val != null && String(val).toLowerCase().includes(q);
        })
      );
    }

    // Apply column filters
    Object.entries(filters).forEach(([key, filterVal]) => {
      if (filterVal) {
        result = result.filter(row => {
          const val = getValue(row, key);
          return String(val).toLowerCase().includes(filterVal.toLowerCase());
        });
      }
    });

    // Apply sorting
    if (sortConfig.key) {
      result.sort((a, b) => {
        const aVal = getValue(a, sortConfig.key);
        const bVal = getValue(b, sortConfig.key);
        if (aVal == null) return 1;
        if (bVal == null) return -1;
        if (typeof aVal === 'number' && typeof bVal === 'number') {
          return sortConfig.direction === 'asc' ? aVal - bVal : bVal - aVal;
        }
        return sortConfig.direction === 'asc'
          ? String(aVal).localeCompare(String(bVal))
          : String(bVal).localeCompare(String(aVal));
      });
    }

    return result;
  }, [data, searchQuery, filters, sortConfig, columns]);

  // Pagination
  const totalPages = Math.ceil(processedData.length / pageSize);
  const paginatedData = paginate
    ? processedData.slice((currentPage - 1) * pageSize, currentPage * pageSize)
    : processedData;

  const handleSort = (key) => {
    if (!sortable) return;
    setSortConfig(prev => ({
      key,
      direction: prev.key === key && prev.direction === 'asc' ? 'desc' : 'asc'
    }));
  };

  const handleExport = () => {
    const headers = columns.map(c => c.label || c.key).join(',');
    const rows = processedData.map(row =>
      columns.map(col => {
        const val = getValue(row, col.key);
        return val != null ? `"${String(val).replace(/"/g, '""')}"` : '';
      }).join(',')
    ).join('\n');
    const csv = `${headers}\n${rows}`;
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `export_${new Date().toISOString().slice(0, 10)}.csv`;
    a.click();
    URL.revokeObjectURL(url);
  };

  if (loading) {
    return (
      <div className="card overflow-hidden">
        <div className="px-4 py-3 bg-gray-50 dark:bg-gray-800 flex gap-4">
          {columns.map((_, i) => (
            <div key={i} className="animate-pulse bg-gray-200 dark:bg-gray-700 rounded h-4 flex-1" />
          ))}
        </div>
        <div className="divide-y divide-gray-100 dark:divide-gray-800">
          {Array.from({ length: 5 }).map((_, i) => (
            <div key={i} className="px-4 py-4 flex gap-4">
              {columns.map((_, j) => (
                <div key={j} className="animate-pulse bg-gray-200 dark:bg-gray-700 rounded h-4 flex-1" />
              ))}
            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {/* Toolbar */}
      <div className="flex items-center gap-3 flex-wrap">
        {searchable && (
          <div className="relative flex-1 min-w-[200px]">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={e => { setSearchQuery(e.target.value); setCurrentPage(1); }}
              placeholder="Search..."
              className="w-full pl-9 pr-4 py-2 text-sm border border-gray-200 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none"
            />
          </div>
        )}
        <button
          onClick={() => setShowFilters(!showFilters)}
          className={`flex items-center gap-2 px-3 py-2 text-sm border rounded-lg transition-colors ${
            showFilters
              ? 'border-indigo-300 bg-indigo-50 text-indigo-700 dark:border-indigo-700 dark:bg-indigo-900/20 dark:text-indigo-300'
              : 'border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800'
          }`}
        >
          <SlidersHorizontal className="w-4 h-4" /> Filters
        </button>
        {exportable && (
          <button
            onClick={handleExport}
            className="flex items-center gap-2 px-3 py-2 text-sm border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-400 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
          >
            <Download className="w-4 h-4" /> Export
          </button>
        )}
        {actions}
        <span className="text-sm text-gray-500 dark:text-gray-400 ml-auto">
          {processedData.length} {processedData.length === 1 ? 'item' : 'items'}
        </span>
      </div>

      {/* Column Filters */}
      {showFilters && (
        <div className="flex flex-wrap gap-2 p-3 bg-gray-50 dark:bg-gray-800/50 rounded-lg">
          {columns.filter(c => c.filterable !== false).map(col => (
            <div key={col.key} className="flex items-center gap-2">
              <span className="text-xs text-gray-500 dark:text-gray-400">{col.label || col.key}:</span>
              <input
                type="text"
                value={filters[col.key] || ''}
                onChange={e => setFilters(prev => ({ ...prev, [col.key]: e.target.value }))}
                placeholder="Filter..."
                className="px-2 py-1 text-xs border border-gray-200 dark:border-gray-700 rounded bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 outline-none focus:ring-1 focus:ring-indigo-500"
              />
            </div>
          ))}
        </div>
      )}

      {/* Table */}
      <div className="card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="min-w-full text-sm">
            <thead className="bg-gray-50 dark:bg-gray-800">
              <tr>
                {columns.map(col => (
                  <th
                    key={col.key}
                    onClick={() => handleSort(col.key)}
                    className={`px-4 py-3 text-left font-medium text-gray-700 dark:text-gray-300 ${
                      sortable && col.sortable !== false ? 'cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-700 select-none' : ''
                    }`}
                  >
                    <div className="flex items-center gap-1">
                      {col.label || col.key}
                      {sortable && col.sortable !== false && (
                        sortConfig.key === col.key ? (
                          sortConfig.direction === 'asc' ? <ArrowUp className="w-3 h-3 text-indigo-600" /> : <ArrowDown className="w-3 h-3 text-indigo-600" />
                        ) : <ArrowUpDown className="w-3 h-3 text-gray-400" />
                      )}
                    </div>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100 dark:divide-gray-800">
              {paginatedData.length === 0 ? (
                <tr>
                  <td colSpan={columns.length} className="px-4 py-12 text-center text-gray-500 dark:text-gray-400">
                    {emptyMessage}
                  </td>
                </tr>
              ) : (
                paginatedData.map((row, i) => (
                  <tr
                    key={getValue(row, keyField) || i}
                    onClick={() => onRowClick?.(row)}
                    className={`hover:bg-gray-50 dark:hover:bg-gray-800/50 transition-colors ${onRowClick ? 'cursor-pointer' : ''}`}
                  >
                    {columns.map(col => (
                      <td key={col.key} className="px-4 py-3 text-gray-900 dark:text-gray-100">
                        {col.render ? col.render(row) : formatValue(getValue(row, col.key))}
                      </td>
                    ))}
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Pagination */}
      {paginate && totalPages > 1 && (
        <div className="flex items-center justify-between">
          <span className="text-sm text-gray-500 dark:text-gray-400">
            Showing {(currentPage - 1) * pageSize + 1} to {Math.min(currentPage * pageSize, processedData.length)} of {processedData.length}
          </span>
          <div className="flex items-center gap-1">
            <button
              onClick={() => setCurrentPage(p => Math.max(1, p - 1))}
              disabled={currentPage === 1}
              className="p-2 border border-gray-200 dark:border-gray-700 rounded-lg disabled:opacity-50 hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-600 dark:text-gray-400"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
            {Array.from({ length: Math.min(5, totalPages) }, (_, i) => {
              let pageNum;
              if (totalPages <= 5) pageNum = i + 1;
              else if (currentPage <= 3) pageNum = i + 1;
              else if (currentPage >= totalPages - 2) pageNum = totalPages - 4 + i;
              else pageNum = currentPage - 2 + i;
              return (
                <button
                  key={pageNum}
                  onClick={() => setCurrentPage(pageNum)}
                  className={`w-9 h-9 rounded-lg text-sm font-medium transition-colors ${
                    currentPage === pageNum
                      ? 'bg-indigo-600 text-white'
                      : 'border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800'
                  }`}
                >
                  {pageNum}
                </button>
              );
            })}
            <button
              onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))}
              disabled={currentPage === totalPages}
              className="p-2 border border-gray-200 dark:border-gray-700 rounded-lg disabled:opacity-50 hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-600 dark:text-gray-400"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

function getValue(obj, path) {
  return path.split('.').reduce((o, p) => o?.[p], obj);
}

function formatValue(val) {
  if (val == null) return '—';
  if (typeof val === 'boolean') return val ? 'Yes' : 'No';
  if (val instanceof Date) return val.toLocaleDateString();
  return String(val);
}

## File: frontend-react/public/manifest.json

{
  "name": "AI-ERP System",
  "short_name": "AI-ERP",
  "description": "AI-Powered Enterprise Resource Planning",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#4f46e5",
  "icons": [
    {
      "src": "/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}

## File: frontend-react/public/sw.js

const CACHE_NAME = 'ai-erp-v1';
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/src/main.jsx',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME)
          .map((name) => caches.delete(name))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  if (event.request.url.includes('/api/')) {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          return response;
        })
        .catch(() => {
          return caches.match(event.request).then((cached) => {
            if (cached) return cached;
            return new Response(JSON.stringify({ offline: true }), {
              headers: { 'Content-Type': 'application/json' }
            });
          });
        })
    );
  } else {
    event.respondWith(
      caches.match(event.request).then((cached) => {
        return cached || fetch(event.request);
      })
    );
  }
});

self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-data') {
    event.waitUntil(syncData());
  }
});

async function syncData() {
  const queue = await getSyncQueue();
  for (const item of queue) {
    try {
      await fetch(item.url, {
        method: item.method,
        headers: item.headers,
        body: item.body
      });
      await removeFromQueue(item.id);
    } catch (e) {
      console.error('Sync failed for item:', item.id);
    }
  }
}

async function getSyncQueue() {
  return [];
}

async function removeFromQueue(id) {
  return;
}