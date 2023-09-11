from random import choice, randint, randrange
from datetime import datetime, date
from .providers_data import Generator
from typing import Optional


class EmailProvider:
    """Provider that generates random emails of supported services.

    Supported email-services are set in 'poss_services'.
    """
    pattern: str = '{email}{poss_service}'
    poss_services: list[str] = [
        "@gmail.com",
        "@yandex.ru",
        "@ya.ru",
        "@mail.ru",
        "@outlook.com",
        "@i.ua",
        "@rambler.ru",
        "@mail.com",
        "@email.com",
        "@usa.com",
        "@myself.com",
        "@groupmail.com",
        "@post.com",
        "@homemail.com",
        "@housemail.com",
        "@writeme.com",
        "@mail-me.com",
        "@workmail.com",
        "@randomsite.com",
        "@blabla.net"
        ]

    def __call__(
            self,
            services: Optional[str] = None,
            length: Optional[int] = None,
            include_digits: bool = True
            ) -> str:
        if services is None:
            services = choice(self.poss_services)
        if length is None:
            length = randint(3, 15)
        if include_digits:
            email = Generator().random_numbers(randint(1, length))
        else:
            email = ''
        email += Generator().random_lowercase_str(length-len(email))
        result = Generator().shuffle_string(email)
        result += services
        return result


class PhoneProvider:
    """Provider that generates random phone with supported country code.

    Supported country codes are set in 'poss_services'.
    """
    pattern: str = '{country_code}{city_code}{phone}'
    poss_services: list[str] = [
        "+375",
        "+374",
        "+7",
        "+994",
        "+1",
        "+380",
        "+44",
        "+48"
    ]

    def __call__(self) -> str:
        country_code = choice(self.poss_services)
        city_code = Generator().random_numbers(6-len(country_code))
        phone = Generator().random_digit_not_null()
        phone += Generator().random_numbers(7-1)
        result = self.pattern.format(country_code=country_code,
                                     city_code=city_code,
                                     phone=phone)
        return result


class NameProvider:
    """Provider that generates random Name in format 'First_name Last_name'.

    For this provider to work in the folder '.providers_data' you must create
    files 'first_names.txt' and 'last_names.txt' with the most popular first
    names and last names. These files will be used as databases for name
    generation.
    """
    first_name: str = ''
    last_name: str = ''

    def __call__(self) -> str:
        first_name_digit1 = Generator().random_uppercase_letter()
        last_name_digit1 = Generator().random_uppercase_letter()
        self.first_name = Generator().get_first_name(first_name_digit1)
        self.last_name = Generator().get_last_name(last_name_digit1)
        result = f'{self.first_name} {self.last_name}'
        return result


class BankCardProvider:
    """ Provider that generates random bankcard information in format:
    '{card_number}, {EXP}, {CVC}, {card_holder}, {system}', where:
        - card_number - number of bankcard (sixteen digits). Generated based on
        the supported services, which are specified in the 'poss_services';
        - EXP - bankcard expiration date;
        - CVC - card verification code;
        - card_holder - name of card holder;
        - system - payment system (Visa, MasterCard, etc.). Generated based on
        the supported services, which are specified in the 'poss_services'.
    """
    pattern: str = '{card_number}, {EXP}, {CVC}, {card_holder}, {system}'
    poss_services: dict[str, str] = {
        "2": "Мir",
        "30": "Diners Club",
        "36": "Diners Club",
        "38": "Diners Club",
        "31": "JCB International",
        "35": "JCB International",
        "34": "American Express",
        "37": "American Express",
        "4": "VISA",
        "50": "Maestro",
        "56": "Maestro",
        "57": "Maestro",
        "58": "Maestro",
        "51": "MasterCard",
        "52": "MasterCard",
        "53": "MasterCard",
        "54": "MasterCard",
        "55": "MasterCard",
        "60": "Discover",
        "62": "China UnionPay",
        "63": "Maestro",
        "67": "Maestro",
        }
    current_year = datetime.now().year
    current_month = datetime.now().month

    def _generate_card_number_and_system(self) -> list[str]:
        """ Generate valid bankcard number."""
        card_number = choice(list(self.poss_services.keys()))
        system = self.poss_services[card_number]
        card_number += Generator().random_numbers(15-len(card_number))
        sum_of_digits = 0
        for ind, number in enumerate(card_number):
            if ind % 2 == 0:
                num = int(number) * 2
                if num > 9:
                    num -= 9
            sum_of_digits += int(number)

        if sum_of_digits % 10 == 0:
            card_number += '0'
        else:
            card_number += str(10 - sum_of_digits % 10)
        return [card_number, system]

    def _generate_exp(self) -> str:
        """Generate valid bankcard expiration code based on today's date."""
        year = self.current_year + randint(0, 10)
        if year == self.current_year and self.current_month != 12:
            month = randint(self.current_month, 12)
        else:
            month = randint(1, 12)
        if month < 10:
            month_str = '0' + str(month)
        else:
            month_str = str(month)
        year_str = str(year)
        exp = f'{month_str}/{year_str}'
        return exp

    def __call__(self) -> str:
        card_number, system = self._generate_card_number_and_system()
        exp = self._generate_exp()
        cvc = Generator().random_numbers(num=3)
        gen_name = NameProvider()
        card_holder = gen_name().upper()
        result = f'{card_number}, {exp}, {cvc}, {card_holder}, {system}'
        return result


class CountryProvider:
    """Provider that generates random city name.

    For this provider to work in the folder '.providers_data' you must create
    files 'cities.json' with the country and city names.
    These files will be used as databases for country name generation.
    """
    def __call__(self) -> str:
        country_name = Generator().get_country_name()
        return country_name


