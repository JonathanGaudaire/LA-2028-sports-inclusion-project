# Data cleaning process for Olympics datasets

import pandas as pd

df = pd.read_csv("D:\Documents\Travail\Mcgill\\5- Fall 2022\INSY 448 - Text and social media analytics\Code\Final project\\tweets_weightlifting.csv") # adjust file name as needed

df_clean = df[df["language"] == "en"] # change column name to whatever your language column is named

df_clean['Text'] = df_clean['Text'].replace(r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True)
df_clean = df_clean.dropna()
df_clean = df_clean.drop_duplicates(subset=['Text'])

df_clean.to_excel("tweets_weightlifting_clean.xlsx",index=False) # adjust output file name as needed
