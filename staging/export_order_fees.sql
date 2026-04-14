
    CREATE TABLE staging.export_order_fees (
    patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(20) NULL,
last_name VARCHAR(21) NULL,
company VARCHAR(255) NULL,
order_fee_type_id VARCHAR(2) NOT NULL,
fee_name VARCHAR(36) NOT NULL,
order_fee_id VARCHAR(5) NOT NULL,
fee_date VARCHAR(19) NOT NULL,
amount DECIMAL(5,2) NOT NULL,
tax_rate VARCHAR(6) NOT NULL,
tax_1_city BIT NOT NULL,
tax_2_pst BIT NOT NULL,
tax_3_gst DECIMAL(3,2) NOT NULL,
fee_total DECIMAL(4,1) NOT NULL,
order_id VARCHAR(6) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    