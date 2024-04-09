import pytest

from src.models.history_model import HistoryModel

try:
    from src.app import app
    from src.database.db import db
except ImportError as error:
    pytestmark = pytest.mark.skip(reason=error.msg)


@pytest.fixture(autouse=True)
def app_test():
    return app.test_client()


@pytest.fixture(autouse=True)
def prepare_base(app_test):
    db.get_collection("history").drop()
    HistoryModel(
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    HistoryModel(
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()
