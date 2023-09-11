import os
import string
import json
from random import randint, choice, shuffle, uniform


class Generator:
    """Generates the necessary random data using database or Random module."""

    def random_digit_not_null(self) -> str:
        """Generates a random digit other than null.

        :rtype: str
        :return: string that contains one random digit from 1 to 9.
        """
        return str(randint(1, 9))

    def random_numbers(self, num: int = randint(1, 5)) -> str:
        """Generates a random string of numbers in range(num).

        :param num: length of the generated string of numbers
                    Default = random.randint(1, 5)
        :type num: int

        :rtype: str
        :return: string that contains a number of 'num' random digits
        """
        result: str = ''.join([str(randint(0, 9)) for _ in range(num)])
        return result

    def random_lowercase_str(self, length: int = randint(5, 10)) -> str:
        """Generates a random string of lowercase letters in range(length).

        :param length: length of the generated string of lowercase letters
                        Default = random.randint(5, 10)
        :type length: int

        :rtype: str
        :return: string that contains a 'length' of lowercase letters
        """
        letters: str = string.ascii_lowercase
        result: str = ''.join(choice(letters) for i in range(length))
        return result

    def random_uppercase_letter(self) -> str:
        """Generates one random uppercase letter.

        :rtype: str
        :return: string that contains one random uppercase letter.
        """
        letters: str = string.ascii_uppercase
        result: str = choice(letters)
        return result

    def shuffle_string(self, text: str) -> str:
        """shuffles the contents of a string in random order.

        :param text: text that needs to be shuffled
        :type text: str

        :rtype: str
        :return: string that contains the shuffling text
        """
        my_list: list = []
        my_list.extend(text)
        shuffle(my_list)
        result: str = ''.join(my_list)
        return result

    def get_path_to_db(self, value: str) -> str:
        """Returns path to database.

        :param value: name of database file
        :type value: str

        :rtype: str
        :return: path to database file
        """
        directory: str = os.path.dirname(__file__)
        path: str = os.path.join(directory, value)
        return path

    def get_first_name(
            self,
            first_digit: str,
            database: str = 'first_names.txt'
            ) -> str:
        """Gets random First Name from database file by the entered letter.

        :param first_digit: first digit of generated name
        :type first_digit: str
        :param database: name of database file
                        Default = 'first_names.txt'
        :type database: str

        :rtype: str
        :return: Random First Name from database by entered letter.
        """
        names: list = []
        data_base: str = self.get_path_to_db(database)
        with open(data_base) as data:
            for name in data:
                if name.startswith(first_digit):
                    new_name: str = name.replace('\n', '')
                    names.append(new_name)
        name = choice(names)
        return name

    def get_last_name(self, first_digit: str) -> str:
        """Gets random Last Name from database file by the entered letter.

        Uses "Generator.get_first_name()" method with default name of database
        file = 'last_names.txt' and the passed parameter 'first_digit'

        :param first_digit: first digit of generated last name
        :type first_digit: str

        :rtype: str
        :return: Random Last Name from database by entered letter.
        """
        result = self.get_first_name(first_digit=first_digit,
                                     database='last_names.txt')
        return result

    def get_country_name(self) -> str:
        """Gets random country_name from database file by the entered letter.

        :rtype: str
        :return: Random country name from database by entered letter.
        """
        countries: list[str] = []
        data_base: str = self.get_path_to_db('cities.json')
        with open(data_base) as file:
            country_data: dict[str, list[str]] = json.load(file)
            for country in country_data.keys():
                country_name: str = country
                countries.append(country_name)
        name: str = choice(countries)
        return name

    def get_city_name(self, country_name: str) -> str:
        """Gets random city_name from database file by the entered country.

        :param country_name: name of the country where the city is located
        :type country_name: str

        :rtype: str
        :return: Random city name from database by entered country_name.
        """
        data_base: str = self.get_path_to_db('cities.json')
        with open(data_base) as file:
            data: dict[str, list[str]] = json.load(file)
            city_list = data.get(country_name)
            if city_list is not None:
                random_city = choice(city_list)
            else:
                random_city = 'Random City'
        return random_city

    def get_street_name(self) -> str:
        """Gets random street_name.

        :rtype: str
        :return: Random street name.
        """
        pattern = choice(['num', 'first_name', 'last_name', 'country_name'])
        if pattern == 'num':
            result = self.random_numbers()
        elif pattern == 'first_name':
            result = self.get_first_name(self.random_uppercase_letter())
        elif pattern == 'last_name':
            result = self.get_last_name(self.random_uppercase_letter())
        elif pattern == 'country_name':
            result = self.get_country_name()
        return result

    def get_description(self) -> str:
        """Generates random description.

        :rtype: str
        :return: random description."""
        data_base: str = self.get_path_to_db('lorem.txt')
        all_sentences = []
        with open(data_base) as data:
            for row in data:
                paragraph_sentences = row.split('.')
                for sent in paragraph_sentences:
                    all_sentences.append(sent)
        result = choice(all_sentences)
        if result == '\n':
            result = self.get_description()
        return result

    def get_book_name(self) -> str:
        """Generates random book_name.

        :rtype: str
        :return: random book name."""
        data = self.get_description()
        book_name = ''
        for _ in range(randint(1, 5)):
            book_name += choice(data.split()).lower()
            book_name += ' '
        book_name = book_name.capitalize().strip()
        return book_name

    def random_float_num(self) -> float:
        """Generates random float value."""
        result = uniform(1, 100)
        return result
