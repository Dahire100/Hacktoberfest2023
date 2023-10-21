from googletrans import Translator

def translate_to_marathi(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='mr')
    return translated.text

if __name__ == "__main__":
    english_text = "Hello, how are you?"
    marathi_translation = translate_to_marathi(english_text)
    print("English: ", english_text)
    print("Marathi: ", marathi_translation)
