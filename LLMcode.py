import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from heapq import nlargest

def summarize_text(file_path, n):
    # read text from file
    with open(file_path, 'r') as f:
        text = f.read()
