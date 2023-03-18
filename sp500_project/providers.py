from data_access import CSVData, JSONData


def provide_db(db_file, db_type):
    if db_type == "csv":
        return CSVData(db_file)
    elif db_type == "json":
        return JSONData(db_file)
    else:
        raise ValueError("Unsupported DB type.")
