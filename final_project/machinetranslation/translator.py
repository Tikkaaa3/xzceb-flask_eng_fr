"""TranslatoR
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_txt):# english to french translate
    french_text = MyMemoryTranslator(source="en-CA", target="fr-FR").translate(text=english_txt)
    return french_text.split(",")[0]

def french_to_english(french_txt):# french to english translate
    english_txt = MyMemoryTranslator(source="fr-FR", target="en-CA").translate(text=french_txt)
    return english_txt.split(",")[0]
