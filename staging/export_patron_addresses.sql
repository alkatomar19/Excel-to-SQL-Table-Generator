
    CREATE TABLE staging.export_patron_addresses (
    id INT IDENTITY(1,1) PRIMARY KEY,
patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(31) NULL,
last_name VARCHAR(22) NULL,
company VARCHAR(255) NULL,
address_id VARCHAR(5) NOT NULL,
location VARCHAR(8) NOT NULL,
address_line_1 VARCHAR(50) NULL,
address_line_2 VARCHAR(30) NULL,
city VARCHAR(30) NULL,
province VARCHAR(11) NULL,
postal_code VARCHAR(10) NULL,
country VARCHAR(9) NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    