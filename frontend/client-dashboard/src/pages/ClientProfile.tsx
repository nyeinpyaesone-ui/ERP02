import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Building, Mail, Phone, MapPin } from 'lucide-react';

export function ClientProfile() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Company Profile</h1>
      <div className="grid grid-cols-2 gap-6">
        <Card>
          <CardHeader><CardTitle>Company Information</CardTitle></CardHeader>
          <CardContent className="space-y-4">
            <div className="flex items-center gap-3">
              <Building className="h-5 w-5 text-gray-400" />
              <div><p className="text-sm text-gray-500">Company Name</p><p className="font-medium">Acme Corporation</p></div>
            </div>
            <div className="flex items-center gap-3">
              <Mail className="h-5 w-5 text-gray-400" />
              <div><p className="text-sm text-gray-500">Email</p><p className="font-medium">contact@acme.com</p></div>
            </div>
            <div className="flex items-center gap-3">
              <Phone className="h-5 w-5 text-gray-400" />
              <div><p className="text-sm text-gray-500">Phone</p><p className="font-medium">+1 (555) 123-4567</p></div>
            </div>
            <div className="flex items-center gap-3">
              <MapPin className="h-5 w-5 text-gray-400" />
              <div><p className="text-sm text-gray-500">Address</p><p className="font-medium">123 Business Ave, Suite 100, New York, NY 10001</p></div>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Account Settings</CardTitle></CardHeader>
          <CardContent className="space-y-4">
            <div><label className="text-sm font-medium">Credit Limit</label><p className="text-lg font-bold">$50,000</p><p className="text-sm text-gray-500">$8,500 currently utilized</p></div>
            <div><label className="text-sm font-medium">Payment Terms</label><p className="font-medium">Net 30</p></div>
            <div><label className="text-sm font-medium">Preferred Currency</label><p className="font-medium">USD</p></div>
            <button className="w-full py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700">Update Profile</button>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
