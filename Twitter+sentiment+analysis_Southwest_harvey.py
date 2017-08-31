
# coding: utf-8

# In[1]:


import tweepy
import csv
import pandas as pd
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import re


# In[17]:


####input your credentials here
consumer_key = '2701n8yQhIWIGWeld9Pg1pCzo'
consumer_secret = 'wi9V8ejZdl7MhW8S1Xv2bzqwry8AamEugU0LMFb1w0gxS4imgL'
access_token = '104434883-8GlZB2wm7Vn3XKakFBnPlXl2ktgQWTpqC462gTW4'
access_token_secret = '8nOct9wjzZ8bCgrWbttRW1ksoRXwpOOXqs8c5uuF7ZmPy'


# class listener(StreamListener):
# 
#     def on_data(self, data):
#         print(data)
#         return(True)
# 
#     def on_error(self, status):
#         print status
# 
# auth = OAuthHandler(ckey, csecret)
# auth.set_access_token(atoken, asecret)
# 
# twitterStream = Stream(auth, listener())
# twitterStream.filter(track=["SouthwestAirlines"])

# In[19]:


ashishauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
ashishauth.set_access_token(access_token, access_token_secret)
api = tweepy.API(ashishauth,wait_on_rate_limit=True)


# In[5]:


#####Southwest Airlines

# Open/Create a file to append data

csvFile = open('s1a.csv', 'a')

#Use csv Writer

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#SouthwestAirlines",count=1000000,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    
csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


# In[21]:


#replicating it for hurricane harvey

public_tweets = api.search('Harvey')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

