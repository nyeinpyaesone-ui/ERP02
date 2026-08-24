import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Download, CreditCard } from 'lucide-react';

export function ClientInvoices() {
  const invoices = [
    { id: 'INV-2024-001', date: '2024-01-15', due: '2024-02-15', amount: '$12,000', status: 'Paid', paid: '$12,000' },
    { id: 'INV-2024-002', date: '2024-01-20', due: '2024-02-20', amount: '$8,500', status: 'Partial', paid: '$4,000' },
    { id: 'INV-2024-003', date: '2024-01-25', due: '2024-02-25', amount: '$4,000', status: 'Pending', paid: '$0' },
  ];
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Invoices</h1>
      <div className="grid grid-cols-3 gap-4">
        <Card><CardContent className="p-6"><p className="text-sm text-gray-500">Total Outstanding</p><p className="text-2xl font-bold mt-1">$8,500</p></CardContent></Card>
        <Card><CardContent className="p-6"><p className="text-sm text-gray-500">Overdue</p><p className="text-2xl font-bold mt-1 text-red-600">$0</p></CardContent></Card>
        <Card><CardContent className="p-6"><p className="text-sm text-gray-500">Paid This Month</p><p className="text-2xl font-bold mt-1 text-green-600">$12,000</p></CardContent></Card>
      </div>
      <Card>
        <CardHeader><CardTitle>All Invoices</CardTitle></CardHeader>
        <CardContent className="p-0">
          <table className="w-full text-sm">
            <thead className="bg-gray-50 border-b"><tr>
              <th className="px-6 py-3 text-left font-medium">Invoice #</th>
              <th className="px-6 py-3 text-left font-medium">Date</th>
              <th className="px-6 py-3 text-left font-medium">Due Date</th>
              <th className="px-6 py-3 text-right font-medium">Amount</th>
              <th className="px-6 py-3 text-right font-medium">Paid</th>
              <th className="px-6 py-3 text-center font-medium">Status</th>
              <th className="px-6 py-3 text-center font-medium">Actions</th>
            </tr></thead>
            <tbody>
              {invoices.map((inv) => (
                <tr key={inv.id} className="border-b last:border-0 hover:bg-gray-50">
                  <td className="px-6 py-4 font-medium">{inv.id}</td>
                  <td className="px-6 py-4 text-gray-500">{inv.date}</td>
                  <td className="px-6 py-4 text-gray-500">{inv.due}</td>
                  <td className="px-6 py-4 text-right font-medium">{inv.amount}</td>
                  <td className="px-6 py-4 text-right">{inv.paid}</td>
                  <td className="px-6 py-4 text-center">
                    <span className={`inline-flex px-2.5 py-1 rounded-full text-xs font-medium ${
                      inv.status === 'Paid' ? 'bg-green-100 text-green-700' :
                      inv.status === 'Partial' ? 'bg-yellow-100 text-yellow-700' :
                      'bg-red-100 text-red-700'
                    }`}>{inv.status}</span>
                  </td>
                  <td className="px-6 py-4 text-center">
                    <div className="flex justify-center gap-2">
                      <button className="p-1.5 hover:bg-gray-100 rounded"><Download className="h-4 w-4 text-gray-500" /></button>
                      {inv.status !== 'Paid' && <button className="p-1.5 hover:bg-gray-100 rounded"><CreditCard className="h-4 w-4 text-blue-600" /></button>}
                    </div>
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