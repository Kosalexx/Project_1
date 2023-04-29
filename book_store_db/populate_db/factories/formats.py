from __future__ import annotations
from data_access.dto import FormatsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import FormatsProvider


class FormatFactory:
    def __init__(
            self,
            format_provider: FormatsProvider
    ):
        self._format_provider = format_provider

    def generate(self) -> FormatsDTO:
        return FormatsDTO(
            format_name=self._format_provider()
        )
