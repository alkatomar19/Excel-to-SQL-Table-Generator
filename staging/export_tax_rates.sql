
    CREATE TABLE staging.export_tax_rates (
    tax_rate_id VARCHAR(1) NOT NULL,
tax_rate VARCHAR(6) NOT NULL,
tax_1_city BIT NOT NULL,
tax_2_pst BIT NOT NULL,
tax_3_gst DECIMAL(3,2) NOT NULL,
tax_1_number VARCHAR(50) NULL,
tax_2_number VARCHAR(50) NULL,
tax_3_number VARCHAR(50) NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    