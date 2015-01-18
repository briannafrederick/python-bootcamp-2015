import datetime
import json
import lxml.html as lh
from lxml.cssselect import CSSSelector

# create list of all links in the document
tree = lh.parse('http://www.presidency.ucsb.edu/sou.php')
select_anchor = CSSSelector('a')
elements = select_anchor(tree)
links = [e.get('href') for e in elements]

# filter out missing strings
links = filter(None, links)

# select links to speeches
pattern = "http://www.presidency.ucsb.edu/ws/index.php?pid="
links = [link for link in links if link.startswith(pattern)]

# helper functions to return speech elements from parsed html tree

def get_date(tree):
    date = tree.xpath("//span[@class='docdate']")[0].text_content()
    return datetime.datetime.strptime(date, "%B %d, %Y")

def get_president(tree):
    # title starts with <president>:
    title = tree.xpath("//title")[0].text_content()
    return title.split(":")[0]

def get_text(tree):
    # replace paragraph tags with new lines
    # since text_content() returns a str with tags removed
    body = tree.xpath("//span[@class='displaytext']")[0]
    for p in body.xpath("./p"):
        p.text = "\n%s\n" % p.text
    return body.text_content()

# use helper functions to extract data elements
def get_speech(tree):
    return {"president": get_president(tree),
            "text" : get_text(tree),
            "date" : get_date(tree).isoformat()}

# list of speech dictionaries
speeches = [get_speech(lh.parse(link)) for link in links]

# save as json
filename = "speeches.json"
with open(filename, 'w') as outfile:
    json.dump(speeches, outfile, indent=4)


words = [w for w in re.split('\W', text) if w]

import nltk.data
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
tokens = nltk.word_tokenize(text)

sentences = sent_detector.tokenize(text.strip())

from nltk.tokenize.punkt import PunktWordTokenizer
tokens = PunktWordTokenizer().tokenize(text)

import string
words = [w.lower() for w in tokens if w not in string.punctuation]
vocab = sorted(set(words))

from collection import Counter
word_counts = Counter(words)
# \u2014 emdash replace  -- .replaceAll("\u2014", " ")
# remove anything starting with ' # does the type of apostrophe matter 
# remove numbers
# 
