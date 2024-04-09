from flask.testing import FlaskClient
from bs4 import BeautifulSoup
import pytest

try:
    from src.models.language_model import LanguageModel
except ImportError as error:
    pytestmark = pytest.mark.skip(reason=error.msg)


def test_request_translate(app_test: FlaskClient):
    response = app_test.get("/")
    assert response.status_code != 404, "A rota '/' não foi encontrada"

    soup = BeautifulSoup(response.text, "html.parser")

    assert (
        soup.find("textarea", {"class": "from-text"}).text
        == "O que deseja traduzir?"
    )
    assert (
        soup.find("textarea", {"class": "to-text"}).text
        == "What do you want to translate?"
    )

    from_languages = [
        language.text.strip()
        for language in soup.find(
            "select", {"name": "translate-from"}
        ).find_all("option")
    ]

    assert all(
        language in from_languages
        for language in ["ENGLISH", "AFRIKAANS", "PORTUGUES"]
    )

    to_languages = [
        language.text.strip()
        for language in soup.find("select", {"name": "translate-to"}).find_all(
            "option"
        )
    ]

    assert all(
        language in to_languages
        for language in ["ENGLISH", "AFRIKAANS", "PORTUGUES"]
    )

    assert (
        len(from_languages) + len(to_languages)
        == len(LanguageModel.find()) * 2
    )

    selected_from = soup.find("select", {"name": "translate-from"}).find(
        "option", {"selected": True}
    )

    assert selected_from, "Uma opção 'translate-from' deve estar selecionada"

    assert (
        selected_from["value"]
        == LanguageModel.find({"acronym": selected_from["value"]})[
            0
        ].to_dict()["acronym"]
    )

    selected_to = soup.find("select", {"name": "translate-to"}).find(
        "option", {"selected": True}
    )

    assert selected_to, "Uma opção 'translate-to' deve estar selecionada"

    assert (
        selected_to["value"]
        == LanguageModel.find({"acronym": selected_to["value"]})[0].to_dict()[
            "acronym"
        ]
    )


def test_post_translate(app_test: FlaskClient):
    response = app_test.post(
        "/",
        data={
            "text-to-translate": "Hello, I like videogame",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )
    assert response.status_code != 404, "A rota '/' não foi encontrada"

    soup = BeautifulSoup(response.text, "html.parser")

    assert (
        soup.find("textarea", {"class": "from-text"}).text
        == "Hello, I like videogame"
    )
    assert (
        soup.find("textarea", {"class": "to-text"}).text
        == "Olá, eu gosto de videogame"
    )

    selected_from = soup.find("select", {"name": "translate-from"}).find(
        "option", {"selected": True}
    )

    assert selected_from, "Uma opção 'translate-from' deve estar selecionada"

    assert selected_from["value"] == "en"

    selected_to = soup.find("select", {"name": "translate-to"}).find(
        "option", {"selected": True}
    )

    assert selected_to, "Uma opção 'translate-to' deve estar selecionada"

    assert selected_to["value"] == "pt"


def test_post_reverse(app_test: FlaskClient):
    response = app_test.post(
        "/reverse",
        data={
            "text-to-translate": "Hello, I like videogame",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )
    assert response.status_code != 404, "A rota '/reverse' não foi encontrada"

    soup = BeautifulSoup(response.text, "html.parser")

    assert (
        soup.find("textarea", {"class": "from-text"}).text
        == "Olá, eu gosto de videogame"
    )
    assert (
        soup.find("textarea", {"class": "to-text"}).text
        == "Hello, I like videogame"
    )

    selected_from = soup.find("select", {"name": "translate-from"}).find(
        "option", {"selected": True}
    )

    assert selected_from, "Uma opção 'translate-from' deve estar selecionada"

    assert selected_from["value"] == "pt"

    selected_to = soup.find("select", {"name": "translate-to"}).find(
        "option", {"selected": True}
    )

    assert selected_to, "Uma opção 'translate-to' deve estar selecionada"

    assert selected_to["value"] == "en"
