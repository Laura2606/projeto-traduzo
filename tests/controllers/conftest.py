import pytest

try:
    from src.app import app
except ImportError as error:
    pytestmark = pytest.mark.skip(reason=error.msg)

try:
    from src.models.language_model import LanguageModel
except ImportError as error:
    pytestmark = pytest.mark.skip(reason=error.msg)


@pytest.fixture(autouse=True)
def app_test():
    return app.test_client()


@pytest.fixture(autouse=True)
def add_countries():
    list_of_languages = [
        {"name": "Afrikaans", "acronym": "af"},
        {"name": "english", "acronym": "en"},
        {"name": "Portugues", "acronym": "pt"},
    ]

    for language in list_of_languages:
        LanguageModel(language).save()
