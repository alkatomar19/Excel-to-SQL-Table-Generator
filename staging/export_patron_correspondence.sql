
    CREATE TABLE staging.export_patron_correspondence (
    patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(18) NULL,
last_name VARCHAR(21) NULL,
company VARCHAR(255) NULL,
letter_type_id VARCHAR(2) NOT NULL,
letter_name VARCHAR(40) NOT NULL,
letter_id VARCHAR(6) NOT NULL,
email_subject VARCHAR(255) NOT NULL,
letter_date VARCHAR(19) NOT NULL,
date_sent_or_printed VARCHAR(19) NOT NULL,
letter_notes VARCHAR(50) NULL,
donation_id BIT NOT NULL,
order_id VARCHAR(6) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    