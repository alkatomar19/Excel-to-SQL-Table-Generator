
    IF NOT EXISTS (
    SELECT 1
    FROM sys.tables t
    JOIN sys.schemas s ON t.schema_id = s.schema_id
    WHERE t.name = 'export_donation_receipts'
      AND s.name = 'staging'
    )
    BEGIN
        CREATE TABLE staging.export_donation_receipts (
    patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(18) NULL,
last_name VARCHAR(18) NULL,
company VARCHAR(41) NULL,
receipt_date VARCHAR(10) NOT NULL,
receipt_number BIT NOT NULL,
receipt_amount DECIMAL(6,2) NOT NULL,
printed_date VARCHAR(50) NULL,
receipt_required BIT NOT NULL,
donation_id VARCHAR(4) NOT NULL,
donation_campaign_id BIT NOT NULL,
campaign_name VARCHAR(22) NOT NULL,
payment_id VARCHAR(6) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    END
    GO
    