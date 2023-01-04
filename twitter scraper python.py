#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:47:09 2021
@author: yandatao
"""
# Please note that the snscrape can't collect RETWEETS
# Avoid high frequency requests:
#  - For ONE keywords/users, you collect 100K tweets                     -> ONE request, it's fine
#  - For 1000 keywords/users, you collect 1 tweet from each keyword/user -> 1K requests, may cause IP blocking

# Please make sure the snscrape has been installed in the Python environment
# If you are using PythonAnywhere
#   Step 1: Open $Bash on your PythonAnywhere Dashboard
#   Step 2: Enter the following command: pip3.9 install --user git+https://github.com/JustAnotherArchivist/snscrape.git
# The Python version has to be greater than 3.8

import snscrape.modules.twitter as sntwitter
import pandas as pd

key_word = "olympics sport climbing"           # Declare a keyword used to search tweets -> Tweet search by keyword
user_name = "@SportsCenter"   # Declare a user name used to search tweets -> Tweet search by user
from_date = "2021-07-23"      # Declare a start date
end_date = '2022-11-18'       # Declare a end date
count = 100000                  # The maximum number of tweets

tweets_list_keyword = [] # A list used to store the returned results for keyword search
tweets_list_user = []    # A list used to store the retuned results for user search
#### Scraping tweets from a specific keyword ####
command_keyword = key_word+' since:'+from_date+' until:'+end_date
print("Scraping data for keyword:",key_word)
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(command_keyword).get_items()):
    # For other available attributes: https://github.com/JustAnotherArchivist/snscrape/issues/115
    tweets_list_keyword.append([tweet.date,tweet.id, tweet.content, tweet.user.username, tweet.url, tweet.lang, tweet.likeCount, tweet.retweetCount])
    if i>count:
        break;
# Create a dataframe from the tweets list above
tweets_df_keyword = pd.DataFrame(tweets_list_keyword, columns=['Datetime','Tweet Id', 'Text', 'Username', 'url', 'language', 'likes', 'retweets'])
tweets_df_keyword['Datetime'] = tweets_df_keyword['Datetime'].astype(str).str[:-6]
tweets_df_keyword.to_csv("tweets_sportclimbing.csv",index=False) # Export to a csv file
#tweets_df_keyword.to_excel("tweets_keywords.xlsx",index=False) # Uncomment this line if you prefer an Excel file
print("Scraped data have been exported to the csv file")

#### Scraping tweets from a specific user’s account ####
#command_user = 'from:'+user_name+' since:'+from_date+' until:'+end_date
#print("Scraping data for user:",user_name)
#for i,tweet in enumerate(sntwitter.TwitterSearchScraper(command_user).get_items()):
#    tweets_list_user.append([tweet.date,tweet.id, tweet.rawContent, tweet.user.username, tweet.url])
#    if i > count:
#        break;

# Create a dataframe from the tweets list above
#tweets_df_user = pd.DataFrame(tweets_list_user, columns=['Datetime','Tweet Id', 'Text', 'Username', 'url'])
#tweets_df_user.to_csv("tweets_users.csv",index=False) # Export to a csv file
#tweets_df_user['Datetime'] = tweets_df_user['Datetime'].astype(str).str[:-6]
#tweets_df_user.to_excel("tweets_users.xlsx",index=False) # Uncomment this line if you prefer an Excel file
#print("Scraped data have been exported to the csv file")