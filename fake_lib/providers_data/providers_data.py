import os
import string
from random import randint, choice, shuffle


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
