CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE cities (
    city_id SERIAL PRIMARY KEY,
    city_name VARCHAR(30) NOT NULL,
    country_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE
);
CREATE TABLE addresses (
    address_id SERIAL PRIMARY KEY,
    city_id INT NOT NULL,
    street_name VARCHAR(30) NOT NULL,
    home_number SMALLINT NOT NULL,
    office_number SMALLINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE
);
CREATE TABLE work_statuses (
    work_status_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE work_formats (
    format_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE competencies (
    competence_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE employment_formats (
    employment_format_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE languages (
    language_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE language_level (
    level_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE salary_ranges (
    salary_id SERIAL PRIMARY KEY,
    range_start MONEY,
    range_end MONEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users_profiles (
    profile_id SERIAL PRIMARY KEY,
    login VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    phone VARCHAR(30) NOT NULL,
    age SMALLINT NOT NULL,
    city_id INT NOT NULL,
    experience_description TEXT DEFAULT NULL,
    linkedin_link TEXT DEFAULT NULL,
    github_link TEXT DEFAULT NULL,
    work_experience INT DEFAULT NULL,
    competence_id INT NOT NULL,
    expected_salary_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE,
    FOREIGN KEY (competence_id) REFERENCES competencies(competence_id) ON DELETE CASCADE,
    FOREIGN KEY (expected_salary_id) REFERENCES salary_ranges(salary_id) ON DELETE CASCADE
);
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    profile_id INT NOT NULL,
    photo TEXT,
    summary TEXT,
    work_status_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (profile_id) REFERENCES users_profiles(profile_id) ON DELETE CASCADE,
    FOREIGN KEY (work_status_id) REFERENCES work_statuses(work_status_id) ON DELETE CASCADE
);
CREATE TABLE users_work_formats (
    user_id INTEGER NOT NULL,
    format_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, format_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (format_id) REFERENCES work_formats(format_id) ON DELETE CASCADE
);
CREATE TABLE users_languages (
    user_id INTEGER NOT NULL,
    language_id INTEGER NOT NULL,
    level_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, language_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES languages(language_id) ON DELETE CASCADE,
    FOREIGN KEY (level_id) REFERENCES language_level(level_id) ON DELETE CASCADE
);
CREATE TABLE users_employment_formats (
    user_id INTEGER NOT NULL,
    employment_format_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, employment_format_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (employment_format_id) REFERENCES employment_formats(employment_format_id) ON DELETE CASCADE
);
CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users_tags (
    user_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, tag_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
);
CREATE TABLE business_areas (
    business_area_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE staff (
    staff_number_id SERIAL PRIMARY KEY,
    range_start INT,
    range_end INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE companies_profiles (
    profile_id SERIAL PRIMARY KEY,
    staff_number_id INTEGER NOT NULL,
    founding_year INT DEFAULT NULL,
    description TEXT DEFAULT NULL,
    phone VARCHAR(30) NOT NULL,
    website_link TEXT NOT NULL,
    linkedin_link TEXT DEFAULT NULL,
    github_link TEXT DEFAULT NULL,
    twitter_link TEXT DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (staff_number_id) REFERENCES staff(staff_number_id) ON DELETE CASCADE
);
CREATE TABLE companies (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    profile_id INTEGER NOT NULL,
    logo TEXT,
    email TEXT NOT NULL,
    address_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (profile_id) REFERENCES companies_profiles(profile_id) ON DELETE CASCADE
);
CREATE TABLE companies_business_areas (
    company_id INTEGER NOT NULL,
    business_area_id INTEGER NOT NULL,
    PRIMARY KEY (company_id, business_area_id),
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    FOREIGN KEY (business_area_id) REFERENCES business_areas(business_area_id) ON DELETE CASCADE
);
CREATE TABLE vacancies (
    vacancy_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT DEFAULT NULL,
    competence_level_id INT NOT NULL,
    salary_fork_id INT NOT NULL,
    company_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (competence_level_id) REFERENCES competencies(competence_id) ON DELETE CASCADE,
    FOREIGN KEY (salary_fork_id) REFERENCES salary_ranges(salary_id) ON DELETE CASCADE,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);
CREATE TABLE vacancies_work_formats (
    vacancy_id INTEGER NOT NULL,
    format_id INTEGER NOT NULL,
    PRIMARY KEY (vacancy_id, format_id),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(vacancy_id) ON DELETE CASCADE,
    FOREIGN KEY (format_id) REFERENCES work_formats(format_id) ON DELETE CASCADE
);
CREATE TABLE vacancies_employment_formats (
    vacancy_id INTEGER NOT NULL,
    employment_format_id INTEGER NOT NULL,
    PRIMARY KEY (vacancy_id, employment_format_id),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(vacancy_id) ON DELETE CASCADE,
    FOREIGN KEY (employment_format_id) REFERENCES employment_formats(employment_format_id) ON DELETE CASCADE
);
CREATE TABLE vacancies_tags (
    vacancy_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (vacancy_id, tag_id),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(vacancy_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
);
CREATE TABLE vacancies_cities (
    vacancy_id INTEGER NOT NULL,
    city_id INTEGER NOT NULL,
    PRIMARY KEY (vacancy_id, city_id),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(vacancy_id) ON DELETE CASCADE,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE
);
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    company_id INT NOT NULL,
    email TEXT NOT NULL,
    phone VARCHAR(30),
    login VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    city_id INT NOT NULL,
    photo TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE
);
CREATE TABLE positions (
    position_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE employee_positions (
    employee_id INTEGER NOT NULL,
    position_id INTEGER NOT NULL,
    PRIMARY KEY (employee_id, position_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (position_id) REFERENCES positions(position_id) ON DELETE CASCADE
);
CREATE TABLE response_statuses (
    status_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE response (
    response_id SERIAL PRIMARY KEY,
    user_id INT,
    vacancy_id INT,
    cover_note VARCHAR(500),
    summary TEXT,
    user_phone VARCHAR(30) NOT NULL,
    status_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(vacancy_id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES response_statuses(status_id) ON DELETE CASCADE
);