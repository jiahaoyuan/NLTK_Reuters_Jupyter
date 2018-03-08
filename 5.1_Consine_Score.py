#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:20:11 2017

@author: jiahaoyuan
"""

from nltk.corpus import reuters
#from Standard import tokenize
import json


# TfD Construction
# Sample Word "japan, Korea, Trade"
query = 'Japan Korea Trade'

query = tokenize(query)
print(query)

from nltk.corpus import reuters
import json
import math

with open('idf.json', 'r') as f: 
        IDF = json.load(f)


with open('CleanPostingList.json', 'r') as f: 
        PL = json.load(f)


#doc
# Wt,q = idf
# L = (q1^2+q2^2)^0.5
# Wt,d = Dtf/L
# Sum of Wt,q * Wt,d

print("Japan IDF ", IDF['japan'])
print("korea IDF ", IDF['korea'])
print("trade IDF ",IDF['trade'], "\n\n")

Score = {}
Length = {}

for q in query:
    try:
        for doc in PL[q]:
            if doc in Score:
                Score[doc] = Score[doc] + PL[q][doc]*IDF[q]
            else:
                Score[doc] = PL[q][doc]*IDF[q]
            if doc in Length:
                Length[doc] = Length[doc]+PL[q][doc]**2
            else:
                Length[doc] = PL[q][doc]**2
    

        for doc in Length:
            Length[doc] = (Length[doc])**0.5


        FinalScore = {}
        for x in Score:
            FinalScore[x] = Score[x]/Length[x]

    except:
        print()
    
import operator
sorted_d_R = sorted(FinalScore.items(), key=operator.itemgetter(1),reverse=True)   

with open('japan_korea_trade.json', 'w') as file:
     json.dump(sorted_d_R, file)



for x in sorted_d_R[0:10]:
    
    print(x[0],'%s' % float('%.3g' % Score[x[0]]), '%s' % float('%.3g' % Length[x[0]]), '%s' % float('%.3g' % FinalScore[x[0]]))
    for q in query:
        try:
          print(PL[q][x[0]]) 
        except: print("not exist");