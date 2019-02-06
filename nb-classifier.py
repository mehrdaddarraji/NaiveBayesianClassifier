import pandas as pd 
import re
from pandas import DataFrame

# function to create dataframes for text and sentiment
def sentimentDataFram(filename):
    
    # import train data
    file = open(filename, "r")
    lines = file.readlines()
    lines.pop(0)
    file.close()
    
    # data structure for text and sentiment
    reviews = []
    sentiments = []
    
    # a DataFrame for the text and the corresponding sentiment
    for line in lines: 
        
        index = 0
        char = ''
        
        # find the start of the comment
        while char != ',' and index < len(line):
            
            char = line[index]
            index += 1
        
        # get the text     
        review = line[index + 1:-7]
        reviews.append(review)
        
        # score of the the text turned into pos/neg
        score = int(line[-4])
        
        if score >= 3:
            sentiments.append(1.0)
            print("positive")
        else:
            sentiments.append(0.0)
            print("neg")
            
    # creating DataFrame out of text and sentiment
    df = DataFrame({'Review':reviews, 'Sentiments':sentiments})
    return df

# dataframes for train and test dataset
train_df = sentimentDataFrame("lab_train.txt")
test_df = sentimentDataFrame("lab_test.txt")

# vectorizer for the strings
re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')
def tokenize(s):
    return re_tok.sub(r' \1 ', s).split()






