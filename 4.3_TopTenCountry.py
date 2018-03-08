#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:32:03 2017

@author: jiahaoyuan
"""

# TopTenCountry

from nltk.corpus import reuters
from Standard import tokenize
import json

with open('Tf-idf.json', 'r') as f: 
        TFIDF = json.load(f)

with open('Tf.json', 'r') as f: 
        TF = json.load(f)

#
#cat = reuters.categories();
#
#for c in cat:
#    filename = c+"_PL.json"
#    
    
file = open("country.txt","r")
name=[]
for line in file:
    name.append(line.split()[0])
    
print(name)

TFIDFScore = {}
TFScore = {}
for name in name:
    x = tokenize(name)

    try:
        TFIDFScore[x[0]]= TFIDF[x[0]]
        TFScore[x[0]] = TF[x[0]]
    except:
        try:
            TFIDFScore[x[0]]= 0
            TFScore[x[0]] = 0
        except:
            print()

     
import operator
sorted1 = sorted(TFIDFScore.items(), key = operator.itemgetter(1),reverse=True)
sorted2 = sorted(TFScore.items(), key = operator.itemgetter(1),reverse=True)
with open('Sorted_Country_TFIDF.json', 'w') as file:
     json.dump(sorted1, file)
with open('Sorted_Country_TF.json', 'w') as file:
     json.dump(sorted2, file)
     


