from flask import Flask, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

from controllers.admin_controller import admin_controller

from os import environ
from waitress import serve


app = Flask(__name__)
app.template_folder = "views/templates"
app.static_folder = "views/static"

app.register_blueprint(admin_controller, url_prefix="/admin")


@app.route('/', methods=['GET', 'POST'])
def home():
    languages = LanguageModel.list_dicts()

    if request.method == 'POST':
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        translated = GoogleTranslator(
            source=translate_from,
            target=translate_to
        ).translate(
            text_to_translate
        )
    else:
        text_to_translate = "O que deseja traduzir?"
        translate_from = "pt"
        translate_to = "en"
        translated = "What do you want to translate?"

    return render_template(
      'index.html',
      languages=languages,
      text_to_translate=text_to_translate,
      translate_from=translate_from,
      translate_to=translate_to,
      translated=translated
    )


@app.route('/reverse', methods=['POST'])
def reverse_translation():
    text_to_translate = request.form.get('text-to-translate')
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    reversed_translation = GoogleTranslator(
        source=translate_from,
        target=translate_to
    ).translate(
        text_to_translate
    )

    languages = LanguageModel.list_dicts()

    return render_template(
        'index.html',
        languages=languages,
        text_to_translate=reversed_translation,
        translated=text_to_translate,
        translate_from=translate_to,
        translate_to=translate_from



    )
#     return render_template(
#         'index.html',
#         languages=languages,
#         text_to_translate="O que deseja traduzir?",
#         translate_from="pt",
#         translate_to="en",
#         translated="What do you want to translate?"
#                           )


# @app.route('/', methods=['POST'])
# def translate_text():
#     languages = LanguageModel.list_dicts()
#     text_to_translate = request.form["text-to-translate"]
#     translate_from = request.form["translate-from"]
#     translate_to = request.form["translate-to"]
#     translated = GoogleTranslator(
#         source=translate_from,
#         target=translate_to
#     ).translate(
#         text_to_translate
#     )

#     return render_template("index.html",
#                            languages=languages,
#                            text_to_translate=text_to_translate,
#                            translate_from=translate_from,
#                            translate_to=translate_to,
#                            translated=translated)


def start_server(host="0.0.0.0", port=8000):
    if environ.get("FLASK_ENV") != "production":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
