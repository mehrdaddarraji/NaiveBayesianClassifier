import pandas as pd
import numpy as np
from pandas import DataFrame
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score

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
        if score != 3:
            review = line[index + 1:-7]
            reviews.append(review)
            
            if score >= 4:
                sentiments.append(1)
            else:
                sentiments.append(0)
            
    # creating DataFrame out of text and sentiment
    df = DataFrame({'reviews':reviews, 'sentiments':sentiments})
    return df


def main():
    
    
    
    # TFIDF Vectorizer - used to convert reviews from text to features
    stopset = set(stopwords.words('english'))
    vectorizer = TfidfVectorizer(use_idf=True, lowercase=True,
                                strip_accents='ascii', stop_words=stopset)
    
    clf = naive_bayes.MultinomialNB()
    
    for i in range (100): 

        # dataframes for train and test dataset
        train_df = sentimentDataFrame("lab_train.txt")
        X_train, y_train = vectorizer.fit_transform(train_df.reviews), train_df.sentiments
        
        test_df = sentimentDataFrame("lab_test.txt")
        X_test, y_test = vectorizer.transform(test_df.reviews), test_df.sentiments
        
        # train using naive bayes classifier
        
        clf.fit(X_train, y_train)
        
        # test models accuracy
        print (roc_auc_score(y_test, clf.predict_proba(X_test)[:,1]))
    
    # import bookings.com comments
    comments_df = pd.read_excel("evaluation_dataset.xlsx", header=None, names=['reviews'])
    
    
    
    comments_vector = vectorizer.transform(comments_df['reviews'].tolist())
    comments_df['sentiments'] = clf.predict(comments_vector)
    
    
    foo_arr = np.array(['worst place in the world, really bad, it sucks, horrible service, never coming again']) # comments_df['reviews'].tolist()
    foo_vect = vectorizer.transform(foo_arr)
    print (clf.predict(foo_vect))
    
    
    
    print (comments_df.loc[92])
    
        
if __name__ == "__main__":
    main()






