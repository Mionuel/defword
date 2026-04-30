from pathlib import Path

import requests
import sys

dictionaryAPI = "https://freedictionaryapi.com/api/v1/entries"
translationAPI = "https://api.mymemory.translated.net/get"

DATA_DIR = Path.home() / ".local" / "share" / "defword"

HISTORY_PATH = DATA_DIR / "history.jsonl"
CACHE_PATH = DATA_DIR / "requests_cache"

# sanitizes the word by making it lowercase and trimming white spaces
def sanitize_word(word):
    return word.lower().strip()

# formats a given definition into a dict
def format_def(lang, text):
    return {"language": lang, "definition": text}

def format_translation(text):
    return text.lower().replace(".", "")

# formats a given line and prints it out
# expects a dict
def format_print_line(line):
    d = line["date"]
    w = line["word"]
    print(f"[{d}] {w}:")
    for defs in line["definitions"]:
        print(f'[{defs["language"]}] {defs["definition"]}')

# fetches the english definition of an english word
def fetch_definition(word):
    try:
        response = requests.get(f"{dictionaryAPI}/en/{word}")
        data = response.json()
    except requests.exceptions.RequestException:
        print(f"Network error")
        sys.exit(1)

    try:
        first_definition = data['entries'][0]['senses'][0]['definition']
        # language_name = data['entries'][0]['language']['name']
        part_speech = data['entries'][0]['partOfSpeech']

    except (KeyError, IndexError):
        print(f"No definition found for {word}")
        sys.exit(1)

    definition = f"{word.capitalize()} ({part_speech}) - {first_definition}"
    return definition


# fetches the translation of a definition
def fetch_translation(text, in_language, out_language):
    my_params = {
        "q": text,
        "langpair": f"{in_language}|{out_language}"
    }

    try:
        response = requests.get(translationAPI, params=my_params) 
        data = response.json()
    except requests.exceptions.RequestException:
        print(f"Network error")
        sys.exit(1)

    return data["responseData"]["translatedText"]