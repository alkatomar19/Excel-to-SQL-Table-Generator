
    CREATE TABLE staging.export_venue_pricing_map_seat_names (
    map_seat_id VARCHAR(5) NOT NULL,
pricing_map_id VARCHAR(2) NOT NULL,
logical_seat VARCHAR(3) NOT NULL,
door VARCHAR(50) NULL,
seat_section VARCHAR(5) NOT NULL,
seat_row VARCHAR(2) NOT NULL,
seat_number VARCHAR(2) NOT NULL,
seat_note VARCHAR(39) NULL,
price_codes_available VARCHAR(17) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    