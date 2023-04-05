from fake_factory import FakeFactory
import providers


def test() -> None:
    """Tests 'fake_lib' library"""
    fake_bank = FakeFactory(providers.BankCardProvider(), 3)
    fake_email = FakeFactory(providers.EmailProvider(), 3)
    fake_phone = FakeFactory(providers.PhoneProvider(), 3)
    fake_name = FakeFactory(providers.NameProvider(), 3)

    email = fake_email.generate()
    print('EmailProvider test:')
    print(email)
    print("Email Iterator calls:")
    for emails in fake_email:
        print(emails)

    banc_card = fake_bank.generate()
    print('BankCardProvider test:')
    print(banc_card)
    print("BancCard Iterator calls: ")
    for card in fake_bank:
        print(card)

    phone = fake_phone.generate()
    print('PhoneProvider test:')
    print(phone)
    print('Phone Iterator calls:')
    for phones in fake_phone:
        print(phones)

    name = fake_name.generate()
    print('Name provider test:')
    print(name)
    print('Name Iterator calls:')
    for names in fake_name:
        print(names)


if __name__ == '__main__':
    test()
