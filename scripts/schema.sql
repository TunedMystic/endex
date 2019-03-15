--
-- PostgreSQL database dump
--

-- Dumped from database version 11.2
-- Dumped by pg_dump version 11.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: tsm_system_rows; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS tsm_system_rows WITH SCHEMA public;


--
-- Name: EXTENSION tsm_system_rows; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION tsm_system_rows IS 'TABLESAMPLE method which accepts number of rows as a limit';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.category OWNER TO postgres;

--
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_id_seq OWNER TO postgres;

--
-- Name: category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.category_id_seq OWNED BY public.category.id;


--
-- Name: etf; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.etf (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    cusip character varying(9),
    isin character varying(12),
    asset_hash character varying(40),
    symbol character varying(10) NOT NULL,
    exchange_id integer,
    description text,
    date_founded date,
    date_listed date,
    website date,
    email character varying(255),
    phone character varying(255),
    issuer_id integer,
    category_id integer,
    market_index_id integer,
    leverage integer,
    total_assets numeric(12,0),
    document tsvector
);


ALTER TABLE public.etf OWNER TO postgres;

--
-- Name: etf_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.etf_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.etf_id_seq OWNER TO postgres;

--
-- Name: etf_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.etf_id_seq OWNED BY public.etf.id;


--
-- Name: etfissuer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.etfissuer (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.etfissuer OWNER TO postgres;

--
-- Name: etfissuer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.etfissuer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.etfissuer_id_seq OWNER TO postgres;

--
-- Name: etfissuer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.etfissuer_id_seq OWNED BY public.etfissuer.id;


--
-- Name: exchange; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.exchange (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.exchange OWNER TO postgres;

--
-- Name: exchange_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.exchange_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exchange_id_seq OWNER TO postgres;

--
-- Name: exchange_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.exchange_id_seq OWNED BY public.exchange.id;


--
-- Name: industry; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.industry (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.industry OWNER TO postgres;

--
-- Name: industry_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.industry_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.industry_id_seq OWNER TO postgres;

--
-- Name: industry_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.industry_id_seq OWNED BY public.industry.id;


--
-- Name: marketindex; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.marketindex (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.marketindex OWNER TO postgres;

--
-- Name: marketindex_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.marketindex_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.marketindex_id_seq OWNER TO postgres;

--
-- Name: marketindex_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.marketindex_id_seq OWNED BY public.marketindex.id;


--
-- Name: sector; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sector (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.sector OWNER TO postgres;

--
-- Name: sector_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sector_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sector_id_seq OWNER TO postgres;

--
-- Name: sector_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sector_id_seq OWNED BY public.sector.id;


--
-- Name: stock; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stock (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    cusip character varying(9),
    isin character varying(12),
    street character varying(255),
    city character varying(255),
    zipcode character varying(255),
    country character varying(2),
    asset_hash character varying(40),
    symbol character varying(10) NOT NULL,
    exchange_id integer,
    description text,
    date_founded date,
    date_listed date,
    website date,
    email character varying(255),
    phone character varying(255),
    sector_id integer,
    industry_id integer,
    shares_float numeric(12,0),
    shares_outstanding numeric(12,0),
    held_by_institutions numeric(6,5),
    held_by_insiders numeric(6,5),
    document tsvector
);


ALTER TABLE public.stock OWNER TO postgres;

--
-- Name: stock_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.stock_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stock_id_seq OWNER TO postgres;

--
-- Name: stock_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.stock_id_seq OWNED BY public.stock.id;


--
-- Name: category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category ALTER COLUMN id SET DEFAULT nextval('public.category_id_seq'::regclass);


--
-- Name: etf id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.etf ALTER COLUMN id SET DEFAULT nextval('public.etf_id_seq'::regclass);


--
-- Name: etfissuer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.etfissuer ALTER COLUMN id SET DEFAULT nextval('public.etfissuer_id_seq'::regclass);


--
-- Name: exchange id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exchange ALTER COLUMN id SET DEFAULT nextval('public.exchange_id_seq'::regclass);


--
-- Name: industry id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.industry ALTER COLUMN id SET DEFAULT nextval('public.industry_id_seq'::regclass);


--
-- Name: marketindex id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.marketindex ALTER COLUMN id SET DEFAULT nextval('public.marketindex_id_seq'::regclass);


--
-- Name: sector id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sector ALTER COLUMN id SET DEFAULT nextval('public.sector_id_seq'::regclass);


--
-- Name: stock id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stock ALTER COLUMN id SET DEFAULT nextval('public.stock_id_seq'::regclass);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- Name: etf etf_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.etf
    ADD CONSTRAINT etf_pkey PRIMARY KEY (id);


--
-- Name: etfissuer etfissuer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.etfissuer
    ADD CONSTRAINT etfissuer_pkey PRIMARY KEY (id);


--
-- Name: exchange exchange_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exchange
    ADD CONSTRAINT exchange_pkey PRIMARY KEY (id);


--
-- Name: industry industry_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.industry
    ADD CONSTRAINT industry_pkey PRIMARY KEY (id);


--
-- Name: marketindex marketindex_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.marketindex
    ADD CONSTRAINT marketindex_pkey PRIMARY KEY (id);


--
-- Name: sector sector_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sector
    ADD CONSTRAINT sector_pkey PRIMARY KEY (id);


--
-- Name: stock stock_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stock
    ADD CONSTRAINT stock_pkey PRIMARY KEY (id);


--
-- Name: etf_category_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX etf_category_id ON public.etf USING btree (category_id);


--
-- Name: etf_document_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX etf_document_idx ON public.etf USING gin (document);


--
-- Name: etf_exchange_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX etf_exchange_id ON public.etf USING btree (exchange_id);


--
-- Name: etf_issuer_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX etf_issuer_id ON public.etf USING btree (issuer_id);


--
-- Name: etf_market_index_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX etf_market_index_id ON public.etf USING btree (market_index_id);


--
-- Name: stock_document_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX stock_document_idx ON public.stock USING gin (document);


--
-- Name: stock_exchange_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX stock_exchange_id ON public.stock USING btree (exchange_id);


--
-- Name: stock_industry_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX stock_industry_id ON public.stock USING btree (industry_id);


--
-- Name: stock_sector_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX stock_sector_id ON public.stock USING btree (sector_id);


--
-- Name: etf etf_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.etf
    ADD CONSTRAINT etf_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.category(id);


--
-- Name: etf etf_exchange_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.etf
    ADD CONSTRAINT etf_exchange_id_fkey FOREIGN KEY (exchange_id) REFERENCES public.exchange(id);


--
-- Name: etf etf_issuer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.etf
    ADD CONSTRAINT etf_issuer_id_fkey FOREIGN KEY (issuer_id) REFERENCES public.etfissuer(id);


--
-- Name: etf etf_market_index_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.etf
    ADD CONSTRAINT etf_market_index_id_fkey FOREIGN KEY (market_index_id) REFERENCES public.marketindex(id);


--
-- Name: stock stock_exchange_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stock
    ADD CONSTRAINT stock_exchange_id_fkey FOREIGN KEY (exchange_id) REFERENCES public.exchange(id);


--
-- Name: stock stock_industry_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stock
    ADD CONSTRAINT stock_industry_id_fkey FOREIGN KEY (industry_id) REFERENCES public.industry(id);


--
-- Name: stock stock_sector_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stock
    ADD CONSTRAINT stock_sector_id_fkey FOREIGN KEY (sector_id) REFERENCES public.sector(id);


--
-- PostgreSQL database dump complete
--

