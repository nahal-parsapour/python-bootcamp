# Analyze text
from collections import Counter

def word_count(text):
    """
    Return the number of words in a text.
    """
    return len(text.split())

def char_frequency(text):
    """
    Return a dictionary counting frequency of each non-whitespace character.
    """
    chars = [ch for ch in text if not ch.isspace()]
    return dict(Counter(chars))