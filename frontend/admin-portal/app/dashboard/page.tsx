"use client";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { useQuery } from "@tanstack/react-query";
import { inventoryApi, crmApi, financeApi, hrApi } from "@/lib/api";
import { Package, Users, DollarSign, Briefcase, TrendingUp, AlertTriangle, Brain } from "lucide-react";
import { formatCurrency, formatNumber } from "@/lib/utils";
export default function DashboardPage() {
  const { data: inventory } = useQuery({ queryKey: ["inventory-dashboard"], queryFn: () => inventoryApi.getDashboard().then(r => r.data) });
  const { data: crm } = useQuery({ queryKey: ["crm-dashboard"], queryFn: () => crmApi.getDashboard().then(r => r.data) });
  const { data: finance } = useQuery({ queryKey: ["finance-dashboard"], queryFn: () => financeApi.getDashboard().then(r => r.data) });
  const { data: hr } = useQuery({ queryKey: ["hr-dashboard"], queryFn: () => hrApi.getDashboard().then(r => r.data) });
  const kpiCards = [
    { title: "Inventory Value", value: formatCurrency(inventory?.inventory_value || 0), change: "+12.5%", trend: "up", icon: Package, subtitle: `${inventory?.total_products || 0} products` },
    { title: "Total Revenue", value: formatCurrency(crm?.total_revenue || 0), change: "+8.2%", trend: "up", icon: DollarSign, subtitle: `${crm?.total_orders || 0} orders` },
    { title: "Active Employees", value: formatNumber(hr?.active_employees || 0), change: "+2", trend: "up", icon: Briefcase, subtitle: `${hr?.pending_leave_requests || 0} pending leave` },
    { title: "Customers", value: formatNumber(crm?.total_customers || 0), change: "+15", trend: "up", icon: Users, subtitle: "12 at churn risk" },
  ];
  return (
    <div className="space-y-6">
      <div><h1 className="text-3xl font-bold tracking-tight">Dashboard</h1><p className="text-muted-foreground">AI-powered overview of your enterprise.</p></div>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {kpiCards.map((card) => {
          const Icon = card.icon;
          const TrendIcon = TrendingUp;
          return (
            <Card key={card.title}>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">{card.title}</CardTitle>
                <Icon className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">{card.value}</div>
                <div className="flex items-center text-xs text-muted-foreground">
                  <TrendIcon className={`mr-1 h-3 w-3 ${card.trend === "up" ? "text-green-500" : "text-red-500"}`} />
                  {card.change} from last month
                </div>
                <p className="mt-1 text-xs text-muted-foreground">{card.subtitle}</p>
              </CardContent>
            </Card>
          );
        })}
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2"><Brain className="h-5 w-5 text-primary" />AI Insights</CardTitle>
            <CardDescription>Latest AI-generated recommendations</CardDescription>
          </CardHeader>
          <CardContent className="space-y-3">
            {[{ title: "Inventory Alert", text: inventory?.ai_recommendation }, { title: "CRM Alert", text: crm?.ai_insight },
              { title: "Finance Alert", text: finance?.ai_insight }, { title: "HR Alert", text: hr?.ai_insight }].map((alert) => (
              <div key={alert.title} className="flex items-start gap-3 rounded-lg border p-3">
                <AlertTriangle className="mt-0.5 h-4 w-4 text-yellow-500" />
                <div><p className="text-sm font-medium">{alert.title}</p><p className="text-xs text-muted-foreground">{alert.text}</p></div>
              </div>
            ))}
          </CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>System Health</CardTitle><CardDescription>Real-time service status</CardDescription></CardHeader>
          <CardContent className="space-y-3">
            {[{ name: "Database", status: "healthy", color: "success" }, { name: "AI Engine", status: "healthy", color: "success" },
              { name: "Redis Cache", status: "healthy", color: "success" }, { name: "Message Queue", status: "healthy", color: "success" },
              { name: "API Gateway", status: "healthy", color: "success" }].map((service) => (
              <div key={service.name} className="flex items-center justify-between">
                <span className="text-sm">{service.name}</span>
                <Badge variant={service.color as any}>{service.status}</Badge>
              </div>
            ))}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}