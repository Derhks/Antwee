-- prepares a PostgreSQL server for the project

DROP DATABASE IF EXISTS antwee_db;
CREATE DATABASE antwee_db;
DROP USER IF EXISTS derhks;
CREATE USER derhks WITH ENCRYPTED PASSWORD 'H2sh1r2m2.17';
ALTER ROLE derhks SET client_encoding TO 'utf8';
ALTER ROLE derhks SET default_transaction_isolation TO 'read committed';
ALTER ROLE derhks SET default_transaction_isolation TO 'read committed';
GRANT ALL PRIVILEGES ON DATABASE antwee_db TO derhks;
