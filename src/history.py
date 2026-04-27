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
        return json.dumps(self.__dict__, indent=4)

    def write_to_history(self):
        with open("history.json", "a") as history:
            history.write(self.to_json() + "\n")

