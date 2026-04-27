import json
import uuid

from datetime import datetime

# {
#     id: 
#     word: fire,
#     definitions: [
#         {
#             language: it
#             definition: fire is a thing...
#         }
#     ]
#     date: now()
# }

class Record:
    def __init__(self, word, definitions):
        self.id = str(uuid.uuid4())
        self.word = word
        self.definitions = definitions
        self.date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def print_out(self):
        print(self.word)
        for d in self.definitions:
            print(d)
        
        for l in self.languages:
            print(l)

    def to_json(self):
        return json.dumps(self.__dict__)

    def write_to_history(self):
        with open("history.json", "a") as history:
            history.write(self.to_json() + "\n")

def print_last_n(n):
    with open("history.json") as file_history:
        lines = file_history.readlines()

        for line in lines[-n:]:
            line = json.loads(line)
            d = line["date"]
            w = line["word"]
            print(f"[{d}] {w}:")
            for defs in line["definitions"]:
                print(f"[{defs["language"]}] {defs["definition"]}")

