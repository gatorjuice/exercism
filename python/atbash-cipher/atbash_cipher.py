import string
import re


alphabet = string.lowercase[0:26]


def decode():
    pass

def encode(message):
    return ''.join([transform(re.match('[a-zA-Z]', char).string) for char in message if re.match('[a-zA-Z]', char)])

def transform(letter):
    return alphabet[25-alphabet.index(letter.lower())]
