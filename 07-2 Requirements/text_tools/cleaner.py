# made it with(Terminal): New-Item -ItemType File -Path text_tools\cleaner.py
# build 2 modules: remove_extra_spaces & remove_punctuation
import re

def remove_extra_spaces(text):
    """
    Replace multiple consecutive whitespace characters with a single space.
    """
    return ' '.join(text.split())

def remove_punctuation(text):
    """
    Remove all punctuation marks (keeps letters, digits, and whitespace).
    """
    return re.sub(r'[^\w\s]', '', text)