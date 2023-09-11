PRAGMA foreign_keys = ON;
CREATE TABLE profiles (
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT NOT NULL,
    age INTEGER NOT NULL,
    phone NUMERIC
);
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    profile_id INTEGER,
    email TEXT,
    creation_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (profile_id) REFERENCES profiles(profile_id) ON DELETE CASCADE
);
CREATE TABLE roles (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    creation_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users_roles (
    user_id INTEGER,
    role_id INTEGER,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
);
CREATE TABLE permissions (
    permission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    creation_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE roles_permissions (
    role_id INTEGER,
    permission_id INTEGER,
    PRIMARY KEY (role_id, permission_id),
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE,
    FOREIGN KEY (permission_id) REFERENCES permissions(permission_id) ON DELETE CASCADE
);
CREATE table formats (
    format_id INTEGER PRIMARY KEY AUTOINCREMENT,
    format_name TEXT UNIQUE
);
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    pages INTEGER NOT NULL,
    format_id INTEGER,
    age_limit INTEGER,
    amount INTEGER,
    price REAL NOT NULL,
    creation_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (format_id) REFERENCES formats(format_id) ON DELETE CASCADE
);
CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date NUMERIC NOT NULL,
    death_date NUMERIC,
    info TEXT,
    creation_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE genres (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    creation_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE books_authors (
    book_id INTEGER,
    author_id INTEGER,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);
CREATE TABLE books_genres (
    book_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (book_id, genre_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);
CREATE TABLE statuses (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status_name TEXT UNIQUE
);
CREATE TABLE baskets (
    basket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    status_id INTEGER,
    creation_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN key (status_id) REFERENCES statuses(status_id) ON DELETE CASCADE
);
CREATE TABLE basket_books (
    basket_id INTEGER,
    book_id INTEGER,
    buy_quantity INTEGER,
    PRIMARY KEY (basket_id, book_id),
    FOREIGN KEY (basket_id) REFERENCES baskets(basket_id) ON DELETE CASCADE,
    FOREIGN key (book_id) REFERENCES books(book_id) ON DELETE CASCADE
);
CREATE TABLE bankcards (
    bankcard_id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_number NUMERIC NOT NULL,
    holder_first_name TEXT NOT NULL,
    holder_last_name TEXT NOT NULL,
    cvc INTEGER NOT NULL,
    expiration_date NUMERIC NOT NULL,
    user_id INTEGER,
    creation_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT UNIQUE
);
CREATE TABLE cities (
    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT NOT NULL,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE
);
CREATE TABLE streets (
    street_id INTEGER PRIMARY KEY AUTOINCREMENT,
    street_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE
);
CREATE TABLE addresses (
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    street_id INTEGER,
    home_number INTEGER NOT NULL,
    postcode NUMERIC NOT NULL,
    user_id INTEGER,
    creation_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (street_id) REFERENCES streets(street_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    basket_id INTEGER UNIQUE,
    bankcard_id INTEGER,
    total_price REAL NOT NULL,
    address_id INTEGER,
    creation_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_datetime NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (basket_id) REFERENCES baskets(basket_id) ON DELETE CASCADE,
    FOREIGN KEY (bankcard_id) REFERENCES bankcards(bankcard_id) ON DELETE CASCADE,
    FOREIGN KEY (address_id) REFERENCES addresses(address_id) ON DELETE CASCADE
);
