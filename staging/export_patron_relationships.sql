
    CREATE TABLE staging.export_patron_relationships (
    patron1_id VARCHAR(5) NOT NULL,
first_name_1 VARCHAR(9) NULL,
last_name_1 VARCHAR(9) NULL,
company_1 VARCHAR(255) NULL,
relation_1 VARCHAR(21) NOT NULL,
patron2_id VARCHAR(5) NOT NULL,
first_name_2 VARCHAR(9) NULL,
last_name_2 VARCHAR(13) NULL,
company_2 VARCHAR(38) NULL,
relation_2 VARCHAR(21) NOT NULL,
relationship_note VARCHAR(50) NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    