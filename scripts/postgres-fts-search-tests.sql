-- SELECT s.symbol, s.name FROM stock s
-- WHERE (
-- 	s.symbol LIKE UPPER('%ok') OR
-- 	LOWER(s.name) LIKE LOWER('rob%')
-- )
-- LIMIT 10;

-- 


SELECT * FROM (
    (
        SELECT s.symbol, s.name, 'stock' AS asset_type FROM stock s
        WHERE (
            s.symbol LIKE UPPER('%ok') OR
            LOWER(s.name) LIKE LOWER('rob%')
        )
        LIMIT 10
    )
    UNION ALL
    (
        SELECT e.symbol, e.name, 'etf' AS asset_type FROM etf e
        WHERE (
            e.symbol LIKE UPPER('%ok') OR
            LOWER(e.name) LIKE LOWER('rob%')
        )
        LIMIT 10
    )
) AS foo;

-- -------------------------------------------------------------------------------------
-- -------------------------------------------------------------------------------------
-- -------------------------------------------------------------------------------------
-- -------------------------------------------------------------------------------------
-- -------------------------------------------------------------------------------------

-- Full Text Search PostgreSQL
-- Ref: https://www.youtube.com/watch?v=szfUbzsKvtE

SELECT * FROM (
    (
        SELECT s.symbol, s.name, 'stock' AS asset_type FROM stock s
        WHERE (
            s.symbol LIKE UPPER('%ok') OR
            LOWER(s.name) LIKE LOWER('rob%')
        )
        LIMIT 10
    )
    UNION ALL
    (
        SELECT e.symbol, e.name, 'etf' AS asset_type FROM etf e
        WHERE (
            e.symbol LIKE UPPER('%ok') OR
            LOWER(e.name) LIKE LOWER('rob%')
        )
        LIMIT 10
    )
) AS foo;


---


SELECT name, description, type
FROM cards
WHERE to_tsvector(name) @@ to_tsquery('Wall');

---

SELECT name, description, type
FROM cards
WHERE to_tsvector(name || ' ' || description) @@ to_tsquery('Wall');

---

-- Add document column to cards table.
ALTER TABLE cards
	ADD COLUMN document tsvector;

-- Update document column with computed tsvector values.
UPDATE cards
	SET document = to_tsvector(name || ' ' || description);

---

-- Query with precomputed document column.
SELECT name, description, type
FROM cards
WHERE document @@ to_tsquery('Spirit')
LIMIT 10;

---

EXPLAIN ANALYZE SELECT name, description, type
FROM cards
WHERE to_tsvector(name || ' ' || description) @@ to_tsquery('Wall') LIMIT 10;

---

EXPLAIN ANALYZE SELECT name, description, type
FROM cards
WHERE document @@ to_tsquery('Spirit')
LIMIT 10;

---

-- Create a GIN (Generalized Inverted Index)-based index on document column.
CREATE INDEX document_idx
ON cards
USING GIN (document);

--

EXPLAIN ANALYZE SELECT name, description, type FROM cards
WHERE document @@ to_tsquery('Spirit') LIMIT 10;

--

-- Rank results, show rank value

SELECT name, description, type, ts_rank(document, plainto_tsquery('target'))
FROM cards
WHERE document @@ plainto_tsquery('target')
ORDER BY ts_rank(document, plainto_tsquery('target')) DESC;

-- -------------------------------------------------------------------------------------
-- -------------------------------------------------------------------------------------
-- -------------------------------------------------------------------------------------
-- -------------------------------------------------------------------------------------
-- -------------------------------------------------------------------------------------


-- Perform full text search on Stock (before 'document' column).

SELECT s.id, s.symbol, s.name
FROM stock s
WHERE to_tsvector(s.symbol || ' ' || s.name) @@ plainto_tsquery('group')
LIMIT 10;

-- Perform full text search on Stock (after 'document' column).

EXPLAIN ANALYZE SELECT s.id, s.symbol, s.name
FROM stock s
WHERE s.document @@ plainto_tsquery('group')
LIMIT 10;

-- Create new column 'document' on Stock.

ALTER TABLE stock
ADD COLUMN document tsvector;

-- Update new 'document' column with tsvector values.

UPDATE stock s
SET document = to_tsvector(s.symbol || ' ' || s.name);

-- Create GIN (Generalized Inverted Index)-based index on 'document' column.

CREATE INDEX stock_document_idx
ON stock
USING GIN(document);

-- ------------------------------------

ALTER TABLE etf ADD COLUMN document tsvector;
UPDATE etf e SET document = to_tsvector(e.symbol || ' ' || e.name);
CREATE INDEX etf_document_idx ON etf USING GIN(document);
SELECT e.id, e.symbol, e.name FROM etf e WHERE e.document @@ plainto_tsquery('group') LIMIT 10;

-- ------------------------------------
-- Union tests
-- Ref: https://dba.stackexchange.com/a/157982

SELECT * FROM (
(
    SELECT s.id, s.symbol, s.name, 'stock' as type, ts_rank(s.document, to_tsquery('simple', 'car:*')) as rank
    FROM stock s
    WHERE s.document @@ to_tsquery('simple', 'car:*')
    ORDER BY ts_rank(s.document, to_tsquery('simple', 'car:*')) DESC LIMIT 10
)
UNION ALL
(
    SELECT e.id, e.symbol, e.name, 'etf' as type, ts_rank(e.document, to_tsquery('simple', 'car:*')) as rank
    FROM etf e
    WHERE e.document @@ to_tsquery('simple', 'car:*')
    ORDER BY ts_rank(e.document, to_tsquery('simple', 'car:*')) DESC LIMIT 10
)
) AS RESULTS ORDER BY rank DESC;










