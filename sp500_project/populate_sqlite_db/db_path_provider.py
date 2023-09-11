from pathlib import Path


def provide_path_to_sqlite_db(db_name: str) -> str:
    """Provides path to database."""
    myself = Path(__file__).resolve()
    res = myself.parents[1] / db_name
    return str(res)
