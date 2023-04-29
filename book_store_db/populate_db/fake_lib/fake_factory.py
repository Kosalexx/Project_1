from .errors import ProviderNameError
from .config import PROVIDERS
from typing import Callable, Self


class FakeFactory:
    """ General Factory class.

    Generates Fake-data depending on the selected provider.
    Supported providers are described in providers.py and config.py.

    :param provider: provider from providers.py
    :type provider: Type[Providers]
    :param num: length of the generated iterated object FakeFactory class
    :type num: int

    Example of how a class FakeFactory works:

    from fake_factory import FakeFactory


    fake_name = FakeFactory(providers.NameProvider(), 3)
    name = fake_name.generate()
    print(name)

    >>> Random Name
    for names in fake_name:
        print(name)

    >>> Firstrandom Name
        Secondrandom Name
        Third RandomName
    """
    def __init__(
            self,
            provider: Callable[[], str],
            num: int) -> None:
        self.provider = provider
        self.num = num

    def _validate_num(self, value: int) -> None:
        """Validates if the num is integer and  greater than zero.

        :param value: value of given to FakeFactory class 'num'
        :type value: int

        :raises ValueError: if number is not integer and number less than zero
        """
        if not isinstance(value, int):
            raise ValueError('Number must be integer.')
        if value <= 0:
            raise ValueError('Number must be greater than 0.')

    def _validate_provider(self, provider_name: object) -> None:
        """Validates if the provider_name is correct and exist in providers.py

        :param provider_name: name of given provider
        :type provider_name: Type[Providers]

        :raises ProviderNameError: if provider_name is not correct and not
                                   exist in providers.py
        """
        if not isinstance(provider_name, object):
            raise ProviderNameError("Incorrect provider name.")
        if provider_name.__class__.__name__ not in PROVIDERS:
            raise ProviderNameError("Incorrect provider name.")

    @property
    def num(self) -> int:
        return self._num

    @num.setter
    def num(self, value: int) -> None:
        self._validate_num(value)
        self._num = value

    @property
    def provider(self) -> Callable[[], str]:
        return self._provider

    @provider.setter
    def provider(self, provider_name: Callable[[], str]) -> None:
        self._validate_provider(provider_name)
        self._provider = provider_name

    def __iter__(self) -> Self:
        self.ind = 0
        return self

    def __next__(self) -> str:
        if self.ind == len(self):
            raise StopIteration
        self.ind += 1
        result = self.generate()
        return result

    def __len__(self) -> int:
        return self.num

    def generate(self) -> str:
        """Generates Fake-data depending on the given provider."""
        result = self.provider()
        return result
