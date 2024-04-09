import pytest

try:
    from src.database.db import db
except ImportError as error:
    pytestmark = pytest.mark.skip(reason=str(error))

import pytest


@pytest.fixture(autouse=True)
def prepare_base(app_test):
    db.get_collection("history").drop()
    app_test.post(
        "/",
        data={
            "text-to-translate": "Hello, I like videogame",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )

    app_test.post(
        "/",
        data={
            "text-to-translate": "Do you love music?",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )


def test_request_history(app_test):
    response = app_test.get("/history/")
    assert "Hello, I like videogame" in response.get_data(as_text=True)
    assert "Do you love music?" in response.get_data(as_text=True)
