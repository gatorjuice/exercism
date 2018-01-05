from math import sqrt
import re

def encode(phrase):
    short_phrase = re.sub('[^A-Za-z0-9]+', '', phrase).lower()
    phrase_length = len(short_phrase)
    columns = int(sqrt(phrase_length))
    rows = columns + 1
    crypto_square = []
    for r in rows:



