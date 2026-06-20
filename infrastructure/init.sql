-- Initial database setup
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

INSERT INTO tenants (id, name, slug, plan, is_active)
VALUES ('00000000-0000-0000-0000-000000000000', 'Default Tenant', 'default', 'enterprise', true)
ON CONFLICT DO NOTHING;
