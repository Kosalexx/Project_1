import csv


def read_csv_data():
    """Reads data from .csv file."""
    with open('sp500.csv', encoding="utf-8") as read_file:
        for item in csv.DictReader(read_file):
            yield item


def write_to_csv_database(fields: list, data: list, mode: str = "a") -> None:
    """Writes data into csv file. """
    with open('sp500.csv', mode=mode, newline='', encoding="utf-8") as \
            w_file:
        names = fields
        file_writer = csv.DictWriter(w_file, names)
        if mode == 'w':
            file_writer.writeheader()
        file_writer.writerows(data)
