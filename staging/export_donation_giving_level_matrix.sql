
    CREATE TABLE staging.export_donation_giving_level_matrix (
    giving_level_matrix_id BIT NOT NULL,
giving_level_matrix_description VARCHAR(14) NOT NULL,
giving_level VARCHAR(9) NOT NULL,
giving_level_from DECIMAL(5,2) NOT NULL,
giving_level_to DECIMAL(9,2) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    