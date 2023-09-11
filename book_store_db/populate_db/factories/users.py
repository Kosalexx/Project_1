from __future__ import annotations
from random import randrange
from data_access.dto import UserDTO, ProfileDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (NameProvider,
                                    EmailProvider,
                                    PasswordProvider,
                                    PhoneProvider,
                                    RandomValueFromListProvider)


class UserFactory:
    def __init__(
            self,
            name_provider: NameProvider,
            email_provider: EmailProvider,
            password: PasswordProvider,
            age: RandomValueFromListProvider,
            phone: PhoneProvider
    ):
        self._name_provider = name_provider
        self._email_provider = email_provider
        self._password = password
        self._age = age
        self._phone = phone

    def generate(self) -> UserDTO:
        first_name, last_name = self._name_provider().split()
        username = (first_name[0:randrange(1, (len(first_name)-1))] +
                    last_name[0:randrange(1, (len(first_name)-1))]).lower()
        username += str(randrange(0, 9999))
        profile = ProfileDTO(
            username=username,
            password=self._password(),
            age=self._age(),
            phone=self._phone()
        )
        return UserDTO(
            first_name=first_name,
            last_name=last_name,
            email=self._email_provider(),
            profile=profile
        )
