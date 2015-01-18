from __future__ import print_function

import json

import nltk.data
from nltk.tokenize.punkt import PunktWordTokenizer

filename = "speeches.json"
with open(filename) as infile:
    speeches = json.load(infile)

text = speeches[0]['text']

#tokens = nltk.word_tokenize(text)
tokens = PunktWordTokenizer().tokenize(text)
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = sent_detector.tokenize(text.strip())
