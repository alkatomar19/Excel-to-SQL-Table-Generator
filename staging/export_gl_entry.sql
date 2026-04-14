
    CREATE TABLE staging.export_gl_entry (
    id INT IDENTITY(1,1) PRIMARY KEY,
gl_reference VARCHAR(10) NOT NULL,
gl_date VARCHAR(10) NOT NULL,
gl_description VARCHAR(255) NOT NULL,
account VARCHAR(12) NOT NULL,
line_memo VARCHAR(255) NOT NULL,
event_code VARCHAR(6) NULL,
campaign_name VARCHAR(22) NULL,
pass_description VARCHAR(17) NULL,
fee_description VARCHAR(36) NULL,
resource_code VARCHAR(19) NULL,
tax_code VARCHAR(6) NULL,
debit DECIMAL(8,2) NOT NULL,
credit DECIMAL(9,2) NOT NULL,
gl_posted_date VARCHAR(19) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    