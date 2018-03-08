#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:34:58 2017

@author: jiahaoyuan
"""

# Word -> Stemmed -> UnStemmed


from nltk.corpus import reuters
from Standard import tokenize
import json

Stemmed_Unstemmed_Dict = {}

document = reuters.fileids()
for doc in document:
    if (doc!='test/.DS_Store'):
        words = reuters.words(doc)
        for w in words:
            x = tokenize(w)
            try:
                if x[0] in Stemmed_Unstemmed_Dict:
                    if w not in Stemmed_Unstemmed_Dict[x[0]]:
                        Stemmed_Unstemmed_Dict[x[0]].append(w)
                else:
                    Stemmed_Unstemmed_Dict[x[0]]=[w]
            except:
                i=0
            
        
with open('Stemmed_Unstemmed_Dict.json', 'w') as file:
     json.dump(Stemmed_Unstemmed_Dict, file)
     