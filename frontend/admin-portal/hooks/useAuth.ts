import { create } from "zustand";
import { persist } from "zustand/middleware";
import { authApi } from "@/lib/api";
interface User { id: string; email: string; first_name: string; last_name: string; role: string; tenant_id: string; }
interface AuthState {
  user: User | null; token: string | null; refreshToken: string | null;
  isAuthenticated: boolean; isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}
export const useAuth = create<AuthState>()(persist((set) => ({
  user: null, token: null, refreshToken: null, isAuthenticated: false, isLoading: false,
  login: async (email, password) => {
    set({ isLoading: true });
    try {
      const response = await authApi.login(email, password);
      const { token, user } = response.data;
      localStorage.setItem("access_token", token.access_token);
      localStorage.setItem("tenant_id", user.tenant_id);
      set({ user, token: token.access_token, refreshToken: token.refresh_token, isAuthenticated: true, isLoading: false });
    } catch (error) { set({ isLoading: false }); throw error; }
  },
  logout: () => {
    localStorage.removeItem("access_token"); localStorage.removeItem("tenant_id");
    set({ user: null, token: null, refreshToken: null, isAuthenticated: false });
  },
}), { name: "auth-storage" }));
