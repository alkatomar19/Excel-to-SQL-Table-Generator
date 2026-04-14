
    CREATE TABLE staging.export_mail_list_data_compact (
    id INT IDENTITY(1,1) PRIMARY KEY,
mail_list_id VARCHAR(3) NOT NULL,
mail_list_name VARCHAR(47) NOT NULL,
patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(31) NULL,
last_name VARCHAR(21) NULL,
company VARCHAR(255) NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    