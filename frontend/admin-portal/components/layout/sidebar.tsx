"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { LayoutDashboard, Package, Users, DollarSign, Briefcase, Brain, BarChart3, Settings, LogOut, ShoppingCart, Factory, FolderKanban, ShieldCheck } from "lucide-react";
import { cn } from "@/lib/utils";
import { useAuth } from "@/hooks/useAuth";
const navItems = [
  { href: "/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { href: "/inventory", label: "Inventory", icon: Package },
  { href: "/crm", label: "CRM", icon: Users },
  { href: "/finance", label: "Finance", icon: DollarSign },
  { href: "/hr", label: "HR", icon: Briefcase },
  { href: "/procurement", label: "Procurement", icon: ShoppingCart },
  { href: "/manufacturing", label: "Manufacturing", icon: Factory },
  { href: "/projects", label: "Projects", icon: FolderKanban },
  { href: "/compliance", label: "Compliance", icon: ShieldCheck },
  { href: "/analytics", label: "Analytics", icon: BarChart3 },
  { href: "/ai-agents", label: "AI Agents", icon: Brain },
  { href: "/settings", label: "Settings", icon: Settings },
];
export function Sidebar() {
  const pathname = usePathname();
  const { logout } = useAuth();
  return (
    <aside className="fixed left-0 top-0 z-40 h-screen w-64 border-r bg-background">
      <div className="flex h-full flex-col">
        <div className="flex h-16 items-center border-b px-6">
          <Brain className="mr-2 h-6 w-6 text-primary" />
          <span className="text-lg font-bold">AI ERP</span>
        </div>
        <nav className="flex-1 space-y-1 px-3 py-4">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = pathname === item.href || pathname?.startsWith(`${item.href}/`);
            return (
              <Link key={item.href} href={item.href}
                className={cn("flex items-center rounded-lg px-3 py-2 text-sm font-medium transition-colors",
                  isActive ? "bg-primary text-primary-foreground" : "text-muted-foreground hover:bg-accent hover:text-accent-foreground")}>
                <Icon className="mr-3 h-4 w-4" />{item.label}
              </Link>
            );
          })}
        </nav>
        <div className="border-t p-3">
          <button onClick={logout}
            className="flex w-full items-center rounded-lg px-3 py-2 text-sm font-medium text-muted-foreground hover:bg-accent hover:text-accent-foreground">
            <LogOut className="mr-3 h-4 w-4" />Logout
          </button>
        </div>
      </div>
    </aside>
  );
}
