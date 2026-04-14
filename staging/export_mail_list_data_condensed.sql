
    CREATE TABLE staging.export_mail_list_data_condensed (
    id INT IDENTITY(1,1) PRIMARY KEY,
mail_list_id VARCHAR(3) NOT NULL,
patron_id VARCHAR(5) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    