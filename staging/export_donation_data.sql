
    CREATE TABLE staging.export_donation_data (
    patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(18) NULL,
last_name VARCHAR(18) NULL,
company VARCHAR(41) NULL,
donation_campaign_id BIT NOT NULL,
campaign_name VARCHAR(22) NOT NULL,
donation_id VARCHAR(4) NOT NULL,
fiscal_year VARCHAR(4) NOT NULL,
program_year VARCHAR(4) NOT NULL,
corporate BIT NOT NULL,
donation_type VARCHAR(21) NOT NULL,
donation_date VARCHAR(10) NOT NULL,
pledge_amount DECIMAL(6,2) NOT NULL,
actual_amount DECIMAL(6,2) NOT NULL,
program_name VARCHAR(40) NULL,
donor_why_patron_gave VARCHAR(16) NULL,
match_gift BIT NOT NULL,
match_amount BIT NOT NULL,
soft_credit_amount BIT NOT NULL,
donation_balance_due BIT NOT NULL,
donation_notes VARCHAR(255) NULL,
match_to_donation_id BIT NOT NULL,
recurring_donation_profile_id BIT NOT NULL,
order_id VARCHAR(6) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    