# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:34:12 2019

@author: Anna Pacher, Kathrin Spendier
"""

# importing the necessery modules 

from wordcloud import WordCloud
import matplotlib.pyplot as plt 
import csv
import os
from os import path
from PIL import Image
import numpy as np
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

# Please change the working directory to your path!
root_path = os.getcwd()

#import english stopwords (these are words that will be excluded from the wordcloud,
#for instance articles and prepositions)
stopwords = stopwords.words('english')



# file object is created 

file_ob = open(path.join(root_path, 'cryptocurrencies_wordcloud.txt'), encoding='utf-8') 

  
# reader object is created 
reader_ob = csv.reader(file_ob) 
  
# contents of reader object is stored . 
# data is stored in list of list format. 
reader_contents = list(reader_ob) 
  
# empty string is declare 
text = "" 
  
# iterating through list of rows 
for row in reader_contents : 
      
    # iterating through words in the row 
    for word in row : 
  
        # concatenate the words 
        text = text + " " + word 
 
    
# Mask
star = np.array(Image.open(path.join(root_path, "star.jpeg")))

 


#########################################
# remove stopwords from WordCloud,  show  200 words in the wordcloud . 
wordcloud = WordCloud(width=480, height=480, max_words=200,
            stopwords=stopwords,
            mask= star,
           mode='RGBA',background_color=None ).generate(text) 
  
# plot the WordCloud image  
plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.show() 

# store to file
wordcloud.to_file("bitcoin_wordcloud.png")
