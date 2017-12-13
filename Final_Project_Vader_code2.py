# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:38:02 2017

@author: datalab
"""

# FINAL CODE
#Importing Packages
import pandas as pd
import numpy as np

#importing the dataset 
reviews=pd.read_csv("S:/DAEN-690 Project data-Krish/inTrain.csv", encoding="latin1")

#text="My girlfriend and I stayed here for 3 nights and loved it. The location of this hotel and very decent price makes this an amazing deal. When you walk out the front door Scott Monument and Princes street are right in front of you, Edinburgh Castle and the Royal Mile is a 2 minute walk via a close right around the corner, and there are so many hidden gems nearby including Calton Hill and the newly opened Arches that made this location incredible."
#vs = analyzer.polarity_scores(text)
#vs['compound'] 

#Importing VADER package
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()

#Creating a new list 'd'    
d=[]

count=0
n=len(reviews)
while(count< n):
    sentence=reviews['text'][count]
    
    vs = analyzer.polarity_scores(sentence)
    d.append({'Business ID':reviews['business_id'][count], 'Vader Score' : vs['compound'], 'Original Star rating': reviews['stars'][count]})    
    count+=1
d    
type(d)
df=pd.DataFrame(d)
df
#grouping by business ID
new=(df.groupby('Business ID')
   .....:    .agg({'Vader Score':'mean', 'Original Star rating':'mean'})
   .....:    .reset_index()
   .....: )
new.to_csv('FinalProject_690_2.csv', encoding='utf-8', index=True)
vader_stars=[]

#Creating star rating for Vader Scores
for row in new['Vader Score']:
    if row>0.9:
        vader_stars.append(5)
    elif row >0.75:
        vader_stars.append(4.5)
    elif row >0.5:
        vader_stars.append(4)
    elif row > 0.25:
        vader_stars.append(3.5)
    elif row > 0:
        vader_stars.append(3)
    elif row > -0.25:
        vader_stars.append(2.5)
    elif row >-0.5:
        vader_stars.append(2)
    elif row >-0.75:
        vader_stars.append(1)
    elif row < -0.76:
        vader_stars.append(0)
        
new['New Star Rating(Vader)']= vader_stars        
new.to_csv('FinalProject_690_3.csv', encoding='utf-8', index=True)
    
    
