import pandas as pd 
import re
import numpy as np
import string
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer

# function to create dataframes for text and sentiment
def sentimentDataFrame(filename):
    
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
        
        
        # score of the the text turned into pos/neg
        score = int(line[-4])
        # get the text 
        review = line[index + 1:-7]
        reviews.append(review)
        
        if score >= 3:
            sentiments.append(1.0)
        else:
            sentiments.append(0.0)
            
    # creating DataFrame out of text and sentiment
    df = DataFrame({'reviews':reviews, 'sentiments':sentiments})
    return df


def main():

    # dataframes for train and test dataset
    train_df = sentimentDataFrame("lab_train.txt")
    X_train, y_train = train_df['reviews'].values, train_df['sentiments'].values
    
    
    test_df = sentimentDataFrame("lab_test.txt")
    X_test, y_test = test_df['reviews'].values, test_df['sentiments'].values
    
    
    # vectorizer for the strings
    re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')
    def tokenize(s):
       return re_tok.sub(r' \1 ', s).split()
    
    # create bag of words 
    vect = CountVectorizer(tokenizer=tokenize)
    tf_train = vect.fit_transform(X_train)
    tf_test = vect.transform(X_test)
    
    # Multinomial Bayes Classifier formula
    
    # p = sum of all feature count vectors with label 1
    p = tf_train[y_train==1].sum(0) + 1
    # q = sum of all feature count vectors with label 0
    q = tf_train[y_train==0].sum(0) + 1
    # log-count ratio r
    r = np.log((p/p.sum()) / (q/q.sum()))
    # ratio of number of positive and negative training cases.
    b = np.log(len(p) / len(q))
    
    # generate predictions on test set
    pre_preds = tf_test @ r.T + b
    preds = pre_preds.T > 0
    accuracy = (preds == y_test).mean()
    
    print (accuracy)


if __name__ == "__main__":
    main()






