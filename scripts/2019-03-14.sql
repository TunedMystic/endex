-- Select random row from table.

-- Ref: https://stackoverflow.com/a/51916026
CREATE EXTENSION IF NOT EXISTS tsm_system_rows;
SELECT s.id FROM stock s TABLESAMPLE SYSTEM_ROWS(1);

-- Slower way to select random row from a table.
SELECT s.id FROM stock s ORDER BY random() LIMIT 1;

-- Select indexes for a table.
SELECT * FROM pg_indexes;
SELECT * FROM pg_indexes WHERE tablename = 'stock';

-- ------------------------------------------------------------------

-- Create user.
CREATE USER "endex" WITH PASSWORD 'endex';

-- Create database.
CREATE DATABASE "endex";
GRANT ALL PRIVILEGES ON DATABASE "endex" to "endex";

-- Create schema.
CREATE SCHEMA IF NOT EXISTS "endex";
ALTER SCHEMA "endex" OWNER TO "endex";

-- Create tables.
CREATE TABLE IF NOT EXISTS "exchange" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "symbol" VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS "marketindex" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "etfissuer" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "category" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "sector" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "industry" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "stock" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "asset_hash" VARCHAR(40),
    "symbol" VARCHAR(10) NOT NULL,
    "name" VARCHAR(255) NOT NULL,

    "description" TEXT,
    "date_founded" DATE,
    "date_listed" DATE,
    "website" VARCHAR(255),
    "email" VARCHAR(255),
    "phone" VARCHAR(255),

    -- Asset identifier fields.
    "cusip" VARCHAR(9),
    "isin" VARCHAR(12),

    -- Address fields.
    "street" VARCHAR(255),
    "city" VARCHAR(255),
    "zipcode" VARCHAR(255),
    "country" VARCHAR(2),

    -- Stock fields.
    "shares_float" NUMERIC(12, 0),
    "shares_outstanding" NUMERIC(12, 0),
    "held_by_institutions" NUMERIC(6, 5),
    "held_by_insiders" NUMERIC(6, 5),

    -- Foreign key relations.
    "exchange_id" INTEGER REFERENCES "exchange" ("id"),
    "sector_id" INTEGER REFERENCES "sector" ("id"),
    "industry_id" INTEGER REFERENCES "industry" ("id"),

    -- Full text search fields.
    "document" tsvector
);

-- Create GIN index on Stock.document column.
CREATE INDEX "stock_document_idx" ON "stock" USING GIN(document);

CREATE TABLE IF NOT EXISTS "etf" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "asset_hash" VARCHAR(40),
    "symbol" VARCHAR(10) NOT NULL,
    "name" VARCHAR(255) NOT NULL,

    "description" TEXT,
    "date_founded" DATE,
    "date_listed" DATE,
    "website" VARCHAR(255),
    "email" VARCHAR(255),
    "phone" VARCHAR(255),

    -- Asset identifier fields.
    "cusip" VARCHAR(9),
    "isin" VARCHAR(12),

    -- Etf fields.
    "leverage" INTEGER,
    "total_assets" NUMERIC(12, 0),

    -- Foreign key relations.
    "exchange_id" INTEGER REFERENCES "exchange" ("id"),
    "category" INTEGER REFERENCES "category" ("id"),
    "issuer_id" INTEGER REFERENCES "etfissuer" ("id"),
    "marketindex_id" INTEGER REFERENCES "marketindex" ("id"),

    -- Full text search fields.
    "document" tsvector
);

-- Create GIN index on Etf.document column.
CREATE INDEX "etf_document_idx" ON "etf" USING GIN(document);

-- ------------------------------------------------------------------

-- Run the first script to setup user, database and schema.
docker exec -i -e PGPASSWORD=postgres pg psql -U postgres -d postgres < ./scripts/1_setup.sql

-- Run the second script to create tables.
docker exec -i -e PGPASSWORD=endex pg psql -U endex -d endex < ./scripts/2_tables.sql


