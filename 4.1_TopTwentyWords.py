#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 21:28:40 2017

@author: jiahaoyuan
"""
# TOP Ten TFIDF Words


import json

with open('Sorted_TFIDF.json', 'r') as f: 
        Sorted = json.load(f)

with open('Stemmed_UnStemmed_Dict.json', 'r') as f: 
        Stemmed_UnStemmed_Dict = json.load(f)



#
#name = []
#for x in topTen:
#    name.append(x[0])
#    
#
#
#value = []
#for x in topTen:
#    value.append(x[1])
#

#import numpy as np
#x = np.array([0,1,2,3,4,5,6,7,8,9])
#plt.xticks(x, name)
#plt.plot(x, value)
##plt.axis([0,6,0,300])
#plt.show()


topTwenty = Sorted[0:20]
print(topTwenty)
for a in topTwenty:
    try:
        print(Stemmed_UnStemmed_Dict[a[0]])
    except:
        print()





