import click
import requests_cache

from history import Record, print_last, print_oldest, clear_history, print_duplicate_lookups
from helpers import sanitize_word, format_def, fetch_definition, fetch_translation, format_translation

from epilogs import history_examples, define_examples, cache_examples

# This "constant" represents the default language code
EN_CODE = "en"

requests_cache.install_cache('requests_cache', expire_after=86400)

@click.group()
def defword():
    pass

@defword.command("define", epilog=define_examples)
@click.argument('word')
@click.option('-o', '--output', 'output_language', multiple=True, 
              help='Set the target (output) language. Can be used multiple times.')
@click.option('--no-cache', 'no_cache', is_flag=True, help='Ignore cached requests for this call.')
@click.option('-i', '--input', 'input_language', help='Set the input language. Can only be used once.')
def define(word, output_language, no_cache, input_language):
    """Defines the word"""
    word_s = sanitize_word(word)

    definitions = []

    if input_language and input_language != EN_CODE:
        english_translation = fetch_translation(word_s, input_language, EN_CODE)
        word_s = format_translation(english_translation)

    if no_cache:
        with requests_cache.disabled():
            definitions.append(format_def(EN_CODE, fetch_definition(word_s)))
    else:
        definitions.append(format_def(EN_CODE, fetch_definition(word_s)))

    record = Record(word_s, definitions)

    if output_language:
        for l in output_language:
            translated = fetch_translation(definitions[0]["definition"], EN_CODE, l)
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


@defword.command("history", epilog=history_examples)
@click.option('--last', '-l', 'l', type=int, help='Print out the latest n definition lookups.')
@click.option('--oldest', '-o', 'o', type=int, help='Print out the oldest n definition lookups.')
@click.option('--duplicates', '-d', 'd', is_flag=True, help='Print out the words that were looked up more than once.')
@click.option('--clear', 'clear', is_flag=True, help='Confirm and clear the history file.')
def history(l, o, d, clear):
    """Manages your definition lookups history."""
    if l:
        print_last(l)
        return

    if o:
        print_oldest(o)
        return

    if clear:
        print("Are you sure you want to clear the history? [y/n]")
        response = input().lower()
        if response == "y":
            clear_history()
        else:
            return
        
    if d:
        print_duplicate_lookups()
        return

    ## if no options were provided -> print out the last 5 lookups
    if not l and not o:
        print_last(5)
        return
    
@defword.command("cache", epilog=cache_examples)
@click.option('--clear', '-c', 'clear', is_flag=True, help='Reset the cache file.')
def cache(clear):
    """Manages the request caching"""
    if clear:
        requests_cache.clear()
        print("Cache cleared successfully!")

  
if __name__ == '__main__':
    defword(prog_name="defword") 