class RandomValueFromListProvider:
    """Provider that generates random value from list.

    :param value: list of values
    :type value: list[int]
    """
    def __init__(self, values: list[int]) -> None:
        self._values = values

    def __call__(self) -> int:
        random_value = choice(self._values)
        if isinstance(random_value, tuple):
            result: int = random_value[0]
        else:
            result = random_value
        return result


class RandomTupleValueFromListProvider:
    """Provider that generates random value from list.

    :param value: list of values
    :type value: list[tuple]
    """
    def __init__(self, values: list[tuple[int, float]]) -> None:
        self._values = values

    def __call__(self) -> tuple[int, float]:
        random_value = choice(self._values)
        return random_value


class CityProvider:
    """Provider that generates random city name.

    For this provider to work in the folder '.providers_data' you must create
    files 'cities.json' with the country and city names.
    These files will be used as databases for country name generation.
    """
    def __call__(self, country_name: str) -> str:
        city_name = Generator().get_city_name(country_name)
        return city_name


class StreetProvider:
    """Provider that generates random street name."""
    street_suffixes = (
        "alley",
        "avenue",
        "branch",
        "bridge",
        "brook",
        "burg",
        "bypass",
        "camp",
        "canyon",
        "cape",
        "center",
        "circle",
        "common",
        "corner",
        "corners",
        "course",
        "court",
        "courts",
        "cove",
        "coves",
        "creek",
        "crescent",
        "crest",
        "crossing",
        "drive",
        "extension",
        "fall",
        "ferry",
        "field",
        "flat",
        "ford",
        "fords",
        "forest",
        "forge",
        "fork",
        "fort",
        "garden",
        "gateway",
        "grove",
        "groves",
        "harbor",
        "hill",
        "hills",
        "hollow",
        "inlet",
        "island",
        "isle",
        "lake",
        "mountain",
        "ramp",
        "ranch",
        "rapid",
        "river",
        "road",
        "route",
        "run",
        "shore",
        "spring",
        "square",
        "station",
        "street",
        "tunnel",
        "underpass",
        "union",
        "valley",
    )

    def __call__(self) -> str:
        street_name = Generator().get_street_name() + ' ' + choice(
            self.street_suffixes)
        return street_name


class PasswordProvider:
    """Provider that generates random password."""
    def __call__(self) -> str:
        password = Generator().random_lowercase_str()
        password += Generator().random_numbers()
        password += Generator().random_uppercase_letter()
        result_password: str = Generator().shuffle_string(password)
        return result_password


class RolesProvider:
    """Provider that returns random role from list of available roles."""
    available_roles = (
        "customer",
        "admin",
        "owner",
        "support specialist",
        "seller"
    )

    def __call__(self) -> str:
        return choice(self.available_roles)


class PermissionsProvider:
    """Provider that returns random permission from list of available values.
    """
    permissions = (
        "read_goods",
        "update_description",
        "add_book",
        "delete_data",
        "update_userinfo",
        "create_order",
        "account_blocking",
        "payment_status_checking",
        "just_reading"
    )

    def __call__(self) -> str:
        return choice(self.permissions)


class FormatsProvider:
    """Provider that returns random format from list of available formats."""
    available_formats = (
        "e-book",
        "softcover",
        "hardcover",
        "glossy pages",
        "trial book"
    )

    def __call__(self) -> str:
        return choice(self.available_formats)


class DescriptionProvider:
    """Provider that generates random description."""
    def __call__(self) -> str:
        result = Generator().get_description()
        if len(result) < 3:
            result += Generator().get_description()
        return result


class BookNameProvider:
    """Provider that generates random book name."""
    def __call__(self) -> str:
        result = Generator().get_book_name()
        return result


class PriceProvider:
    """Provider that generates random price (float value)."""
    def __call__(self) -> float:
        result = Generator().random_float_num()
        rounded_result = round(result, 2)
        return rounded_result


class LifeDateProvider:
    """Provider that generates random birthday_date and death_date."""
    today_day = date.today()

    def __call__(self) -> list[str]:
        birth_date = date(
            randrange(1900, 2023), randrange(1, 12), randrange(1, 30))
        age_of_life = randrange(25, 100)
        death_date = date(
            birth_date.year + age_of_life, randrange(1, 12), randrange(1, 30))
        result_date = [str(birth_date),]
        if death_date > self.today_day:
            result_date.append('NULL')
        else:
            result_date.append(str(death_date))
        return result_date


class GenresProvider:
    """Provider that returns random genre_name from list of available genres.
    """
    available_genres = (
        "Adventure stories",
        "Classics",
        "Crime",
        "Fairy tales, fables, and folk tales",
        "Fantasy",
        "Historical fiction",
        "Horror",
        "Humour and satire",
        "Literary fiction",
        "Mystery",
        "Poetry",
        "Plays",
        "Romance",
        "Science fiction",
        "Short stories",
        "Thrillers",
        "War",
        "Women’s fiction",
        "Young adult",
        "Autobiography and memoir",
        "Biography",
        "Essays",
        "Non-fiction novel",
        "Self-help"
    )

    def __call__(self) -> str:
        result = choice(self.available_genres)
        return result


class StatusesProvider:
    """Provider that returns random status from list of available statuses."""
    available_statuses = (
        "placed",
        "awaits payment",
        "open",
        "in process",
        "paid",
        "canceled"
    )

    def __call__(self) -> str:
        result = choice(self.available_statuses)
        return result
