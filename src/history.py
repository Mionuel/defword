import json
import uuid

from datetime import datetime
from collections import Counter, deque
from itertools import islice

from helpers import format_print_line, HISTORY_PATH
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

# A class for memorizing a word and its definitions inside an object
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

# prints out the latest n definition lookups
def print_last(n):
    is_first_line = True

    with open(HISTORY_PATH) as file_history:
        last_lines = deque(file_history, maxlen=n)

        for line in last_lines:
            if not is_first_line:
                print()

            line = json.loads(line)
            format_print_line(line)
            is_first_line = False

# prints out the oldest n definition lookups
def print_oldest(n):
    is_first_line = True

    with open(HISTORY_PATH) as file_history:
        for line in islice(file_history, n):
            if not is_first_line:
                print()
                
            line = json.loads(line)
            format_print_line(line)
            is_first_line = False

def print_duplicate_lookups():
    words = []
    with open(HISTORY_PATH, 'r') as history_file:
        for line in history_file:
            line = json.loads(line)
            words.append(line['word'])
    
    # creates a dictionary word_counts of word:counts pairs
    word_counts = Counter(words)
    
    if not any(count > 1 for count in word_counts.values()):
        print("No words were looked up more than once.")
        return
    
    # most_common sort the counts in descending order
    for word, count in word_counts.most_common():
        # only the words that occured more than once will be printed
        if count > 1:
            print(f"{word} - {count} times")

def clear_history():
    with open(HISTORY_PATH, 'w') as file_history:    
        pass