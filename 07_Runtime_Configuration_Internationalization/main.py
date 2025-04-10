import json

def get_translation(lang_code):
    with open("translations.json", "r") as f:
        all_translations = json.load(f)
        return all_translations.get(lang_code, all_translations["en"])

# Pemakaian
t = get_translation("id")
print(t["greeting"])
print(t["thanks"])