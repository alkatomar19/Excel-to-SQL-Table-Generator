
    CREATE TABLE staging.export_volunteer_history (
    id INT IDENTITY(1,1) PRIMARY KEY,
patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(14) NULL,
last_name VARCHAR(16) NULL,
company VARCHAR(38) NULL,
year VARCHAR(4) NOT NULL,
volunteer_position VARCHAR(22) NOT NULL,
role VARCHAR(40) NULL,
duties VARCHAR(255) NULL,
start_date VARCHAR(19) NOT NULL,
end_date VARCHAR(19) NOT NULL,
hours DECIMAL(6,2) NOT NULL,
event_code VARCHAR(6) NULL,
event_series VARCHAR(8) NULL,
evaluation VARCHAR(14) NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    