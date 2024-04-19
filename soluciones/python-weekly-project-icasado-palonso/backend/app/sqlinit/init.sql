CREATE TABLE IF NOT EXISTS TASKS(
    id SERIAL PRIMARY KEY,
    TITLE VARCHAR(255),
    DESCRIPTION VARCHAR(255),
    CREATED TIMESTAMP DEFAULT NOW(),
    DONE BOOLEAN DEFAULT FALSE
);
