-- Create user.
CREATE USER "endex" WITH PASSWORD 'endex';
ALTER USER "endex" WITH SUPERUSER;

-- Create database.
CREATE DATABASE "endex";
GRANT ALL PRIVILEGES ON DATABASE "endex" to "endex";
