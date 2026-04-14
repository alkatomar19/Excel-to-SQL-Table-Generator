
    CREATE TABLE staging.export_order_data (
    patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(20) NULL,
last_name VARCHAR(21) NULL,
company VARCHAR(255) NULL,
order_id VARCHAR(6) NOT NULL,
order_date VARCHAR(10) NOT NULL,
order_reason_to_buy VARCHAR(27) NULL,
tix_comment VARCHAR(16) NULL,
order_notes_internal VARCHAR(1000) NULL,
order_notes_external VARCHAR(1000) NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    