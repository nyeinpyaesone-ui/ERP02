-- =============================================================================
-- ENTERPRISE ERP MASTER DATA FOR MYANMAR BUSINESS OPERATIONS
-- Production-grade deterministic data tables for Finance, Logistics, HR, E-commerce, SME modules
-- NO AI/LLM dependencies. Pure SQL business logic.
-- =============================================================================

-- Extensions (only standard PostgreSQL extensions)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS citext;

-- =============================================================================
-- 1. GEOGRAPHY – Townships (Master Location Data)
-- Used by: Logistics, E-commerce, SME modules for delivery calculations
-- =============================================================================
CREATE TABLE IF NOT EXISTS erp_townships (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    township_code VARCHAR(20) UNIQUE NOT NULL,
    name_en VARCHAR(100) NOT NULL,
    name_mm VARCHAR(100),
    region_state VARCHAR(100) NOT NULL,
    delivery_zone VARCHAR(20) NOT NULL CHECK (delivery_zone IN ('Express', 'Standard', 'Remote')),
    delivery_fee_mmk NUMERIC(12,2) NOT NULL CHECK (delivery_fee_mmk >= 0),
    estimated_delivery_days INTEGER NOT NULL CHECK (estimated_delivery_days > 0 AND estimated_delivery_days <= 30),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO erp_townships (township_code, name_en, name_mm, region_state, delivery_zone, delivery_fee_mmk, estimated_delivery_days) VALUES
('YGN-001','Hlaingthaya','လှိုင်သာယာ','Yangon','Standard',1500.00,2),
('YGN-002','Hlaing','လှိုင်','Yangon','Express',1000.00,1),
('YGN-003','Kamayut','ကမာရွတ်','Yangon','Express',1000.00,1),
('YGN-006','Botataung','ဗိုလ်တစ်ထောင်','Yangon','Express',1000.00,1),
('MDY-001','Chanayethazan','ချမ်းအေးသာဇံ','Mandalay','Express',1500.00,1),
('MDY-002','Mahaaungmye','မဟာအောင်မြေ','Mandalay','Express',1500.00,1),
('NPW-001','Zayarthiri','ဇေယျာသီရိ','Nay Pyi Taw','Standard',2000.00,1),
('SHN-001','Taunggyi','တောင်ကြီး','Shan','Remote',4000.00,3),
('KYN-001','Myawaddy','မြဝတီ','Kayin','Remote',5000.00,3),
('RKH-001','Sittwe','စစ်တွေ','Rakhine','Remote',6000.00,5);

-- =============================================================================
-- 2. BORDER TRADE STATIONS (Cross-border Operations Data)
-- Used by: Logistics, Finance modules for international trade compliance
-- =============================================================================
CREATE TABLE IF NOT EXISTS erp_border_trade_stations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    station_name VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Active' CHECK (status IN ('Active', 'Restricted', 'Inactive')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO erp_border_trade_stations (station_name, country, status, notes) VALUES
('Muse','China','Active','105-mile trade zone; busiest border point'),
('Chinshwehaw','China','Active','MNDAA-controlled area'),
('Lweje','China','Active','Kachin State'),
('Kampaiti','China','Active','Kachin State'),
('Kengtung','China','Active','Shan State'),
('Myawaddy','Thailand','Active','Reopened 28 May 2026; full import/export licenses resumed'),
('Hteekhee','Thailand','Active','Major alternative to Myawaddy'),
('Kawthoung','Thailand','Active','Coastal; alternative maritime route via Ranong'),
('Tachilek','Thailand','Restricted','Mandatory 1.3M MMK VIP pass; cargo volume down 90%'),
('Tamu','India','Active','Key India border post'),
('Reed','India','Inactive','Not operational'),
('Sittwe','Bangladesh','Active','Coastal via sea'),
('Maungtaw','Bangladesh','Active','Land border, restricted');

-- =============================================================================
-- 3. TAX RATES & COMPLIANCE RULES (Financial Calculations)
-- Used by: Finance, SME modules for accurate tax calculations and reporting
-- =============================================================================
CREATE TABLE IF NOT EXISTS erp_tax_rates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tax_type VARCHAR(50) NOT NULL,
    tax_name_en VARCHAR(100) NOT NULL,
    tax_name_mm VARCHAR(100),
    rate DECIMAL(5,4) NOT NULL CHECK (rate >= 0 AND rate <= 1),
    applicable_to TEXT,
    filing_frequency VARCHAR(50),
    notes TEXT,
    effective_from DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO erp_tax_rates (tax_type, tax_name_en, tax_name_mm, rate, applicable_to, filing_frequency, notes) VALUES
('CIT','Corporate Income Tax','ကော်ပိုရိတ် ဝင်ငွေခွန်',0.22,'Net profit','Annually (within 3 months of year end)','Quarterly advance payment may be required'),
('CT','Commercial Tax','ကုန်သွယ်ခွန်',0.05,'Sales','Monthly (or quarterly for SMEs)','Exempt for certain agricultural goods'),
('AIT','Advance Income Tax','ကြိုတင်ဝင်ငွေခွန်',0.02,'Imports','Per shipment','Recoverable against annual CIT'),
('WHT','Withholding Tax','ထိန်းသိမ်းခွန်',0.10,'Non-resident payments','Monthly','Generate certificate'),
('PIT','Personal Income Tax','ဝင်ငွေခွန်',0.00,'Salary (progressive 0-25%)','Monthly (employer) + annual return','Progressive rates apply; 0.00 indicates progressive scale'),
('SSB','Social Security Benefit','လူမှုဖူလုံရေး',0.02,'Salary (employer)','Monthly','Employee contributes additional 1%');

-- =============================================================================
-- 4. INDUSTRIAL ZONES & SEZs (Manufacturing & Investment Data)
-- Used by: Logistics, SME modules for location-based business decisions
-- =============================================================================
CREATE TABLE IF NOT EXISTS erp_industrial_zones (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    zone_name VARCHAR(100) NOT NULL,
    region VARCHAR(100),
    area_acres VARCHAR(50),
    key_industries TEXT,
    is_sez BOOLEAN DEFAULT FALSE,
    tax_holiday_years INTEGER DEFAULT 0 CHECK (tax_holiday_years >= 0 AND tax_holiday_years <= 50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO erp_industrial_zones (zone_name, region, area_acres, key_industries, is_sez, tax_holiday_years) VALUES
('Hlaing Thar Yar','Yangon','13,000','Garments, food processing, general manufacturing',FALSE,0),
('Shwe Pyi Thar','Yangon','~2,000','Mixed, logistics',FALSE,0),
('South Dagon','Yangon','~1,500','Light manufacturing',FALSE,0),
('Mandalay IZ','Mandalay','~1,000','Agriculture machinery, garments',FALSE,0),
('Myotha Industrial Park','Mandalay','3,978','New development; logistics hub',FALSE,0),
('Pathein IZ','Ayeyarwady','–','Garments, rice mills',FALSE,0),
('Thilawa SEZ','Yangon','5,027','90+ investors; multi-sector',TRUE,7),
('Dawei SEZ','Tanintharyi','–','Deep-sea port potential',TRUE,0),
('Kyaukphyu SEZ','Rakhine','–','Oil/gas pipelines',TRUE,0);

-- =============================================================================
-- 5. TRUCKING CORRIDORS & FREIGHT RATES (Logistics Operations)
-- Used by: Logistics, E-commerce modules for shipping cost calculations
-- =============================================================================
CREATE TABLE IF NOT EXISTS erp_trucking_corridors (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    route_name VARCHAR(100) NOT NULL,
    distance_km INTEGER CHECK (distance_km > 0 AND distance_km < 10000),
    terrain VARCHAR(50),
    daily_truck_volume VARCHAR(50),
    rate_per_ton_mmk NUMERIC(12,2) CHECK (rate_per_ton_mmk >= 0),
    seasonal_variation TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO erp_trucking_corridors (route_name, distance_km, terrain, daily_truck_volume, rate_per_ton_mmk, seasonal_variation) VALUES
('Yangon–Mandalay',712,'Flat','High',25000.00,'+40% during Thingyan; +30% monsoon'),
('Yangon–Myawaddy',460,'Mixed','Medium',30000.00,'+30% after road closures'),
('Mandalay–Muse',750,'Mountainous','100-150',45000.00,'+20% during harvest'),
('Mandalay–Tamu',600,'Mountainous','Low',40000.00,'Minimal variation');

-- =============================================================================
-- 6. CORRECTED BUSINESS TERMINOLOGY (Language Governance)
-- Used by: All modules for standardized Myanmar/English business terms
-- =============================================================================
CREATE TABLE IF NOT EXISTS erp_business_terms (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    term_en VARCHAR(100) NOT NULL,
    term_mm VARCHAR(200) NOT NULL,
    forbidden_version VARCHAR(200),
    domain VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO erp_business_terms (term_en, term_mm, forbidden_version, domain) VALUES
('Cargo Manifest','ကုန်စည်ပို့ဆောင်ရေးမှတ်တမ်း','Bus Cargo Manifest','logistics'),
('Finance','ဘဏ္ဍာရေး','ဖိုင်နန့်','finance'),
('Logistics','ထောက်ပံ့ပို့ဆောင်ရေး','လော်ဂျစ်စတစ်','logistics'),
('Human Resources','လူ့စွမ်းအားအရင်းအမြစ်','အိတ်ချ်အာရ်','hr'),
('E-commerce','အီလက်ထရွန်းနစ် ကုန်သွယ်ရေး','အီးကောမာ့စ်','ecommerce'),
('SME','အသေးစားနှင့် အလတ်စား စီးပွားရေးလုပ်ငန်းများ','အက်စ်အမ်အီး','sme'),
('POS','ရောင်းချသည့်နေရာ (ပွိုင့်အော့ဖ်ဆဲလ်)','ပေါ့စ်','sme'),
('Invoice','ငွေတောင်းခံလွှာ (ပြေစာ)','အင်ဗွိုက်','finance'),
('Shipment','ကုန်စည်ပို့ဆောင်မှု','ရှစ်ပ်မင့်','logistics'),
('Commercial Tax','ကုန်သွယ်ခွန်','စီတီ','finance'),
('Corporate Income Tax','ကော်ပိုရိတ် ဝင်ငွေခွန်','စီအိုင်တီ','finance'),
('Withholding Tax','ထိန်းသိမ်းခွန်','ဝှစ်ဟိုးလ်ဒင်း','finance'),
('Advance Income Tax','ကြိုတင်ဝင်ငွေခွန်','အေအိုင်တီ','finance'),
('Border Trade Station','နယ်စပ်ကုန်သွယ်ရေးစခန်း','ဘော်ဒါ','logistics'),
('Customs','အကောက်ခွန်','ကတ်စတမ်','logistics'),
('Industrial Zone','စက်မှုဇုန်','အင်ဒပ်စထရီယယ်လ် ဇုန်','logistics'),
('Special Economic Zone','အထူးစီးပွားရေးဇုန်','အက်စ်အီးဇက်','logistics');

-- =============================================================================
-- 7. PRODUCTION INDEXES (Query Performance)
-- =============================================================================
CREATE INDEX IF NOT EXISTS idx_erp_townships_zone ON erp_townships(delivery_zone);
CREATE INDEX IF NOT EXISTS idx_erp_townships_region ON erp_townships(region_state);
CREATE INDEX IF NOT EXISTS idx_erp_townships_active ON erp_townships(is_active);
CREATE INDEX IF NOT EXISTS idx_erp_tax_rates_type ON erp_tax_rates(tax_type);
CREATE INDEX IF NOT EXISTS idx_erp_tax_rates_active ON erp_tax_rates(is_active);
CREATE INDEX IF NOT EXISTS idx_erp_border_stations_country ON erp_border_trade_stations(country, status);
CREATE INDEX IF NOT EXISTS idx_erp_business_terms_domain ON erp_business_terms(domain);

-- =============================================================================
-- 8. BUSINESS VIEWS (Safe API Endpoints)
-- =============================================================================
CREATE OR REPLACE VIEW v_active_townships AS
SELECT 
    township_code, 
    name_en, 
    name_mm, 
    region_state, 
    delivery_zone, 
    delivery_fee_mmk, 
    estimated_delivery_days
FROM erp_townships 
WHERE is_active = TRUE;

CREATE OR REPLACE VIEW v_current_tax_rates AS
SELECT 
    tax_type, 
    tax_name_en, 
    rate, 
    filing_frequency, 
    notes
FROM erp_tax_rates 
WHERE is_active = TRUE;

CREATE OR REPLACE VIEW v_active_border_stations AS
SELECT 
    station_name, 
    country, 
    notes
FROM erp_border_trade_stations 
WHERE status = 'Active';

-- =============================================================================
-- END OF ERP MASTER DATA SCHEMA
-- Execute with: psql -U erp_user -d erp_database -f erp_myanmar_master_data.sql
-- =============================================================================
