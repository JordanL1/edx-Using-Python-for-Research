import time
from collections import Counter

def count_words(text):
    text = text.lower()
    punctuation = [".",",","!","?",";",":","'",'"']

    # remove punctuation
    for ch in punctuation:
        text = text.replace(ch, "")
    
    word_counts = {}
    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def count_words2(text):
    text = text.lower()
    punctuation = [".",",","!","?",";",":","'",'"']
    # remove punctuation
    for ch in punctuation:
        text = text.replace(ch, "")
    
    word_counts = Counter(text.split(" "))

    return word_counts

def read_book(title_path):
    """
    Read book and return as string.
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r","")

    return text
