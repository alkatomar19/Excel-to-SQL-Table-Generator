-- Run all staging tables

IF NOT EXISTS (
    SELECT * FROM sys.schemas WHERE name = 'staging'
)
BEGIN
    EXEC('CREATE SCHEMA staging')
END
GO

:r .\staging\export_donation_data.sql
:r .\staging\export_donation_funds.sql
:r .\staging\export_donation_giving_level_matrix.sql
:r .\staging\export_donation_receipts.sql
:r .\staging\export_gl_chart_of_accounts.sql
:r .\staging\export_gl_entry.sql
:r .\staging\export_mail_lists.sql
:r .\staging\export_mail_list_data_compact.sql
:r .\staging\export_mail_list_data_condensed.sql
:r .\staging\export_mail_list_data_full.sql
:r .\staging\export_order_data.sql
:r .\staging\export_order_fees.sql
:r .\staging\export_order_fee_types.sql
:r .\staging\export_order_payments.sql
:r .\staging\export_pass_data.sql
:r .\staging\export_pass_types.sql
:r .\staging\export_patron_addresses.sql
:r .\staging\export_patron_contacts.sql
:r .\staging\export_patron_correspondence.sql
:r .\staging\export_patron_data.sql
:r .\staging\export_patron_relationships.sql
:r .\staging\export_patron_task_notes.sql
:r .\staging\export_season_package_data.sql
:r .\staging\export_tax_rates.sql
:r .\staging\export_tickets.sql
:r .\staging\export_ticket_event_performances.sql
:r .\staging\export_ticket_price_codes.sql
:r .\staging\export_ticket_sales_promotions.sql
:r .\staging\export_venue_pricing_maps.sql
:r .\staging\export_venue_pricing_map_seat_names.sql
:r .\staging\export_volunteer_flags.sql
:r .\staging\export_volunteer_history.sql
:r .\staging\export_volunteer_positions.sql
