# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:33:06 2019

@author: Patrick Plum

Description: This script creates a wordcloud of the relative appearance of all constituent cryptocurrencies of the CRIX in the time window from 2014/08/01 until 2019/04/01
- called by: CRIXRebalancingMaster.py - pls run the latter
"""

############################### Import Modules #############################################

import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud 
import csv 
from PIL import Image
plt.style.use('ggplot')


####### Wordcloud for relative frequency of appearance of a cryptocurrency in CRIX #######

# make bag of words of CRIX members
file_ob = open('index_members.csv',encoding="utf-8") 
  
# reader object is created 
reader_ob = csv.reader(file_ob) 
  
# contents of reader object is stored . 
# data is stored in list of list format. 
reader_contents = list(reader_ob) 

# initialize text 
text = "" 
  
# iterating through list of rows
for row in reader_contents :
    # iterating through words in the row 
    for word in row : 
        # concatenate the words 
        text = text + " " + word
        
#lowercase all words to exclude redundancies
text = text.upper()

#Image as mask for the wordcloud
wave_mask = np.array(Image.open('Dollar.png'))
#generating the wordcloud
wordcloud = WordCloud(width=800, height=1600, background_color="white",colormap="Accent"
                      , collocations = False, contour_width=3, contour_color='firebrick',mask=wave_mask,
                      relative_scaling=0.2, max_words=2000).generate(text) 
 
# plot WordCloud image  
plt.figure(figsize=(40,40),facecolor = 'white', edgecolor='blue')
plt.imshow(wordcloud,interpolation="bilinear")  
plt.axis("off") 
plt.margins(x=0, y=0)
plt.show() 

wordcloud.to_file("Wordcloud_CRIX_Frequency.png")

#########################################################################################