#!/bin/bash
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL

    CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';
    CREATE DATABASE $APP_DB_NAME;
    GRANT ALL PRIVILEGES ON DATABASE $APP_DB_NAME TO $APP_DB_USER;
    \c $APP_DB_NAME $APP_DB_USER
    BEGIN;

        SET client_encoding = 'LATIN1';

        CREATE TABLE IF NOT EXISTS products (
            code VARCHAR(10) NOT NULL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price NUMERIC(10,2) NOT NULL
        );

        INSERT INTO products (code, name, price) VALUES('PEN', 'Lana Pen', 5.00);
        INSERT INTO products (code, name, price) VALUES('TSHIRT', 'Lana T-Shirt', 20.00);
        INSERT INTO products (code, name, price) VALUES('MUG', 'Lana Coffee Mug', 7.50);

    COMMIT;
EOSQL