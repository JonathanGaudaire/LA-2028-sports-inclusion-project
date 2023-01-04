# Final project data cleaning process

# Import libraries
import pandas as pd
import csv
from nltk.corpus import stopwords
import re
import string
from collections import defaultdict
import nltk
nltk.download('stopwords')
stop = stopwords.words('english')


# Import data
surf = pd.read_csv("D:\Documents\Travail\Mcgill\\5- Fall 2022\INSY 448 - Text and social media analytics\Code\Final project\\tweets_surf.csv")

# Remove stop words from sentence
inter1 =surf['Text']
sentences_all = []
sentences_clean = []

# Split the row into different sentences
for row in inter1:
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', row)
    for s in sentences:
        in1 = ''.join(s)
        out = re.sub('[%s]' % re.escape(string.punctuation), '', in1.lower())
        sentences_all.append(out)
        
for sentence in sentences_all:
    s = []
    for i in sentence.split():
        if i not in stop and i.isdigit() is False:
            s.append(i)
    sentences_clean.append(s)

