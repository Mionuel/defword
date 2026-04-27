# sanitezes the word by making it lowercase and trimming white spaces
def sanitize_word(word):
    return word.lower().strip()

def format_def(lang, text):
    return {"language": lang, "definition": text}