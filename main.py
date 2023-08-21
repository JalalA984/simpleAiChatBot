import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tensorflow
import random
import json

# TODO: tflearn import causing bug
#import tflearn

with open("intents.json") as file:
    data = json.load(file)

print(data)


