from db_provider import provide_path_to_sqlite_db
from data_access import SqliteGateway
from data_access.dao import (
    CountryDAO,
    CityDAO,
    StreetDAO,
    UserDAO,
    RolesDAO,
    UserRolesDAO,
    PermissionsDAO,
    RolesPermissionsDAO,
    FormatDAO,
    BooksDAO,
    AuthorsDAO,
    GenresDAO,
    BooksAuthorsDAO,
    BooksGenresDAO,
    StatusesDAO,
    BasketsDAO,
    BasketBooksDAO,
    BankcardsDAO,
    AddressesDAO,
    TransactionsDAO
    )
from fake_lib.providers import (
    CountryProvider,
    RandomValueFromListProvider,
    RandomTupleValueFromListProvider,
    CityProvider,
    StreetProvider,
    NameProvider,
    EmailProvider,
    PhoneProvider,
    PasswordProvider,
    RolesProvider,
    PermissionsProvider,
    FormatsProvider,
    BookNameProvider,
    PriceProvider,
    DescriptionProvider,
    LifeDateProvider,
    GenresProvider,
    StatusesProvider,
    BankCardProvider
    )
from factories import (
    CountryFactory,
    CityFactory,
    StreetFactory,
    UserFactory,
    RolesFactory,
    UsersRolesFactory,
    PermissionsFactory,
    RolesPermissionsFactory,
    BooksFactory,
    FormatFactory,
    AuthorFactory,
    GenresFactory,
    BooksAuthorsFactory,
    BooksGenresFactory,
    StatusesFactory,
    BasketsFactory,
    BasketBooksFactory,
    BankcardsFactory,
    AddressesFactory,
    TransactionsFactory
    )
from populate_table_command import PopulateTable


def populate_db(
        db_name: str,
        num: int
        ) -> None:
    """Populates database with random data."""
    db_path = provide_path_to_sqlite_db(db_name)
    db_gateway = SqliteGateway(db_name=db_path)

    country_dao = CountryDAO(db_gateway=db_gateway)
    country_factory = CountryFactory(country_provider=CountryProvider())
    PopulateTable(
        records_number=num,
        dao=country_dao,
        fake_factory=country_factory
    ).execute()

    countries_list = country_dao.get_ids_list()
    city_dao = CityDAO(db_gateway=db_gateway)
    city_factory = CityFactory(
        random_value_provider=RandomValueFromListProvider(countries_list),
        country_dao=country_dao,
        city_provider=CityProvider(),
    )
    PopulateTable(
        records_number=num,
        dao=city_dao,
        fake_factory=city_factory
    ).execute()
    street_dao = StreetDAO(db_gateway=db_gateway)
    cities_list = city_dao.get_ids_list()
    street_factory = StreetFactory(
        street_provider=StreetProvider(),
        random_value_provider=RandomValueFromListProvider(cities_list)
    )
    PopulateTable(
        records_number=num,
        dao=street_dao,
        fake_factory=street_factory
    ).execute()
    user_dao = UserDAO(db_gateway=db_gateway)
    user_factory = UserFactory(
        name_provider=NameProvider(),
        email_provider=EmailProvider(),
        password=PasswordProvider(),
        age=RandomValueFromListProvider(range(14, 100)),
        phone=PhoneProvider()
    )
    PopulateTable(
        records_number=num,
        dao=user_dao,
        fake_factory=user_factory
    ).execute()
    roles_dao = RolesDAO(db_gateway=db_gateway)
    role_factory = RolesFactory(role_provider=RolesProvider())
    PopulateTable(
        records_number=num,
        dao=roles_dao,
        fake_factory=role_factory
    ).execute()
    users_list = user_dao.get_ids_list()
    roles_list = roles_dao.get_ids_list()
    users_roles_dao = UserRolesDAO(db_gateway=db_gateway)
    users_roles_factory = UsersRolesFactory(
        user_id_provider=RandomValueFromListProvider(values=users_list),
        role_id_provider=RandomValueFromListProvider(values=roles_list)
    )
    PopulateTable(
        records_number=num,
        dao=users_roles_dao,
        fake_factory=users_roles_factory
    ).execute()
    permissions_dao = PermissionsDAO(db_gateway=db_gateway)
    permissions_factory = PermissionsFactory(
        permissions_provider=PermissionsProvider())
    PopulateTable(
        records_number=num,
        dao=permissions_dao,
        fake_factory=permissions_factory
    ).execute()
    roles_permissions_dao = RolesPermissionsDAO(db_gateway=db_gateway)
    roles_list = roles_dao.get_ids_list()
    permissions_list = permissions_dao.get_ids_list()
    roles_permissions_factory = RolesPermissionsFactory(
        role_id_provider=RandomValueFromListProvider(values=roles_list),
        permission_id_provider=RandomValueFromListProvider(
            values=permissions_list)
        )
    PopulateTable(
        records_number=num,
        dao=roles_permissions_dao,
        fake_factory=roles_permissions_factory
    ).execute()
    formats_dao = FormatDAO(db_gateway=db_gateway)
    formats_factory = FormatFactory(format_provider=FormatsProvider())
    PopulateTable(
        records_number=num,
        dao=formats_dao,
        fake_factory=formats_factory
    ).execute()
    books_dao = BooksDAO(db_gateway=db_gateway)
    formats_list = formats_dao.get_ids_list()
    books_factory = BooksFactory(
        name_provider=BookNameProvider(),
        description_provider=DescriptionProvider(),
        pages_provider=RandomValueFromListProvider(range(30, 1000)),
        format_id_provider=RandomValueFromListProvider(formats_list),
        age_limit_provider=RandomValueFromListProvider(range(0, 21)),
        amount_provider=RandomValueFromListProvider(range(1, 30)),
        price_provider=PriceProvider()
    )
    PopulateTable(
        records_number=num,
        dao=books_dao,
        fake_factory=books_factory
    ).execute()
    authors_dao = AuthorsDAO(db_gateway=db_gateway)
    authors_factory = AuthorFactory(
        name_provider=NameProvider(),
        life_date_provider=LifeDateProvider(),
        info_provider=DescriptionProvider()
    )
    PopulateTable(
        records_number=num,
        dao=authors_dao,
        fake_factory=authors_factory
    ).execute()
    genres_dao = GenresDAO(db_gateway=db_gateway)
    genres_factory = GenresFactory(
        name_provider=GenresProvider(),
        description_provider=DescriptionProvider()
    )
    PopulateTable(
        records_number=num,
        dao=genres_dao,
        fake_factory=genres_factory
    ).execute()
    books_list = books_dao.get_ids_list()
    authors_list = authors_dao.get_ids_list()
    books_authors_dao = BooksAuthorsDAO(db_gateway=db_gateway)
    books_authors_factory = BooksAuthorsFactory(
        book_id_provider=RandomValueFromListProvider(books_list),
        author_id_provider=RandomValueFromListProvider(authors_list)
    )
    PopulateTable(
        records_number=num,
        dao=books_authors_dao,
        fake_factory=books_authors_factory
    ).execute()
    genres_list = genres_dao.get_ids_list()
    books_genres_dao = BooksGenresDAO(db_gateway=db_gateway)
    books_genres_factory = BooksGenresFactory(
        book_id_provider=RandomValueFromListProvider(books_list),
        genre_id_provider=RandomValueFromListProvider(genres_list)
    )
    PopulateTable(
        records_number=num,
        dao=books_genres_dao,
        fake_factory=books_genres_factory
    ).execute()
    statuses_dao = StatusesDAO(db_gateway=db_gateway)
    statuses_factory = StatusesFactory(
        statuses_provider=StatusesProvider()
    )
    PopulateTable(
        records_number=num,
        dao=statuses_dao,
        fake_factory=statuses_factory
    ).execute()
    users_list = user_dao.get_ids_list()
    statuses_list = statuses_dao.get_ids_list()
    baskets_dao = BasketsDAO(db_gateway=db_gateway)
    baskets_factory = BasketsFactory(
        user_id_provider=RandomValueFromListProvider(users_list),
        status_id_provider=RandomValueFromListProvider(statuses_list)
    )
    PopulateTable(
        records_number=num,
        dao=baskets_dao,
        fake_factory=baskets_factory
    ).execute()
    baskets_list = baskets_dao.get_ids_list()
    books_list = books_dao.get_ids_list()
    basket_books_dao = BasketBooksDAO(db_gateway=db_gateway)
    basket_books_factory = BasketBooksFactory(
        basket_id_provider=RandomValueFromListProvider(baskets_list),
        book_id_provider=RandomValueFromListProvider(books_list),
        buy_quantity_provider=RandomValueFromListProvider(range(1, 50))
    )
    PopulateTable(
        records_number=num,
        dao=basket_books_dao,
        fake_factory=basket_books_factory
    ).execute()
    bankcards_dao = BankcardsDAO(db_gateway=db_gateway)
    bankcards_factory = BankcardsFactory(
        bankcard_provider=BankCardProvider(),
        user_id_provider=RandomValueFromListProvider(users_list)
    )
    PopulateTable(
        records_number=num,
        dao=bankcards_dao,
        fake_factory=bankcards_factory
    ).execute()
    streets_list = street_dao.get_ids_list()
    addresses_dao = AddressesDAO(db_gateway=db_gateway)
    addresses_factory = AddressesFactory(
        street_id_provider=RandomValueFromListProvider(streets_list),
        home_number_provider=RandomValueFromListProvider(range(1, 150)),
        postcode_provider=RandomValueFromListProvider(range(111111, 999999)),
        user_id_provider=RandomValueFromListProvider(users_list)
    )
    PopulateTable(
        records_number=num,
        dao=addresses_dao,
        fake_factory=addresses_factory
    ).execute()
    paid_baskets_list = baskets_dao.get_paid_baskets_dao()
    if paid_baskets_list != []:
        bankcards_list = bankcards_dao.get_ids_list()
        addresses_list = addresses_dao.get_ids_list()
        transactions_dao = TransactionsDAO(db_gateway=db_gateway)
        transactions_factory = TransactionsFactory(
            paid_basket_provider=RandomTupleValueFromListProvider(
                paid_baskets_list),
            bankcards_id_provider=RandomValueFromListProvider(bankcards_list),
            address_id_provider=RandomValueFromListProvider(addresses_list)
        )
        PopulateTable(
            records_number=num,
            dao=transactions_dao,
            fake_factory=transactions_factory
        ).execute()
