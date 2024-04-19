import json
from src.models.history_model import HistoryModel

# Req. 8


def test_request_history():
    obj = {
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "pt"
    }

    history = HistoryModel.list_as_json()
    history_data = json.loads(history)

    assert history_data[0]["text_to_translate"] == obj["text_to_translate"]
    assert history_data[0]["translate_from"] == obj["translate_from"]
    assert history_data[0]["translate_to"] == obj["translate_to"]

# history = HistoryModel.list_as_json()

    # expected_data = prepare_base()

    # history_data = json.loads(history)

    # assert history_data == expected_data

    # assert json.loads(history)[1]["translate_from"] == "en"
    # assert json.loads(history)[1]["translate_to"] == "pt"
    # assert (
    #     json.loads(history){
    #         "text_to_translate": "Hello, I like videogame",
    #         "translate_from": "en",
    #         "translate_to": "pt",
    #     }
    #     )
