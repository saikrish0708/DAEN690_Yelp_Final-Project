# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:38:02 2017

@author: datalab
"""
# FINAL CODE

#North Carolina State

import pandas as pd
import numpy as np

#importing the dataset

reviews_nc=pd.read_csv("C:/Users/Saikrishna Nellutla/Downloads/nc.csv", encoding="latin1")

#importing Vader Package
    
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
     analyzer = SentimentIntensityAnalyzer()


#Creating a new data frame with original rating and Vader scores

d=[]

count=0
n=len(reviews_nc)
while(count< n):
    sentence=reviews_nc['text'][count]
    
    vader_score = analyzer.polarity_scores(sentence)
    d.append({'Business ID':reviews_nc['business_id'][count], 'Vader Score' : vader_score['compound'], 'Original Star rating': reviews_nc['stars'][count], 'city' : reviews_nc['city'], 'state': reviews_nc['state'], 'categories': reviews_nc['categories']})    
    count+=1
d    
type(d) 
df=pd.DataFrame(d)
df

new=(df.groupby(['Business ID'])
   .....:    .agg({'Vader Score':'mean', 'Original Star rating':'mean'})
   .....:    .reset_index()
   .....: )

#Creating Star rating from Vader Scores

vader_stars=[]

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

#Creating a csv file with original rating and Vader rating

vader=pd.DataFrame(vader_stars)        
new['New Star Rating(Vader)']= vader        
new.to_csv('FinalProject_690_nc.csv', encoding='utf-8', index=True)

# Ohio State
    
#importing the dataset

reviews_oh=pd.read_csv("C:/Users/Saikrishna Nellutla/Downloads/nc.csv", encoding="latin1")

#importing Vader Package
    
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
     analyzer = SentimentIntensityAnalyzer()


#Creating a new data frame with original rating and Vader scores

d=[]

count=0
n=len(reviews_nc)
while(count< n):
    sentence=reviews_nc['text'][count]
    
    vader_score = analyzer.polarity_scores(sentence)
    d.append({'Business ID':reviews_oh['business_id'][count], 'Vader Score' : vader_score['compound'], 'Original Star rating': reviews_oh['stars'][count], 'city' : reviews_oh['city'], 'state': reviews_oh['state'], 'categories': reviews_oh['categories']})    
    count+=1
d    
type(d) 
df=pd.DataFrame(d)
df

new=(df.groupby(['Business ID'])
   .....:    .agg({'Vader Score':'mean', 'Original Star rating':'mean'})
   .....:    .reset_index()
   .....: )

#Creating Star rating from Vader Scores

vader_stars=[]

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

#Creating a csv file with original rating and Vader rating

vader=pd.DataFrame(vader_stars)        
new['New Star Rating(Vader)']= vader        
new.to_csv('FinalProject_690_oh.csv', encoding='utf-8', index=True)     

# Pennsylvania State

#importing the dataset

reviews_pa=pd.read_csv("C:/Users/Saikrishna Nellutla/Downloads/pa.csv", encoding="latin1")

#importing Vader Package
    
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
     analyzer = SentimentIntensityAnalyzer()


#Creating a new data frame with original rating and Vader scores

d=[]

count=0
n=len(reviews_pa)
while(count< n):
    sentence=reviews_nc['text'][count]
    
    vader_score = analyzer.polarity_scores(sentence)
    d.append({'Business ID':reviews_pa['business_id'][count], 'Vader Score' : vader_score['compound'], 'Original Star rating': reviews_pa['stars'][count], 'city' : reviews_pa['city'], 'state': reviews_pa['state'], 'categories': reviews_pa['categories']})    
    count+=1
d    
type(d) 
df=pd.DataFrame(d)
df

new=(df.groupby(['Business ID'])
   .....:    .agg({'Vader Score':'mean', 'Original Star rating':'mean'})
   .....:    .reset_index()
   .....: )

#Creating Star rating from Vader Scores

vader_stars=[]

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

#Creating a csv file with original rating and Vader rating

vader=pd.DataFrame(vader_stars)        
new['New Star Rating(Vader)']= vader        
new.to_csv('FinalProject_690_pa.csv', encoding='utf-8', index=True)
