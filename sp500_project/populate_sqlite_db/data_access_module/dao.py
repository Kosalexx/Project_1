from __future__ import annotations
from typing import TYPE_CHECKING
from .dto import CompaniesDTO
if TYPE_CHECKING:
    from .interfaces import DBGatewayProtocol


class CompaniesDAO:
    def __init__(
            self,
            db_gateway: DBGatewayProtocol
    ) -> None:
        self._db_gateway = db_gateway

    def create(self, data: CompaniesDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            'INSERT INTO sp500 (symbol, name, sector, price, '
            'price_earnings, dividend_yield, earnings_share, '
            'fifty_two_week_low, fifty_two_week_high, market_cap, ebitda, '
            'price_sales, price_book, sec_filings) VALUES (?, ?, ?, ?, ?, '
            '?, ?, ?, ?, ?, ?, ?, ?, ?);', (
                data.symbol, data.name, data.sector, data.price,
                data.price_earnings, data.divided_yield, data.earnings_share,
                data.fifty_two_weak_low, data.fifty_two_weak_high,
                data.market_cap, data.ebitda, data.price_sales,
                data.price_book, data.sec_filings)
        )
        self._db_gateway.connection.commit()
