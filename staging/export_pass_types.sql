
    CREATE TABLE staging.export_pass_types (
    pass_type_id VARCHAR(2) NOT NULL,
pass_description VARCHAR(36) NOT NULL,
pass_description_external VARCHAR(36) NOT NULL,
redemption_type VARCHAR(16) NOT NULL,
active BIT NOT NULL,
start_date VARCHAR(19) NULL,
end_date VARCHAR(19) NULL,
tax_rate VARCHAR(6) NOT NULL,
number_of_passes_issued VARCHAR(2) NOT NULL,
purchase_amount DECIMAL(4,2) NOT NULL,
notes_external VARCHAR(255) NULL,
notes_internal VARCHAR(50) NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    