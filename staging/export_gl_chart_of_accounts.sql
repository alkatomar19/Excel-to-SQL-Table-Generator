
    CREATE TABLE staging.export_gl_chart_of_accounts (
    type VARCHAR(13) NOT NULL,
account VARCHAR(12) NOT NULL,
external_account VARCHAR(13) NOT NULL,
account_description VARCHAR(40) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    