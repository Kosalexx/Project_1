class Contact:
    def __init__(self, email, phone, first_name, last_name) -> None:
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        email_split = value.split('@')
        if len(email_split) != 2:
            raise ValueError('Email must contain one "@" symbol.')
        poss_end = ['gmail.com', 'yandex.ru', 'ya.ru', 'yahoo.com', 'mail.ru']
        if email_split[1] not in poss_end:
            raise ValueError('Unsupported email provider.')
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if len(value) != 13:
            raise ValueError('Phone length must be 13.')
        if value[0] != '+':
            raise ValueError('Phone must start from "+".')
        if value[1:4] not in ['374', '375']:
            if value[1:3] != '48':
                raise ValueError('Unsupportable phone provider.')
        self._phone = value

    def _validate_name(self, value):
        if not value[0].isupper():
            raise ValueError("First name and Last name must start from "
                             "capital letter.")
        if len(value) not in range(5, 15):
            raise ValueError("Length of First name and Last name must be in "
                             "range (5, 15).")
        return value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._validate_name(value)
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._validate_name(value)
        self._last_name = value
