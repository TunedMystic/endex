# Stock.
('CREATE TABLE IF NOT EXISTS "stock" ("id" SERIAL NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL, "cusip" VARCHAR(9), "isin" VARCHAR(12), "street" VARCHAR(255), "city" VARCHAR(255), "zipcode" VARCHAR(255), "country" VARCHAR(2), "asset_hash" VARCHAR(40), "symbol" VARCHAR(10) NOT NULL, "exchange_id" INTEGER, "description" TEXT, "date_founded" DATE, "date_listed" DATE, "website" DATE, "email" VARCHAR(255), "phone" VARCHAR(255), "sector_id" INTEGER, "industry_id" INTEGER, "shares_float" NUMERIC(12, 0), "shares_outstanding" NUMERIC(12, 0), "held_by_institutions" NUMERIC(6, 5), "held_by_insiders" NUMERIC(6, 5), FOREIGN KEY ("exchange_id") REFERENCES "exchange" ("id"), FOREIGN KEY ("sector_id") REFERENCES "sector" ("id"), FOREIGN KEY ("industry_id") REFERENCES "industry" ("id"))', [])
('CREATE INDEX IF NOT EXISTS "stock_exchange_id" ON "stock" ("exchange_id")', [])
('CREATE INDEX IF NOT EXISTS "stock_sector_id" ON "stock" ("sector_id")', [])
('CREATE INDEX IF NOT EXISTS "stock_industry_id" ON "stock" ("industry_id")', [])

# Etf.
('CREATE TABLE IF NOT EXISTS "etf" ("id" SERIAL NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL, "cusip" VARCHAR(9), "isin" VARCHAR(12), "asset_hash" VARCHAR(40), "symbol" VARCHAR(10) NOT NULL, "exchange_id" INTEGER, "description" TEXT, "date_founded" DATE, "date_listed" DATE, "website" DATE, "email" VARCHAR(255), "phone" VARCHAR(255), "issuer_id" INTEGER, "category_id" INTEGER, "market_index_id" INTEGER, "leverage" INTEGER, "total_assets" NUMERIC(12, 0), FOREIGN KEY ("exchange_id") REFERENCES "exchange" ("id"), FOREIGN KEY ("issuer_id") REFERENCES "etfissuer" ("id"), FOREIGN KEY ("category_id") REFERENCES "category" ("id"), FOREIGN KEY ("market_index_id") REFERENCES "marketindex" ("id"))', [])
('CREATE INDEX IF NOT EXISTS "etf_exchange_id" ON "etf" ("exchange_id")', [])
('CREATE INDEX IF NOT EXISTS "etf_issuer_id" ON "etf" ("issuer_id")', [])
('CREATE INDEX IF NOT EXISTS "etf_category_id" ON "etf" ("category_id")', [])
('CREATE INDEX IF NOT EXISTS "etf_market_index_id" ON "etf" ("market_index_id")', [])

# Exchange, MarketIndex, Category, EtfIssuer, Sector, Industry.
('CREATE TABLE IF NOT EXISTS "exchange" ("id" SERIAL NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL)', [])
('CREATE TABLE IF NOT EXISTS "marketindex" ("id" SERIAL NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL)', [])
('CREATE TABLE IF NOT EXISTS "category" ("id" SERIAL NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL)', [])
('CREATE TABLE IF NOT EXISTS "etfissuer" ("id" SERIAL NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL)', [])
('CREATE TABLE IF NOT EXISTS "sector" ("id" SERIAL NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL)', [])
('CREATE TABLE IF NOT EXISTS "industry" ("id" SERIAL NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL)', [])


# -------------------------------------------------------------------
