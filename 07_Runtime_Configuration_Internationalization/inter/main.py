import json

def get_translation(lang_code):
    with open('translations.json', 'r') as file:
        translations = json.load(file)
        return translations.get(lang_code, translations['en'])
    
translate = get_translation('en')
print(translate['greeting'])
print(translate['thanks'])