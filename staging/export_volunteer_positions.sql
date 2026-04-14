
    CREATE TABLE staging.export_volunteer_positions (
    id INT IDENTITY(1,1) PRIMARY KEY,
patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(14) NULL,
last_name VARCHAR(16) NULL,
company VARCHAR(38) NULL,
volunteer_position VARCHAR(22) NOT NULL,
last_contact VARCHAR(10) NOT NULL,
do_it_again BIT NOT NULL,
volunteer_note VARCHAR(32) NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    