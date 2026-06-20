import { Routes, Route } from 'react-router-dom';
import { ClientLayout } from './components/ClientLayout';
import { ClientDashboard } from './pages/ClientDashboard';
import { ClientOrders } from './pages/ClientOrders';
import { ClientInvoices } from './pages/ClientInvoices';
import { ClientProfile } from './pages/ClientProfile';
import { ClientLogin } from './pages/ClientLogin';

function App() {
  return (
    <Routes>
      <Route path="/login" element={<ClientLogin />} />
      <Route path="/" element={<ClientLayout />}>
        <Route index element={<ClientDashboard />} />
        <Route path="orders" element={<ClientOrders />} />
        <Route path="invoices" element={<ClientInvoices />} />
        <Route path="profile" element={<ClientProfile />} />
      </Route>
    </Routes>
  );
}

export default App;
