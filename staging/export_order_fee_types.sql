
    CREATE TABLE staging.export_order_fee_types (
    order_fee_id VARCHAR(2) NOT NULL,
fee_description_internal VARCHAR(36) NOT NULL,
fee_description_external VARCHAR(36) NOT NULL,
start_date VARCHAR(19) NULL,
end_date VARCHAR(19) NULL,
active BIT NOT NULL,
fixed_amount DECIMAL(5,2) NOT NULL,
percentage_of_items_in_cart BIT NOT NULL,
maximum_amount BIT NOT NULL,
base_price_item_minimum BIT NOT NULL,
base_price_item_maximum DECIMAL(11,2) NOT NULL,
tax_rate VARCHAR(6) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    