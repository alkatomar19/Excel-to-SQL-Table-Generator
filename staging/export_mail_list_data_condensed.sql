
    IF NOT EXISTS (
    SELECT 1
    FROM sys.tables t
    JOIN sys.schemas s ON t.schema_id = s.schema_id
    WHERE t.name = 'export_mail_list_data_condensed'
      AND s.name = 'staging'
    )
    BEGIN
        CREATE TABLE staging.export_mail_list_data_condensed (
    id INT IDENTITY(1,1) PRIMARY KEY,
mail_list_id VARCHAR(3) NOT NULL,
patron_id VARCHAR(5) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    END
    GO
    