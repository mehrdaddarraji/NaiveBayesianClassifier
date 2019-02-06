# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello Hubba Bubba Haibo\n")

import pandas as pd 
from pandas import DataFrame

file = open("lab_train.txt", "r")
lines = file.readlines()
lines.pop(0)
file.close()

reviews = []
sentiments = []

for line in lines: 
    
    index = 0
    char = ''
    
    while char != ',' and index < len(line):
        
        char = line[index]
        index += 1
        
    review = line[index + 1:-7]
    reviews.append(review)

    score = int(line[-4])
    
    if score >= 3:
        sentiments.append(1.0)
        print("positive")
    else:
        sentiments.append(0.0)
        print("neg")
        
    

df = DataFrame({'Review':reviews, 'Sentiments':sentiments})