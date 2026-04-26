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
# @click.option('-h', '--history', 'history', type=int, help='This flag prints out the last 5 (default) or n definition lookups.')
# @click.option('-i', '--input', 'input_language', help='The input language.')
def defword(word, output_language, history):
    word_s = sanitize_word(word)

    response = requests.get(f"{dictionaryAPI}/en/{word_s}")
    data = response.json()

    first_definition = data['entries'][0]['senses'][0]['definition']
    language_name = data['entries'][0]['language']['name']
    part_speech = data['entries'][0]['partOfSpeech']

    definition = f"{word_s.capitalize()} ({language_name} {part_speech}) - {first_definition}"

    if not output_language:
        print(definition)
    else:
        for l in output_language:
            print(translate(first_definition, "en", l))


def sanitize_word(word):
    return word.lower().strip()

def translate(text, in_language, out_language):
    my_params = {
        "q": text,
        "langpair": f"{in_language}|{out_language}"
    }

    response = requests.get(translationAPI, params=my_params) 

    data = response.json()   
    return data["responseData"]["translatedText"]
  
if __name__ == '__main__':
    defword() 
