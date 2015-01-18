from __future__ import print_function

import json
import re

filename = "speeches.json"
with open(filename) as infile:
    speeches = json.load(infile)

# number of speeches
len(speeches)

# list the presidents
[speech['president'] for speech in speeches]

# list the dates
[speech['date'] for speech in speeches]

# get text from first speech and make list of words
text = speeches[0]['text'] 
words = [w for w in re.split('\W', text) if w]
vocab = sorted(set(words))

from collection import Counter
word_counts = Counter(words)

# function to extract president and word count
def summarize(speech):
    text = speech['text']
    words = [w for w in re.split('\W', text) if w]
    return (speech['president'], len(words), speech['date'])

summary = [summarize(speech) for speech in speeches]

# https://wiki.python.org/moin/HowTo/Sorting
from operator import itemgetter
[speech[2] for speech in sorted(summary, key=itemgetter(1))]
