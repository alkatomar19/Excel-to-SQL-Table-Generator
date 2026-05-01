
    IF NOT EXISTS (
    SELECT 1
    FROM sys.tables t
    JOIN sys.schemas s ON t.schema_id = s.schema_id
    WHERE t.name = 'export_mail_lists'
      AND s.name = 'staging'
    )
    BEGIN
        CREATE TABLE staging.export_mail_lists (
    mail_list_id VARCHAR(3) NOT NULL,
mail_list_name VARCHAR(47) NOT NULL,
active BIT NOT NULL,
employee_vip_notifications BIT NOT NULL,
mail_list_description VARCHAR(255) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    END
    GO
    