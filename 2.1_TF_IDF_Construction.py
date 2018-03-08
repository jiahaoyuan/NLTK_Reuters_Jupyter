#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:11:56 2017

@author: jiahaoyuan
"""
from nltk.corpus import reuters
import json
import math

def TF_IDF_Construction():
    with open('CleanPostingList.json', 'r') as f: 
            data = json.load(f)
    
    #### TF ####
    TF = {}
    for x in data:
        for y in data[x]:
            if x in TF:
                TF[x] += data[x][y]
            else:
                TF[x] = data[x][y]
                
    with open('Tf.json', 'w') as file:
         json.dump(TF, file)
         
    #### DF ####
    DF = {}
    for x in data:
        DF[x]= len(data[x])
    
    with open('Df.json', 'w') as file:
         json.dump(DF, file)
    
    #### IDF ####
    IDF = {}
    for x in DF:
        IDF[x] = math.log10(10790/DF[x])
    
    with open('idf.json', 'w') as file:
         json.dump(IDF, file)

    
    #### TF-IDF ####
    TFIDF = {}
    for x in TF:
        TFIDF[x] = (1+math.log10(TF[x]))*IDF[x]
        
    with open('Tf-idf.json', 'w') as file:
         json.dump(TFIDF, file)
         
    import operator
    sorted = sorted(TFIDF.items(), key = operator.itemgetter(1),reverse=True)
    
    with open('Sorted_TFIDF.json', 'w') as file:
         json.dump(sorted, file)

#10790 total
