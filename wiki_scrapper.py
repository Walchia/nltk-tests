#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from nltk.probability import FreqDist
from nltk import tokenize
from nltk.corpus import stopwords
import nltk

book_file = r"/home/wojciech/Programowanie/python/nltk_testy/james_henry_the_american.txt"

def tokenize_book():
    with open(book_file, mode='r') as fr:
        raw = fr.read()
    tokens = tokenize.regexp_tokenize(raw, "\w+")
    sw = stopwords.words('english')
    words_sw = [w.lower() for w in tokens]
    words = [w for w in words_sw if w not in sw]
    return words
    
def main():
    words = tokenize_book()
    fdist = nltk.FreqDist(words)
    mc = fdist.most_common(50)
    print(mc)
    print(type(fdist))
    # fdist[:50].plot()


if __name__ == "__main__":
    # execute only if run as a script
    main()
