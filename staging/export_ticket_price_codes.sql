
    CREATE TABLE staging.export_ticket_price_codes (
    id INT IDENTITY(1,1) PRIMARY KEY,
year VARCHAR(4) NOT NULL,
event_id VARCHAR(4) NOT NULL,
event_code VARCHAR(6) NOT NULL,
title VARCHAR(255) NOT NULL,
performance_id VARCHAR(4) NOT NULL,
performance_code VARCHAR(8) NOT NULL,
performance_date VARCHAR(10) NOT NULL,
performance_time VARCHAR(8) NOT NULL,
price_code VARCHAR(1) NOT NULL,
price_code_description VARCHAR(20) NOT NULL,
active BIT NOT NULL,
base_price DECIMAL(7,2) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    