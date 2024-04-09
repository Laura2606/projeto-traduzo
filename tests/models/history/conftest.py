import pytest

try:
    from src.database.db import db
    from src.models.history_model import HistoryModel
except ImportError as error:
    pytestmark = pytest.mark.skip(reason=error.msg)


@pytest.fixture(autouse=True)
def prepare_base():
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
