#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:58:01 2017

@author: jiahaoyuan
"""

#tokenize, stem, lowercase, stopwords
from nltk.corpus import reuters

from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import re
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")
#Stoplist = []
#f3 = open('stopwords.txt', 'r')
#for x in f3:
#    Stoplist.append(x[:-1])
#f3.close()

def tokenize(text):
    min_length = 3
    # 1. tokenize
    words = list(map(lambda word: word.lower(), word_tokenize(text)))

    
    # 2. stopwords
    words = [word for word in words
                     if word not in cachedStopWords]

    
    # 3. stem
    tokens = (list(map(lambda token: PorterStemmer().stem(token),words)))

    
    # 4. words made by letters
    p = re.compile('[a-zA-Z]+');
    filtered_tokens = list(filter(lambda token: p.match(token) and len(token)>= min_length,tokens))


    return filtered_tokens




