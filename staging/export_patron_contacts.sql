
    IF NOT EXISTS (
    SELECT 1
    FROM sys.tables t
    JOIN sys.schemas s ON t.schema_id = s.schema_id
    WHERE t.name = 'export_patron_contacts'
      AND s.name = 'staging'
    )
    BEGIN
        CREATE TABLE staging.export_patron_contacts (
    id INT IDENTITY(1,1) PRIMARY KEY,
patron_id INT NULL,
first_name VARCHAR(20) NULL,
last_name VARCHAR(22) NULL,
company VARCHAR(255) NULL,
contact_info_id INT NULL,
type VARCHAR(7) NULL,
location VARCHAR(8) NULL,
contactinfo VARCHAR(47) NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    END
    GO
    