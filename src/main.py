import click
import requests

dictionaryAPI = "https://freedictionaryapi.com/api/v1/entries"
translationAPI = "https://api.mymemory.translated.net/get"

@click.command()
@click.option('-w', '--word', required=True, help='The word to define.')
@click.option('-o', '--output', 'output_language', help='The target (output) language.')
# @click.option('-i', '--input', 'input_language', help='The input language.')
def defword(word, output_language):
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
        print(translate(first_definition, output_language))

def sanitize_word(word):
    return word.lower().strip()

def translate(text, language):
    my_params = {
        "q": text,
        "langpair": f"en|{language}"
    }

    response = requests.get(translationAPI, params=my_params) 

    data = response.json()   
    return data["responseData"]["translatedText"]
  
if __name__ == '__main__':
    defword() 
