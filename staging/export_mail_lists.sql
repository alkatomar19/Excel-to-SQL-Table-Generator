
    CREATE TABLE staging.export_mail_lists (
    mail_list_id VARCHAR(3) NOT NULL,
mail_list_name VARCHAR(47) NOT NULL,
active BIT NOT NULL,
employee_vip_notifications BIT NOT NULL,
mail_list_description VARCHAR(255) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    