import json

# sanitizes the word by making it lowercase and trimming white spaces
def sanitize_word(word):
    return word.lower().strip()

# formats a given definition into a dict
def format_def(lang, text):
    return {"language": lang, "definition": text}

# formats a given line and prints it out
def format_print_line(line):
        line = json.loads(line)
        d = line["date"]
        w = line["word"]
        print(f"[{d}] {w}:")
        for defs in line["definitions"]:
            print(f'[{defs["language"]}] {defs["definition"]}')