# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:19:15 2019

@author: Anna Pacher, Kathrin Spendier

In the following script the two packages textblob and vader are analyzed.
Both packages are used for sentiment analysis.
"""



from textblob import TextBlob
# you may need to install textblob with
# !pip install textblob 
analysis = TextBlob("Bitcoins are super cool")
analysis.sentiment
#Out[1]: Sentiment(polarity=0.3416666666666667, subjectivity=0.6583333333333333)

analysis1 = TextBlob("Bitcoins are super cool!!!")
analysis1.sentiment
#Out[2]: Sentiment(polarity=0.5084635416666666, subjectivity=0.6583333333333333)
# ! improves the polarity rate

analysis2 = TextBlob("Bitcoins are super cool :) !!!")
analysis2.sentiment
#Out[3]: Sentiment(polarity=0.5532986111111111, subjectivity=0.7722222222222221)
# :) improves the polarity rate

analysis3 = TextBlob("Bitcoins are SUPER COOL !!!")
analysis3.sentiment
#Out[4]: Sentiment(polarity=0.5084635416666666, subjectivity=0.6583333333333333)
# upper case letters make no difference

#For German texts this package does not work:
analysis4 = TextBlob("Bitcoins sind nicht super")
analysis4.sentiment
#Out[4]: Sentiment(polarity=0.3333333333333333, subjectivity=0.6666666666666666)

#Does not interpret slang words:
analysis5 = TextBlob("Bitcoin sux")
analysis5.sentiment
#Out[5]: Sentiment(polarity=0.0, subjectivity=0.0)

analysis6 = TextBlob("Bitcoin kinda sux")
analysis6.sentiment
#Out[6]: Sentiment(polarity=0.0, subjectivity=0.0)

#Emojis are not implemented:
analysis7 = TextBlob("Bitcoins make me 😊")
analysis7.sentiment
#Out[7]: Sentiment(polarity=0.0, subjectivity=0.0)

analysis8 = TextBlob("Bitcoins make me 😭")
analysis8.sentiment
#Out[8]: Sentiment(polarity=0.0, subjectivity=0.0)

#Some acronyms are recognized:

analysis9 = TextBlob("LOL")
analysis9.sentiment
#Out[9]: Sentiment(polarity=0.8, subjectivity=0.7)

analysis10 = TextBlob("XOXO")
analysis10.sentiment
#Out[10]: Sentiment(polarity=0.0, subjectivity=0.0)

#####################################################################

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# you may need to install vaderSentiment with
# !pip install vaderSentiment 
analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))

sentiment_analyzer_scores("Bitcoins are super cool")
#Bitcoins are super cool----------------- {'neg': 0.0, 'neu': 0.244, 'pos': 0.756, 'compound': 0.7351}

sentiment_analyzer_scores("Bitcoins are super cool!!!")
#Bitcoins are super cool!!!-------------- {'neg': 0.0, 'neu': 0.22, 'pos': 0.78, 'compound': 0.795}
# ! improves the sentiment score

sentiment_analyzer_scores("Bitcoins are super cool :) !!!")
#Bitcoins are super cool :) !!!---------- {'neg': 0.0, 'neu': 0.229, 'pos': 0.771, 'compound': 0.8772}
# :) & ! leads to a very high compound score


sentiment_analyzer_scores("Bitcoins are SUPER COOL!!!")
#Bitcoins are SUPER COOL!!!-------------- {'neg': 0.0, 'neu': 0.19, 'pos': 0.81, 'compound': 0.8605}
# capital letters improve the sentiment score

#For German texts this packages does not work:
sentiment_analyzer_scores("Bitcoins sind nicht super")
#Bitcoins sind nicht super--------------- {'neg': 0.0, 'neu': 0.435, 'pos': 0.565, 'compound': 0.5994}

#Successfully interprets slang words:
sentiment_analyzer_scores("Bitcoin sux")
#Bitcoin sux----------------------------- {'neg': 0.714, 'neu': 0.286, 'pos': 0.0, 'compound': -0.3612}

sentiment_analyzer_scores("Bitcoin kinda sux")
#Bitcoin kinda sux----------------------- {'neg': 0.525, 'neu': 0.475, 'pos': 0.0, 'compound': -0.2975}

#Emojis are implemented (recognizes UTF-8 encoded emojis)

sentiment_analyzer_scores("Bitcoins make me 😊")
#Bitcoins make me 😊---------------------- {'neg': 0.0, 'neu': 0.5, 'pos': 0.5, 'compound': 0.7184}

sentiment_analyzer_scores("Bitcoins make me 😭")
#Bitcoins make me 😭---------------------- {'neg': 0.383, 'neu': 0.617, 'pos': 0.0, 'compound': -0.4767}

#Acronyms are recognized:

sentiment_analyzer_scores("LOL") 
#LOL------------------------------------- {'neg': 0.0, 'neu': 0.0, 'pos': 1.0, 'compound': 0.4215}

sentiment_analyzer_scores("XOXO")
#XOXO------------------------------------ {'neg': 0.0, 'neu': 0.0, 'pos': 1.0, 'compound': 0.6124
