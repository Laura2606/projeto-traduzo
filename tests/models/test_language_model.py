import pytest

try:
    from src.models.language_model import LanguageModel
except ImportError as error:
    pytestmark = pytest.mark.skip(reason=error.msg)


def test_create_language() -> None:
    language = LanguageModel({"name": "afrikaans", "acronym": "af"})
    saved_language = language.save()

    assert saved_language.id is not None
    assert isinstance(saved_language.id, str)


def test_create_dict_language() -> None:
    language = LanguageModel({"name": "afrikaans", "acronym": "af"})
    saved_language = language.save()
    dict_language = saved_language.to_dict()
    assert dict_language["name"] == "afrikaans"
    assert dict_language["acronym"] == "af"
    assert len(dict_language) == 2


def test_create_list_languages() -> None:
    list_of_languages = [
        {"name": "Afrikaans", "acronym": "af"},
        {"name": "english", "acronym": "en"},
        {"name": "Portugues", "acronym": "pt"},
    ]

    for language in list_of_languages:
        LanguageModel(language).save()

    assert LanguageModel.list_dicts() == list_of_languages
