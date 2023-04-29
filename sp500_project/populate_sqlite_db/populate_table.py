from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access_module.interfaces import (CreateRecordProtocol,
                                               FakeFactoryProtocol)


class PopulateTable:
    def __init__(
            self,
            dao: CreateRecordProtocol,
            fake_factory: FakeFactoryProtocol
    ) -> None:
        self._dao = dao
        self._fake_factory = fake_factory

    def execute(self) -> None:
        """Executes a data recording into the database."""
        all_data = self._fake_factory.generate()
        for row in all_data:
            self._dao.create(data=row)
