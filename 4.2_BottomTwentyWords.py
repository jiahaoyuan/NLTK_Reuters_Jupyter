#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:28:59 2017

@author: jiahaoyuan
"""

# Bottome Twenty Words

import json

with open('Sorted_TFIDF.json', 'r') as f: 
        Sorted = json.load(f)

with open('Stemmed_UnStemmed_Dict.json', 'r') as f: 
        Stemmed_UnStemmed_Dict = json.load(f)


topTwenty = Sorted[-20:]
print(topTwenty)
for a in topTwenty:
    try:
        print(Stemmed_UnStemmed_Dict[a[0]])
    except:
        print()
