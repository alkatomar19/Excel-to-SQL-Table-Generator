
    CREATE TABLE staging.export_patron_task_notes (
    id INT IDENTITY(1,1) PRIMARY KEY,
patron_id VARCHAR(5) NOT NULL,
first_name VARCHAR(10) NULL,
last_name VARCHAR(14) NULL,
company VARCHAR(38) NULL,
task_id VARCHAR(4) NOT NULL,
calendar_type VARCHAR(8) NOT NULL,
task_type VARCHAR(38) NOT NULL,
date_begin VARCHAR(19) NULL,
date_end VARCHAR(19) NOT NULL,
date_completed VARCHAR(19) NULL,
status VARCHAR(8) NOT NULL,
description VARCHAR(48) NOT NULL,
notes VARCHAR(255) NULL,
created_at DATETIME DEFAULT GETDATE()
    );
    