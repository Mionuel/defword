import json

import click
import requests
import requests_cache

from pprint import pprint

from history import Record, print_last, print_oldest
from helpers import sanitize_word, format_def

dictionaryAPI = "https://freedictionaryapi.com/api/v1/entries"
translationAPI = "https://api.mymemory.translated.net/get"

# This "constant" represents the default language code
EN_CODE = "en"

requests_cache.install_cache('requests_cache', expire_after=86400)

@click.group()
def defword():
    pass

@defword.command("define")
@click.argument('word')
@click.option('-o', '--output', 'output_language', multiple=True, 
              help='The target (output) language(s). This flag can be used multiple times in order to define the word in multiple languages.')
@click.option('--no-cache', 'no_cache', is_flag=True, help='Disables the requests caching for this call.')
@click.option('--clear-cache', 'clear_cache', is_flag=True, help='Resets the cache file.')
# @click.option('-i', '--input', 'input_language', help='The input language.')
def define(word, output_language, no_cache, clear_cache):
    if clear_cache:
        requests_cache.uninstall_cache()

    word_s = sanitize_word(word)

    definitions = []

    if no_cache:
        with requests_cache.disabled():
            definitions.append(format_def(EN_CODE, fetch_definition(word_s)))
    else:
        definitions.append(format_def(EN_CODE, fetch_definition(word_s)))

    record = Record(word_s, definitions)
    # pprint(record.to_json())

    if output_language:
        for l in output_language:
            translated = fetch_translation(definitions[0]["definition"], EN_CODE, l)
            # print(translated)
            definitions.append(format_def(l, translated))

    record
    if output_language: 
        for d in definitions[1:]:
            print(d["definition"])
        record = Record(word_s, definitions[1:])
    else:
        for d in definitions:
            print(d["definition"])
        record = Record(word_s, definitions)
 
    record.write_to_history()


@defword.command("history")
@click.option('--last', '-l', 'l', type=int, help='This option prints out the latest or n definition lookups.')
@click.option('--oldest', '-o', 'o', type=int, help='This option prints out the oldest 5 (default) or n definition lookups.')
def history(l, o):
    if l:
        print_last(l)

    if o:
        print_oldest(o)

    ## if neither options were provided -> print out the last 5 lookups
    if not l and not o:
        print_last(5)


# fetches the english definition of an english word
def fetch_definition(word):
    response = requests.get(f"{dictionaryAPI}/en/{word}")
    data = response.json()

    first_definition = data['entries'][0]['senses'][0]['definition']
    # language_name = data['entries'][0]['language']['name']
    part_speech = data['entries'][0]['partOfSpeech']

    definition = f"{word.capitalize()} ({part_speech}) - {first_definition}"
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
