
    IF NOT EXISTS (
    SELECT 1
    FROM sys.tables t
    JOIN sys.schemas s ON t.schema_id = s.schema_id
    WHERE t.name = 'export_gl_chart_of_accounts'
      AND s.name = 'staging'
    )
    BEGIN
        CREATE TABLE staging.export_gl_chart_of_accounts (
    type VARCHAR(13) NOT NULL,
account VARCHAR(12) NOT NULL,
external_account VARCHAR(13) NOT NULL,
account_description VARCHAR(40) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    END
    GO
    