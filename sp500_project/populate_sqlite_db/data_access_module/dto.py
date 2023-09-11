from dataclasses import dataclass


@dataclass
class CompaniesDTO:
    symbol: str
    name: str
    sector: str
    price: float | str
    price_earnings: float | str
    divided_yield: float | str
    earnings_share: float | str
    fifty_two_weak_low: float | str
    fifty_two_weak_high: float | str
    market_cap: float | str
    ebitda: float | str
    price_sales: float | str
    price_book: float | str
    sec_filings: str | str
