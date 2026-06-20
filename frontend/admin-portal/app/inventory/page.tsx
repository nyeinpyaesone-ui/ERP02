"use client";
import { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { useQuery } from "@tanstack/react-query";
import { inventoryApi } from "@/lib/api";
import { Package, AlertTriangle } from "lucide-react";
import { formatCurrency, formatNumber } from "@/lib/utils";
export default function InventoryPage() {
  const [page, setPage] = useState(1);
  const { data: products, isLoading } = useQuery({ queryKey: ["products", page], queryFn: () => inventoryApi.getProducts({ page, page_size: 10 }).then(r => r.data) });
  const { data: lowStock } = useQuery({ queryKey: ["low-stock"], queryFn: () => inventoryApi.getLowStock().then(r => r.data) });
  const { data: dashboard } = useQuery({ queryKey: ["inventory-dashboard"], queryFn: () => inventoryApi.getDashboard().then(r => r.data) });
  const statusColors: Record<string, string> = { in_stock: "success", low_stock: "warning", out_of_stock: "danger", discontinued: "secondary", on_order: "default" };
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div><h1 className="text-3xl font-bold tracking-tight">Inventory</h1><p className="text-muted-foreground">Manage products, stock levels, and AI forecasts.</p></div>
        <Button><Package className="mr-2 h-4 w-4" />Add Product</Button>
      </div>
      <div className="grid gap-4 md:grid-cols-3">
        <Card><CardHeader className="pb-2"><CardTitle className="text-sm font-medium">Total Products</CardTitle></CardHeader>
          <CardContent><div className="text-2xl font-bold">{formatNumber(dashboard?.total_products || 0)}</div></CardContent></Card>
        <Card><CardHeader className="pb-2"><CardTitle className="text-sm font-medium text-yellow-600">Low Stock Items</CardTitle></CardHeader>
          <CardContent><div className="text-2xl font-bold text-yellow-600">{dashboard?.low_stock_count || 0}</div></CardContent></Card>
        <Card><CardHeader className="pb-2"><CardTitle className="text-sm font-medium">Inventory Value</CardTitle></CardHeader>
          <CardContent><div className="text-2xl font-bold">{formatCurrency(dashboard?.inventory_value || 0)}</div></CardContent></Card>
      </div>
      <Card>
        <CardHeader><CardTitle>Products</CardTitle></CardHeader>
        <CardContent>
          {isLoading ? <div className="py-8 text-center text-muted-foreground">Loading...</div> : (
            <div className="rounded-md border">
              <table className="w-full text-sm">
                <thead className="border-b bg-muted/50"><tr>
                  <th className="px-4 py-3 text-left font-medium">SKU</th>
                  <th className="px-4 py-3 text-left font-medium">Name</th>
                  <th className="px-4 py-3 text-right font-medium">Price</th>
                  <th className="px-4 py-3 text-right font-medium">Stock</th>
                  <th className="px-4 py-3 text-center font-medium">Status</th>
                </tr></thead>
                <tbody>
                  {products?.map((product: any) => (
                    <tr key={product.id} className="border-b last:border-0 hover:bg-muted/50">
                      <td className="px-4 py-3 font-mono text-xs">{product.sku}</td>
                      <td className="px-4 py-3">{product.name}</td>
                      <td className="px-4 py-3 text-right">{formatCurrency(product.unit_price)}</td>
                      <td className="px-4 py-3 text-right">{product.quantity_on_hand}</td>
                      <td className="px-4 py-3 text-center"><Badge variant={statusColors[product.status] as any || "default"}>{product.status}</Badge></td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
          <div className="mt-4 flex items-center justify-between">
            <Button variant="outline" size="sm" onClick={() => setPage(Math.max(1, page - 1))} disabled={page === 1}>Previous</Button>
            <span className="text-sm text-muted-foreground">Page {page}</span>
            <Button variant="outline" size="sm" onClick={() => setPage(page + 1)}>Next</Button>
          </div>
        </CardContent>
      </Card>
      {lowStock && lowStock.length > 0 && (
        <Card className="border-yellow-200 bg-yellow-50/50">
          <CardHeader><CardTitle className="flex items-center gap-2 text-yellow-700"><AlertTriangle className="h-5 w-5" />Low Stock Alerts</CardTitle></CardHeader>
          <CardContent>
            <div className="space-y-2">
              {lowStock.map((item: any) => (
                <div key={item.id} className="flex items-center justify-between rounded-md border bg-white p-3">
                  <div><p className="font-medium">{item.name}</p><p className="text-xs text-muted-foreground">SKU: {item.sku}</p></div>
                  <div className="text-right"><p className="text-sm font-medium text-yellow-600">{item.quantity} remaining</p><p className="text-xs text-muted-foreground">Reorder at: {item.reorder_point}</p></div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
