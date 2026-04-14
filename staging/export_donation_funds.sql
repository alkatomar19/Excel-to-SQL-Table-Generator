
    CREATE TABLE staging.export_donation_funds (
    donation_campaign_id BIT NOT NULL,
donation_campaign_name VARCHAR(22) NOT NULL,
start_date VARCHAR(50) NULL,
end_date VARCHAR(50) NULL,
number_donations_received VARCHAR(4) NOT NULL,
total_prospect BIT NOT NULL,
total_pledge DECIMAL(8,2) NOT NULL,
total_actual DECIMAL(8,2) NOT NULL,
total_match_gift BIT NOT NULL,
total_soft_credit BIT NOT NULL,
notes_external VARCHAR(1000) NOT NULL,
notes_internal VARCHAR(50) NULL,
giving_level_matrix_id BIT NOT NULL,
giving_level_matrix_description VARCHAR(14) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    