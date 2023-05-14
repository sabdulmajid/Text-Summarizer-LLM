import os
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

    # calculate word frequencies and scores
    word_freq = defaultdict(int)
    word_scores = defaultdict(int)
    for word in words:
        word_freq[word] += 1
    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_scores[word] = word_freq[word] / max_freq

    # calculate sentence scores based on reduced word frequencies and position
    sentence_scores = defaultdict(int)
    for i, sentence in enumerate(sentences):
        words = word_tokenize(sentence.lower())
        for word in words:
            if word in word_scores:
                sentence_scores[i] += word_scores[word]
        sentence_scores[i] /= len(words)
        sentence_scores[i] += (n - i) * 0.1

    # select the top n sentences with the highest scores
    top_sentences = nlargest(n, sentence_scores, key=sentence_scores.get)
    summary = ' '.join([sentences[i] for i in sorted(top_sentences)])

    # save summary to output file with "-OUTPUT" appended to the original file name
    output_path = os.path.join('output-files', os.path.basename(file_path) + '-OUTPUT')
    with open(output_path, 'w') as f:
        f.write(summary)

    return summary

# example usage
file_path = 'text-files/lone-lamppost.txt' # change this to the path of the text file you want to summarize, such as 'text-files/lone-lamppost.txt' or 'text-files/lorem-ipsum.txt'
summary = summarize_text(file_path, 3) # change the second argument to the number of sentences you want in the summary
print(summary) # print the summary
