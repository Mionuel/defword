import json

import click
import requests
import requests_cache

from history import Word

dictionaryAPI = "https://freedictionaryapi.com/api/v1/entries"
translationAPI = "https://api.mymemory.translated.net/get"

requests_cache.install_cache('requests_cache', expire_after=86400)

@click.command()
@click.argument('word')
@click.option('-o', '--output', 'output_language', multiple=True, 
              help='The target (output) language(s). This flag can be used multiple times in order to define the word in multiple languages.')
@click.option('--no-cache', 'no_cache', is_flag=True, help='Disables the requests caching for this call.')
@click.option('--clear-cache', 'clear_cache', is_flag=True, help='Resets the cache file.')
# @click.option('-h', '--history', 'history', type=int, help='This flag prints out the last 5 (default) or n definition lookups.')
# @click.option('-i', '--input', 'input_language', help='The input language.')
def defword(word, output_language, no_cache, clear_cache):
    if clear_cache:
        requests_cache.uninstall_cache()

    word_s = sanitize_word(word)

    definitions = []
    if no_cache:
        with requests_cache.disabled():
            definitions.append(fetch_definition(word_s))
    else:
        definitions.append(fetch_definition(word_s))

    if output_language:
        for l in output_language:
            translated = fetch_translation(definitions[0], "en", l)
            definitions.append(translated)

    for d in definitions:
        print(d)

# sanitezes the word by making it lowercase and trimming white spaces
def sanitize_word(word):
    return word.lower().strip()

# fetches the english definition of an english word
def fetch_definition(word):
    response = requests.get(f"{dictionaryAPI}/en/{word}")
    data = response.json()

    first_definition = data['entries'][0]['senses'][0]['definition']
    language_name = data['entries'][0]['language']['name']
    part_speech = data['entries'][0]['partOfSpeech']

    definition = f"{word.capitalize()} ({language_name} {part_speech}) - {first_definition}"
    return definition


# fetches the translation of a definition
def fetch_translation(text, in_language, out_language):
    my_params = {
        "q": text,
        "langpair": f"{in_language}|{out_language}"
    }

    response = requests.get(translationAPI, params=my_params) 

    data = response.json()   
    return data["responseData"]["translatedText"]
  
if __name__ == '__main__':
    defword() 
