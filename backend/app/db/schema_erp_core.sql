-- Enterprise ERP Core Schema (PostgreSQL 16)
-- ACID Compliant, Multi-Tenant, Audit-Ready

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm"; -- For enterprise search indexing

-- 1. Multi-Tenancy & Security
CREATE TABLE tenants (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    schema_name VARCHAR(63) NOT NULL UNIQUE,
    status VARCHAR(20) DEFAULT 'active', -- active, suspended, archived
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    config JSONB DEFAULT '{}'::jsonb
);

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id) ON DELETE CASCADE,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL, -- ADMIN, FINANCE_MANAGER, HR_MANAGER, WAREHOUSE_SUPERVISOR
    mfa_secret VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP WITH TIME ZONE,
    UNIQUE(tenant_id, email)
);

-- 2. Finance Module (General Ledger, AP/AR, Cash Management)
CREATE TABLE chart_of_accounts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    code VARCHAR(20) NOT NULL,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL, -- ASSET, LIABILITY, EQUITY, REVENUE, EXPENSE
    parent_id UUID REFERENCES chart_of_accounts(id),
    currency CHAR(3) DEFAULT 'USD',
    UNIQUE(tenant_id, code)
);

CREATE TABLE journal_entries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    entry_date DATE NOT NULL,
    description VARCHAR(500),
    reference_type VARCHAR(50), -- INVOICE, PAYMENT, ADJUSTMENT
    reference_id UUID,
    status VARCHAR(20) DEFAULT 'draft', -- draft, posted, locked
    created_by UUID REFERENCES users(id),
    posted_at TIMESTAMP WITH TIME ZONE,
    locked BOOLEAN DEFAULT FALSE
);

CREATE TABLE journal_lines (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entry_id UUID REFERENCES journal_entries(id) ON DELETE CASCADE,
    account_id UUID REFERENCES chart_of_accounts(id),
    debit DECIMAL(19, 4) DEFAULT 0.0000,
    credit DECIMAL(19, 4) DEFAULT 0.0000,
    CHECK (debit >= 0 AND credit >= 0)
);

-- Ensure Journal Entry Balance
CREATE OR REPLACE FUNCTION check_entry_balance() RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT SUM(debit) - SUM(credit) FROM journal_lines WHERE entry_id = NEW.entry_id) != 0 THEN
        RAISE EXCEPTION 'Journal entry must balance (Debit = Credit)';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_entry_balance
AFTER INSERT OR UPDATE ON journal_lines
FOR EACH ROW EXECUTE FUNCTION check_entry_balance();

CREATE TABLE invoices (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    type VARCHAR(20) NOT NULL, -- ACCOUNT_RECEIVABLE, ACCOUNT_PAYABLE
    invoice_number VARCHAR(50) NOT NULL,
    partner_id UUID, -- Link to CRM/Vendor table
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    total_amount DECIMAL(19, 4) NOT NULL,
    paid_amount DECIMAL(19, 4) DEFAULT 0.0000,
    status VARCHAR(20) DEFAULT 'draft', -- draft, posted, paid, overdue, cancelled
    currency CHAR(3) DEFAULT 'USD',
    UNIQUE(tenant_id, invoice_number)
);

-- 3. Human Resources (HRM) Module
CREATE TABLE employees (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    user_id UUID REFERENCES users(id),
    employee_number VARCHAR(50) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    department VARCHAR(100),
    position VARCHAR(100),
    hire_date DATE NOT NULL,
    termination_date DATE,
    salary_base DECIMAL(19, 4),
    status VARCHAR(20) DEFAULT 'active',
    UNIQUE(tenant_id, employee_number)
);

CREATE TABLE payroll_runs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    pay_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'draft', -- draft, calculated, approved, paid
    total_gross DECIMAL(19, 4),
    total_net DECIMAL(19, 4),
    created_by UUID REFERENCES users(id)
);

CREATE TABLE payroll_lines (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    run_id UUID REFERENCES payroll_runs(id) ON DELETE CASCADE,
    employee_id UUID REFERENCES employees(id),
    gross_pay DECIMAL(19, 4),
    deductions JSONB, -- Tax, Insurance, etc.
    net_pay DECIMAL(19, 4),
    paid BOOLEAN DEFAULT FALSE
);

-- 4. Supply Chain & Inventory Module
CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    sku VARCHAR(100) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(100),
    unit_of_measure VARCHAR(50) DEFAULT 'UNIT',
    cost_price DECIMAL(19, 4),
    sales_price DECIMAL(19, 4),
    reorder_point INTEGER DEFAULT 0,
    UNIQUE(tenant_id, sku)
);

