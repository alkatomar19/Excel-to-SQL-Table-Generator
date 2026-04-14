
    CREATE TABLE staging.export_season_package_data (
    patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(15) NULL,
last_name VARCHAR(18) NULL,
company VARCHAR(38) NULL,
season_package_id VARCHAR(1) NOT NULL,
year VARCHAR(4) NOT NULL,
package VARCHAR(35) NOT NULL,
season_subscription_id VARCHAR(4) NOT NULL,
series VARCHAR(7) NOT NULL,
seat_count VARCHAR(2) NOT NULL,
status VARCHAR(16) NOT NULL,
date_renewed VARCHAR(10) NULL,
change_request_notes VARCHAR(255) NULL,
auto_renew BIT NOT NULL,
date_patron_started_auto_renew VARCHAR(50) NULL,
auto_renew_payment_frequency VARCHAR(50) NULL,
auto_renew_number_of_payments BIT NOT NULL,
order_id VARCHAR(6) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    