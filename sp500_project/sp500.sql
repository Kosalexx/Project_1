PRAGMA foreign_keys = ON;
CREATE TABLE sp500 (
    symbol TEXT UNIQUE NOT NULL,
    name TEXT UNIQUE NOT NULL,
    sector TEXT NOT NULL,
    price REAL NOT NULL,
    price_earnings REAL,
    dividend_yield REAL,
    earnings_share REAL,
    fifty_two_week_low REAL,
    fifty_two_week_high REAL,
    market_cap REAL,
    ebitda REAL,
    price_sales REAL,
    price_book REAL,
    sec_filings TEXT
);