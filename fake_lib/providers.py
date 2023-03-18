from typing import Any
from random import choice, randint
from datetime import datetime
from providers_data import Generator


class EmailProvider:
    """Provider that generates random emails of supported services.

    Supported email-services are set in 'poss_services'.
    """
    pattern = '{email}{poss_service}'
    poss_services = [
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
            services: str = None,
            length: int = None,
            include_digits: bool = True
            ):
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
    pattern = '{country_code}{city_code}{phone}'
    poss_services = [
        "+375",
        "+374",
        "+7",
        "+994",
        "+1",
        "+380",
        "+44",
        "+48"
    ]

    def __call__(self, *args: Any, **kwds: Any) -> Any:
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
    pattern = '{first_name} {last_name}'

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        first_name_digit1 = Generator().random_uppercase_letter()
        last_name_digit1 = Generator().random_uppercase_letter()
        first_name = Generator().get_first_name(first_name_digit1)
        last_name = Generator().get_last_name(last_name_digit1)
        result = f'{first_name} {last_name}'
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
    pattern = '{card_number}, {EXP}, {CVC}, {card_holder}, {system}'
    poss_services = {
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

    def _generate_card_number_and_system(self):
        """ Generate valid bankcard number."""
        card_number = choice(list(self.poss_services.keys()))
        system = self.poss_services[card_number]
        card_number += Generator().random_numbers(15-len(card_number))
        sum_of_digits = 0
        for ind, number in enumerate(card_number):
            if ind % 2 == 0:
                number = int(number) * 2
                if number > 9:
                    number -= 9
            sum_of_digits += int(number)

        if sum_of_digits % 10 == 0:
            card_number += '0'
        else:
            card_number += str(10 - sum_of_digits % 10)
        return [card_number, system]

    def _generate_exp(self):
        """Generate valid bankcard expiration code based on today's date."""
        year = self.current_year + randint(0, 10)
        if year == self.current_year and self.current_month != 12:
            month = randint(self.current_month, 12)
        else:
            month = randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        year = str(year)
        exp = f'{month}/{year}'
        return exp

    def __call__(self) -> str:
        card_number, system = self._generate_card_number_and_system()
        exp = self._generate_exp()
        cvc = Generator().random_numbers(num=3)
        gen_name = NameProvider()
        card_holder = gen_name().upper()
        result = f'{card_number}, {exp}, {cvc}, {card_holder}, {system}'
        return result
