import { Card, CardContent } from '../components/ui/card';
import { Search, Filter } from 'lucide-react';

export function ClientOrders() {
  const orders = [
    { id: 'SO-2024-001', date: '2024-01-15', items: 5, total: '$12,000', status: 'Delivered' },
    { id: 'SO-2024-002', date: '2024-01-20', items: 3, total: '$8,500', status: 'Shipped' },
    { id: 'SO-2024-003', date: '2024-01-25', items: 2, total: '$4,000', status: 'Processing' },
    { id: 'SO-2024-004', date: '2024-02-01', items: 8, total: '$18,000', status: 'Pending' },
  ];
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold">My Orders</h1>
        <div className="flex gap-2">
          <div className="relative">
            <Search className="absolute left-3 top-2.5 h-4 w-4 text-gray-400" />
            <input type="text" placeholder="Search orders..." className="pl-10 pr-4 py-2 border rounded-lg text-sm w-64" />
          </div>
          <button className="flex items-center gap-2 px-4 py-2 border rounded-lg text-sm hover:bg-gray-50">
            <Filter className="h-4 w-4" />Filter
          </button>
        </div>
      </div>
      <Card>
        <CardContent className="p-0">
          <table className="w-full text-sm">
            <thead className="bg-gray-50 border-b"><tr>
              <th className="px-6 py-3 text-left font-medium">Order #</th>
              <th className="px-6 py-3 text-left font-medium">Date</th>
              <th className="px-6 py-3 text-right font-medium">Items</th>
              <th className="px-6 py-3 text-right font-medium">Total</th>
              <th className="px-6 py-3 text-center font-medium">Status</th>
            </tr></thead>
            <tbody>
              {orders.map((order) => (
                <tr key={order.id} className="border-b last:border-0 hover:bg-gray-50">
                  <td className="px-6 py-4 font-medium">{order.id}</td>
                  <td className="px-6 py-4 text-gray-500">{order.date}</td>
                  <td className="px-6 py-4 text-right">{order.items}</td>
                  <td className="px-6 py-4 text-right font-medium">{order.total}</td>
                  <td className="px-6 py-4 text-center">
                    <span className={`inline-flex px-2.5 py-1 rounded-full text-xs font-medium ${
                      order.status === 'Delivered' ? 'bg-green-100 text-green-700' :
                      order.status === 'Shipped' ? 'bg-blue-100 text-blue-700' :
                      order.status === 'Processing' ? 'bg-yellow-100 text-yellow-700' :
                      'bg-gray-100 text-gray-700'
                    }`}>{order.status}</span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </CardContent>
      </Card>
    </div>
  );
}
