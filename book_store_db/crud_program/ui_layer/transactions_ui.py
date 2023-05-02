from __future__ import annotations
from typing import TYPE_CHECKING
from business_logic import TransactionsLogic
if TYPE_CHECKING:
    from data_access.interfaces import DBGatewayProtocol


def transactions_ui_menu(db_connector: DBGatewayProtocol) -> None:
    logic = TransactionsLogic(db_gateway=db_connector)
    result = logic.list_of_all_data()
    for row in result:
        print(row)
