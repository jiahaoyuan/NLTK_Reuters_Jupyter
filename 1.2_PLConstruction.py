#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 19:40:46 2017

@author: jiahaoyuan
"""

from nltk.corpus import reuters
from Standard import tokenize
import json

Dict = {}

document = reuters.fileids()
for doc in document:
    x = tokenize(reuters.raw(doc))

    #x = list(set(x))

    for words in x:
        if words in Dict:
            if doc in Dict[words]:
                Dict[words][doc]= Dict[words][doc]+1
            else: 
                Dict[words][doc] = 1
        else:
            Dict[words] = {doc:1}
        


with open('ProjectPostingList.json', 'w') as file:
     json.dump(Dict, file)
     
     