CREATE TABLE warehouses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    code VARCHAR(50) NOT NULL,
    name VARCHAR(255),
    location_address TEXT,
    UNIQUE(tenant_id, code)
);

CREATE TABLE inventory_levels (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID REFERENCES products(id),
    warehouse_id UUID REFERENCES warehouses(id),
    quantity_on_hand DECIMAL(19, 4) DEFAULT 0,
    quantity_reserved DECIMAL(19, 4) DEFAULT 0,
    quantity_available GENERATED ALWAYS AS (quantity_on_hand - quantity_reserved) STORED,
    last_counted_at TIMESTAMP WITH TIME ZONE,
    UNIQUE(product_id, warehouse_id)
);

CREATE TABLE stock_moves (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    product_id UUID REFERENCES products(id),
    warehouse_id UUID REFERENCES warehouses(id),
    move_type VARCHAR(50), -- INBOUND, OUTBOUND, INTERNAL, ADJUSTMENT
    reference_doc_type VARCHAR(50), -- PO, SO, MO
    reference_doc_id UUID,
    quantity DECIMAL(19, 4) NOT NULL,
    direction INTEGER, -- 1 (in), -1 (out)
    occurred_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    performed_by UUID REFERENCES users(id)
);

-- 5. Manufacturing (MRP) Module
CREATE TABLE bills_of_materials (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    product_id UUID REFERENCES products(id), -- Parent Product
    version INTEGER DEFAULT 1,
    is_active BOOLEAN DEFAULT TRUE,
    UNIQUE(tenant_id, product_id, version)
);

CREATE TABLE bom_lines (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    bom_id UUID REFERENCES bills_of_materials(id) ON DELETE CASCADE,
    component_product_id UUID REFERENCES products(id),
    quantity_required DECIMAL(19, 4) NOT NULL,
    scrap_percentage DECIMAL(5, 2) DEFAULT 0.00
);

CREATE TABLE manufacturing_orders (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    order_number VARCHAR(50) NOT NULL,
    product_id UUID REFERENCES products(id),
    bom_id UUID REFERENCES bills_of_materials(id),
    quantity_to_produce DECIMAL(19, 4) NOT NULL,
    status VARCHAR(20) DEFAULT 'draft', -- draft, planned, in_progress, completed, cancelled
    scheduled_start DATE,
    scheduled_end DATE,
    actual_start TIMESTAMP WITH TIME ZONE,
    actual_end TIMESTAMP WITH TIME ZONE,
    UNIQUE(tenant_id, order_number)
);

-- 6. CRM Module
CREATE TABLE partners (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    type VARCHAR(20), -- CUSTOMER, VENDOR, BOTH
    name VARCHAR(255) NOT NULL,
    tax_id VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(50),
    address TEXT,
    credit_limit DECIMAL(19, 4) DEFAULT 0.0000,
    UNIQUE(tenant_id, name)
);

CREATE TABLE sales_opportunities (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id),
    partner_id UUID REFERENCES partners(id),
    title VARCHAR(255),
    stage VARCHAR(50), -- LEAD, QUALIFIED, PROPOSAL, NEGOTIATION, WON, LOST
    expected_amount DECIMAL(19, 4),
    expected_close_date DATE,
    probability INTEGER DEFAULT 0, -- 0-100
    owner_id UUID REFERENCES users(id)
);

-- 7. Audit Logging (Compliance)
CREATE TABLE audit_logs (
    id BIGSERIAL PRIMARY KEY,
    tenant_id UUID,
    user_id UUID,
    action VARCHAR(50) NOT NULL, -- CREATE, UPDATE, DELETE, POST, LOGIN
    entity_type VARCHAR(50) NOT NULL,
    entity_id UUID,
    old_values JSONB,
    new_values JSONB,
    ip_address INET,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexing for Enterprise Search Performance
CREATE INDEX idx_products_sku ON products USING gin (sku gin_trgm_ops);
CREATE INDEX idx_partners_name ON partners USING gin (name gin_trgm_ops);
CREATE INDEX idx_journal_lines_account ON journal_lines(account_id);
CREATE INDEX idx_inventory_levels ON inventory_levels(product_id, warehouse_id);
CREATE INDEX idx_audit_logs_entity ON audit_logs(entity_type, entity_id);
