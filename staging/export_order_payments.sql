
    CREATE TABLE staging.export_order_payments (
    patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(20) NULL,
last_name VARCHAR(21) NULL,
company VARCHAR(255) NULL,
payment_id VARCHAR(6) NOT NULL,
source VARCHAR(16) NOT NULL,
date_received VARCHAR(10) NOT NULL,
total_paid DECIMAL(7,2) NOT NULL,
payment_method VARCHAR(20) NOT NULL,
check_voucher_id VARCHAR(18) NULL,
pass_used_qty VARCHAR(1) NOT NULL,
redeemed_by_pass_control_id VARCHAR(10) NULL,
gift_desc VARCHAR(50) NULL,
gift_appraiser VARCHAR(50) NULL,
appraiser_address VARCHAR(50) NULL,
date_deposited VARCHAR(10) NOT NULL,
deposit_number VARCHAR(4) NOT NULL,
gl_journal_posting VARCHAR(10) NOT NULL,
order_id VARCHAR(6) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    