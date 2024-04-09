import pytest
from pymongo.database import Database


@pytest.fixture(autouse=True)
def set_test_environment():
    try:
        from src.database.db import db
    except ImportError as error:
        pytest.skip(reason=str(error))

    assert isinstance(db, Database), "db is not a instance of Database"

    db.get_collection("languages").drop()
    db.get_collection("history").drop()
    db.get_collection("users").drop()
    yield
