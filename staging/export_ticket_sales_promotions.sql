
    CREATE TABLE staging.export_ticket_sales_promotions (
    sales_promotion_id VARCHAR(4) NOT NULL,
promotion_internal VARCHAR(40) NOT NULL,
promotion_external VARCHAR(40) NOT NULL,
start_date VARCHAR(19) NULL,
end_date VARCHAR(19) NULL,
active BIT NOT NULL,
disc_amt DECIMAL(5,2) NOT NULL,
disc_pct DECIMAL(3,2) NOT NULL,
markup_amt BIT NOT NULL,
markup_pct BIT NOT NULL,
fee_1_surcharge DECIMAL(3,2) NOT NULL,
fee_2_6_pct_net_sales BIT NOT NULL,
fee_3 DECIMAL(4,2) NOT NULL,
promotion_type VARCHAR(12) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    