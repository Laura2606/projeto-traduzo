

from pymongo import MongoClient


def test_database_connection():
    try:
        from src.database.db import db
    except ImportError as error:
        assert False, error

    assert db.name == "test_db_traduzo"
    assert isinstance(db.client, MongoClient)
