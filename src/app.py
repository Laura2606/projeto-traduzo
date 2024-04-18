from flask import Flask, render_template
from src.models.language_model import LanguageModel

from controllers.admin_controller import admin_controller

from os import environ
from waitress import serve


app = Flask(__name__)
app.template_folder = "views/templates"
app.static_folder = "views/static"

app.register_blueprint(admin_controller, url_prefix="/admin")


@app.route('/', methods=['GET'])
def home():
    languages = LanguageModel.list_dicts()
    return render_template(
        'index.html',
        languages=languages,
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?"
                          )


def start_server(host="0.0.0.0", port=8000):
    if environ.get("FLASK_ENV") != "production":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
