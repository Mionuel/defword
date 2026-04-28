import json
import uuid

from datetime import datetime
from collections import deque
from itertools import islice

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

# The history.json file will be created in the project's root folder
HISTORY_PATH = "./history.jsonl"

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
        with open(HISTORY_PATH, "a") as history:
            history.write(self.to_json() + "\n")

def print_last(n):
    with open(HISTORY_PATH) as file_history:
        last_lines = deque(file_history, maxlen=n)

        for line in last_lines:
            format_print_line(line)

def print_oldest(n):
    with open(HISTORY_PATH) as file_history:
        for line in islice(file_history, n):
            format_print_line(line)

def format_print_line(line):
        line = json.loads(line)
        d = line["date"]
        w = line["word"]
        print(f"[{d}] {w}:")
        for defs in line["definitions"]:
            print(f'[{defs["language"]}] {defs["definition"]}')
        print()

