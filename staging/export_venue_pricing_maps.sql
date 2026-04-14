
    CREATE TABLE staging.export_venue_pricing_maps (
    venue_id VARCHAR(2) NOT NULL,
venue_name_internal VARCHAR(49) NOT NULL,
venue_name_external VARCHAR(50) NOT NULL,
address_1 VARCHAR(35) NOT NULL,
address_2 VARCHAR(18) NULL,
city VARCHAR(13) NOT NULL,
province VARCHAR(2) NOT NULL,
postal_code VARCHAR(7) NOT NULL,
country VARCHAR(6) NOT NULL,
pricing_map_id VARCHAR(2) NOT NULL,
pricing_map_name VARCHAR(50) NOT NULL,
capacity VARCHAR(6) NOT NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    