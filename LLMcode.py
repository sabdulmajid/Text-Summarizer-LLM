import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from heapq import nlargest

def summarize_text(file_path, n):
    # read text from file
    with open(file_path, 'r') as f:
        text = f.read()
        
    # tokenize the text into words and sentences
    words = word_tokenize(text.lower())
    sentences = sent_tokenize(text)

    # remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and word.isalnum()]
    sentences = [sentence for sentence in sentences if sentence.isalnum()]