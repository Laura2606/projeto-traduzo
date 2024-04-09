from deep_translator import GoogleTranslator

translated = GoogleTranslator(source="auto", target="pt").translate(
    "Hi, would you like some ice cream?"
)
print(translated)
