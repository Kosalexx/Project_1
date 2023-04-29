from __future__ import annotations
from .dto import CompaniesDTO
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from .interfaces import ReadDataProtocol


class CompaniesFactory:
    def __init__(
            self,
            data_provider: ReadDataProtocol
    ):
        self._data_provider = data_provider

    def _check_none_or_float(self, value: Optional[str]) -> float | str:
        if value is None:
            return 'NULL'
        elif value == '':
            return ''
        else:
            return float(value)

    def _check_none_or_str(self, value: Optional[str]) -> str:
        if value is None:
            result: str = 'NULL'
        else:
            result = str(value)
        return result

    def generate(self) -> list[CompaniesDTO]:
        """Generates CompanyDTO with data from the data file."""
        data = self._data_provider.read_all_data()
        result_list = []
        for row in data:
            symbol = self._check_none_or_str(row.get('Symbol'))
            name = self._check_none_or_str(row.get('Name'))
            sector = self._check_none_or_str(row.get('Sector'))
            price = self._check_none_or_float(row.get('Price'))
            price_earnings = self._check_none_or_float(row.get(
                'Price/Earnings'))
            divided_yield = self._check_none_or_float(
                row.get('Dividend Yield'))
            earnings_share = self._check_none_or_float(
                row.get('Earnings/Share'))
            fifty_two_weak_low = self._check_none_or_float(
                row.get('52 Week Low'))
            fifty_two_weak_high = self._check_none_or_float(
                row.get('52 Week High'))
            market_cap = self._check_none_or_float(
                row.get('Market Cap'))
            ebitda = self._check_none_or_float(
                row.get('EBITDA'))
            price_sales = self._check_none_or_float(
                row.get('Price/Sales'))
            price_book = self._check_none_or_float(
                row.get('Price/Book'))
            sec_filings = self._check_none_or_str(row.get('SEC Filings'))
            dto = CompaniesDTO(
                symbol=symbol,
                name=name,
                sector=sector,
                price=price,
                price_earnings=price_earnings,
                divided_yield=divided_yield,
                earnings_share=earnings_share,
                fifty_two_weak_low=fifty_two_weak_low,
                fifty_two_weak_high=fifty_two_weak_high,
                market_cap=market_cap,
                ebitda=ebitda,
                price_sales=price_sales,
                price_book=price_book,
                sec_filings=sec_filings
            )
            result_list.append(dto)
        return result_list
