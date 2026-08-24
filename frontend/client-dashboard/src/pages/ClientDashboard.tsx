import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Package, DollarSign, TrendingUp, Clock } from 'lucide-react';

export function ClientDashboard() {
  const [timeRange, setTimeRange] = useState('30d');
  const stats = [
    { title: 'Active Orders', value: '3', icon: Package, color: 'blue' },
    { title: 'Total Spent', value: '$24,500', icon: DollarSign, color: 'green' },
    { title: 'Avg. Order Value', value: '$8,167', icon: TrendingUp, color: 'purple' },
    { title: 'Pending Invoices', value: '2', icon: Clock, color: 'orange' },
  ];
  const recentOrders = [
    { id: 'SO-2024-001', date: '2024-01-15', status: 'Shipped', total: '$12,000' },
    { id: 'SO-2024-002', date: '2024-01-20', status: 'Processing', total: '$8,500' },
    { id: 'SO-2024-003', date: '2024-01-25', status: 'Pending', total: '$4,000' },
  ];
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div><h1 className="text-2xl font-bold">Welcome back, Acme Corp</h1><p className="text-gray-500">Here is what is happening with your account.</p></div>
        <div className="flex gap-2">
          {['7d', '30d', '90d', '1y'].map((range) => (
            <button key={range} onClick={() => setTimeRange(range)}
              className={`px-3 py-1.5 rounded-md text-sm font-medium ${timeRange === range ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'}`}>
              {range === '1y' ? '1 Year' : `Last ${range}`}
            </button>
          ))}
        </div>
      </div>
      <div className="grid grid-cols-4 gap-4">
        {stats.map((stat) => {
          const Icon = stat.icon;
          return (
            <Card key={stat.title}>
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div><p className="text-sm text-gray-500">{stat.title}</p><p className="text-2xl font-bold mt-1">{stat.value}</p></div>
                  <div className={`p-3 rounded-lg bg-${stat.color}-50`}><Icon className={`h-5 w-5 text-${stat.color}-600`} /></div>
                </div>
              </CardContent>
            </Card>
          );
        })}
      </div>
      <div className="grid grid-cols-2 gap-6">
        <Card>
          <CardHeader><CardTitle>Recent Orders</CardTitle></CardHeader>
          <CardContent>
            <div className="space-y-3">
              {recentOrders.map((order) => (
                <div key={order.id} className="flex items-center justify-between p-3 rounded-lg border">
                  <div><p className="font-medium">{order.id}</p><p className="text-sm text-gray-500">{order.date}</p></div>
                  <div className="text-right">
                    <span className={`inline-flex px-2 py-1 rounded-full text-xs font-medium ${
                      order.status === 'Shipped' ? 'bg-green-100 text-green-700' :
                      order.status === 'Processing' ? 'bg-blue-100 text-blue-700' :
                      'bg-yellow-100 text-yellow-700'
                    }`}>{order.status}</span>
                    <p className="text-sm font-medium mt-1">{order.total}</p>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>AI Recommendations</CardTitle></CardHeader>
          <CardContent>
            <div className="space-y-3">
              <div className="p-3 rounded-lg border bg-blue-50">
                <p className="font-medium text-blue-900">Bulk Order Discount</p>
                <p className="text-sm text-blue-700 mt-1">Order 500+ units of SKU-001 to unlock 15% volume discount. Potential savings: $2,400.</p>
              </div>
              <div className="p-3 rounded-lg border bg-green-50">
                <p className="font-medium text-green-900">Payment Optimization</p>
                <p className="text-sm text-green-700 mt-1">Pay Invoice INV-2024-003 within 5 days to earn 2% early payment discount.</p>
              </div>
              <div className="p-3 rounded-lg border bg-purple-50">
                <p className="font-medium text-purple-900">Product Substitution</p>
                <p className="text-sm text-purple-700 mt-1">SKU-002 is backordered. AI suggests SKU-002-B as equivalent with faster delivery.</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}