# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 08:28:38 2021

@author: 60112
"""

import pandas as pd
import tweepy
from tweepy import OAuthHandler

from datetime import datetime
from matplotlib.ticker import StrMethodFormatter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import collections


import nltk 
import string
import re

stopword = nltk.corpus.stopwords.words('english')

#Variables that contains the user credentials to access Twitter API
access_token = "1418153178529292290-WNH8wmyHZf0aeUiEM8wjBhCguSojDP"
access_token_secret = "vKsbWJdsjkau0s7bjSNzFs38Lig5Q9W3gqkWvvboxotol"
consumer_key = "1LCfEHmPKIVcImonk9xW804f1"
consumer_secret = "yIzDAz2oco9NAJi5r8a08bUi3nnRMomBGSQSyxK0X2pDuoPEK0"



auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


#screen_name = "HuaweiMobile"
screen_name = "SamsungMobile"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

user_tweets = tweepy.Cursor(api.user_timeline,screen_name).items(300)


names = ["Date","Text","Retweet_count","Favorite_count","hashtags","Source"]
Sam = pd.DataFrame(columns = names)
huw = pd.DataFrame(columns = names)

def clean_text(text):
    text_lc = "".join([word.lower() for word in text if word not in string.punctuation]) # remove puntuation
    text_rc = re.sub('[0-9]+', '', text_lc)
    tokens = re.split('\W+', text_rc)    # tokenization
    text = [word for word in tokens if word not in stopword]  # remove stopwords and stemming
    return text


#user_tweets = tweepy.Cursor(api.user_timeline,screen_name).items(300)
list_tweets = [tweet for tweet in user_tweets]



#extracting and filtering data
for tweet in list_tweets:
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if (tweet.in_reply_to_status_id_str==None):
            if (tweet.created_at.year == 2021):
                if (tweet.created_at.month == 9):
                    if ((tweet.created_at.day >= 1) and (tweet.created_at.day <= 30)):
                        Sam = Sam.append({'Date': tweet.created_at , 'Text' :tweet.text, 'Retweet_count':tweet.retweet_count ,
                                            'Favorite_count' :tweet.favorite_count, 'hashtags' : "".join([i.get('text') for i in tweet.entities['hashtags']]), 'Source':tweet.source},ignore_index=True)


#huw.to_csv("Huawei.csv",index=False)

#huw.head(30)




hasht = Sam.copy()
hasht=hasht[hasht['hashtags']!='']

#new_datetime = datetime.strftime(datetime.strftime(b['Date'].astype(str),'%Y-%m-%d'))
hasht['Date']=hasht['Date'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d'))



#bar chart for retweeted_count
x = hasht.groupby('hashtags')['Retweet_count'].mean().sort_values().tail(15)
ax = x.plot(kind='barh', figsize=(15, 10), color='#86bf91', zorder=2, width=0.85)

  # Despine
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

  # Switch off ticks
ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

  # Draw vertical axis lines
vals = ax.get_xticks()
for tick in vals:
    ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

  # Set x-axis label
ax.set_xlabel("Average Retweet Count", labelpad=20, weight='bold', size=12)

  # Set y-axis label
ax.set_ylabel("Hashtags", labelpad=20, weight='bold', size=12)

  # Format y-axis label
ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))

#plt.savefig('avg_retweet.png')



#bar chart for favorite count
x = hasht.groupby('hashtags')['Favorite_count'].mean().sort_values().tail(15)
ax = x.plot(kind='barh', figsize=(15, 10), color='#a89732', zorder=2, width=0.85)

  # Despine
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

  # Switch off ticks
ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

  # Draw vertical axis lines
vals = ax.get_xticks()
for tick in vals:
    ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

  # Set x-axis label
ax.set_xlabel("Average Favorite Count", labelpad=20, weight='bold', size=12)

  # Set y-axis label
ax.set_ylabel("Hashtags", labelpad=20, weight='bold', size=12)

  # Format y-axis label
ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))

#plt.savefig('avg_fav.png')






#barchart for date vs hashtags
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.barh(hasht['hashtags'],
       hasht['Date'],
        color='#d4abab')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Hashtags")

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)

plt.show()


#wordcloud

#text = "".join(review for review in str(clean_tweet))
clean_tweet = Sam['Text'].apply(lambda x: clean_text(x))
clean_tweet = clean_tweet.value_counts(50)

#counted_words = collections.Counter(clean_tweet)
#print(clean_tweet)
wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white',max_words=100, width=1600, height=900).generate(str(clean_tweet))
#plt.figsize(figure=(10,8))
#plt.figure()
plt.figure( figsize=(10,10) )
plt.imshow(wordcloud)
plt.axis("off")
plt.show()




#line series for engagement
plt.subplots(figsize =(20, 8))

plt.plot( 'Date', 'Retweet_count', data=hasht, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.plot( 'Date', 'Favorite_count', data=hasht, marker='', color='olive', linewidth=2)
#plt.plot( 'Date', 'y3_values', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
plt.xticks(rotation=45)
# show legend
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()

# show graph
plt.show()







