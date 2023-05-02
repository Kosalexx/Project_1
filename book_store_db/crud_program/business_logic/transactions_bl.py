from __future__ import annotations
from data_access.dao import TransactionsDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.interfaces import DBGatewayProtocol


class TransactionsLogic:
    def __init__(
            self,
            db_gateway: DBGatewayProtocol
    ) -> None:
        self._db_gateway = db_gateway
        self._dao = TransactionsDAO(db_gateway=self._db_gateway)

    def list_of_all_data(self) -> list[dict]:
        data_list = self._dao.get_all_data()
        result_list: list[dict] = []
        for row in data_list:
            data_dict: dict[str, int | str | float] = dict()
            data_dict['ID'] = row.tr_id
            data_dict['User name'] = row.user_name
            data_dict['Bankcard number'] = row.bankcard
            data_dict['Total price'] = row.total_sum
            data_dict['Transaction date'] = row.transaction_date
            data_dict['Address'] = row.address
            result_list.append(data_dict)
        return result_list
