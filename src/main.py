import click
import requests
from pprint import pprint

dictionaryAPI = "https://freedictionaryapi.com/api/v1/entries"

@click.command()
@click.option('-w', '--word', help='The word to define.')
def call(word):
    word_s = sanitize_word(word)
    response = requests.get(f"{dictionaryAPI}/en/{word_s}")
    data = response.json()

    first_definition = data['entries'][0]['senses'][0]['definition']
    language_name = data['entries'][0]['language']['name']
    part_speech = data['entries'][0]['partOfSpeech']

    print(f"{word_s.capitalize()} ({language_name} {part_speech}) - {first_definition}")

def sanitize_word(word):
    return word.lower().strip()
  
    
if __name__ == '__main__':
    call() 
