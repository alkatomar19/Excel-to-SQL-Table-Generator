
    CREATE TABLE staging.export_volunteer_flags (
    patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(14) NULL,
last_name VARCHAR(16) NULL,
company VARCHAR(38) NULL,
hair_colour VARCHAR(50) NULL,
eye_colour VARCHAR(50) NULL,
vocal_range VARCHAR(50) NULL,
instrument VARCHAR(50) NULL,
flag_dance BIT NOT NULL,
flag_sing BIT NOT NULL,
flag_act BIT NOT NULL,
flag_play_instrument BIT NOT NULL,
volunteer_note VARCHAR(38) NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    