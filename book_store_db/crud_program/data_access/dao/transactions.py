from __future__ import annotations
from .base import BaseDAO
from data_access.factories import TransactionsFactory
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.dto import TransactionsDTO


class TransactionsDAO(BaseDAO):
    def get_all_data(self) -> list[TransactionsDTO]:
        data = self._db_gateway.cursor.execute(
            'SELECT users.first_name, users.last_name, bankcards.card_number, '
            'transactions.total_price, transactions.creation_datetime, '
            'countries.country_name, cities.city_name, streets.street_name, '
            'addresses.home_number, addresses.postcode, '
            'transactions.transaction_id FROM transactions '
            'JOIN baskets ON transactions.basket_id = baskets.basket_id '
            'JOIN users ON baskets.user_id = users.user_id '
            'JOIN bankcards ON transactions.bankcard_id = '
            'bankcards.bankcard_id '
            'JOIN addresses ON transactions.address_id = addresses.address_id'
            ' JOIN streets ON addresses.street_id = streets.street_id '
            'JOIN cities ON streets.city_id = cities.city_id '
            'JOIN countries ON cities.country_id = countries.country_id '
            'ORDER BY transactions.transaction_id;'
        )
        result_list: list[tuple] = data.fetchall()
        final_list: list[TransactionsDTO] = []
        for row in result_list:
            list_data = list(row)
            data_dto = TransactionsFactory(list_data=list_data).generate_dto()
            final_list.append(data_dto)
        return final_list
