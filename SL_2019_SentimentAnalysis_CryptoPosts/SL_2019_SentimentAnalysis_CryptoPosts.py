# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:40:11 2019

@author: Anna Pacher, Kathrin Spendier

In the following skript a sentiment analysis is performed.
The text for analysis is taken from: https://cryptocurrencytalk.com,
which is a forum for crypto currencies. 


"""


#!pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))
  
    
  #2013
sentiment_analyzer_scores("BYTECOIN DYING? One of the large pools at http://pool.bytecoin.in  doesn't seem to be working anymore.  I wonder if this is the end of Bytecoin.  I have a couple hundred BTEs so I hope it does go somewhere.  I also read that the exchange went offline or is under repair... I have no idea. The failure of the coin to make it to an exchange considering the fact that it's older then CNC and BTB which both made it to exchanges, makes me wonder.") 

  #2014
sentiment_analyzer_scores("Hi Community. Today is a day that I realized that banks are for themselves, and not for the people. 3 years ago there was a major earthquake in my city where many people died. My family was lucky enough to have survived this disaster with, what we considered, only a small matter for a severally damaged house After all this time we have struggled without insurance to get a pay out to fix our, un-weatherproof, unhealthy house and we finally succeeded! BUT - only to have our bank refuse to release the money to use because they don't believe it is sufficient to repair the damage and want to protect their interest in our property This is why Bitcoin and crypto-currency are the way of the future. It takes the power out of the hands of the big corporation banks and back into the hands of the people!!! If anyone would like to show their support to a fellow Crypto-miner, please click the link and like my post. Social media has already started working, but the more interest shown, the more the bank will work to resolve our problem. Don't forget to mention Bitcoins in any comments to remind banks that their days are numbered Smiley  All we want is a warm dry house this winter the kids deserve it and I don't think we can do another one without walking away from out home. You can start saying fuck the government by saying bye-bye to your friends & stop using facebook.")

  #2015
sentiment_analyzer_scores("Trying to find a place to spend your treasure trove of Bitcoin can be difficult. Many sites claim to accept Bitcoin but in actuality only accept it for certain items. To help you I have assembled a list of websites that provide lists of merchants who accept Bitcoin. I hope that you find this helpful. This is just a short list of websites that I found. As for individual merchants who accept Bitcoin I know that thecryptostore.com accepts Bitcoin for everything and does so so through Bitpay. Definitely checkout these sites, they are very helpful. I believe Newegg.com but I'm not sure? There is a bunch of hosting places which accept Bitcoin. People are waking up and realizing that accepting Bitcoin is a smart move.  I think a lot of business think that they will be shorted if they accept Bitcoin and the price drops.  What they don't realize is that some payment providers let them instantly exchange their BTC for fiat. I am so glad that today I have a list of the options that I can use when trying to make the bitcoin purchases. Sometimes being confined to one source is never good and hence one need to explore and see how the rest of the platforms are doing. I will for sure find time and visit the above market place and see which one will best work out for me especially in this year when everything is expected to grow further.")

  #2016
sentiment_analyzer_scores("Hey Everyone !!! I have about $10,000 that I would like to invest in 2017 on Crypto Currencies. I have looked and researched about different types of Crypto currencies such as bitcoin, LiteCoin etc for a while but I do not know what to invest in. Can someone give me some advice on a smart way to invest $ 10,000 on crypto currencies with the best short term and long term options? How safe/risky is it? What kind of a return could I get? Any good strategies on how to go about doing this? Thanks !!!! That's tough, there are risks with any coin you invest in.   Honestly, if I had 10K to invest, I'd throw it into one of the gambling sites with an invest feature.  The house always makes a nice return.  If you're not looking to keep the coins long-term and you're not a day trader, I'd go down the gambling invest route. As with anything financial / gaming there are risks.  Know your risks and only invest the amount you can lose. Investing in cryptocurrencies is an extremely high risk venture. That is evident in the extreme volatility of most of the coin values relative to the US Dollar. Also many new coins simply disappear from the market as interest fluctuates amongst miners who get on the bandwagon of a new issue, hoping to see their minted coins rise in value, but then abandon it for the next one with apparently more promise. Investing in cryptocurrencies is high risk does offer the potential of high returns, and a good strategy would be to portion investment in the top five coins in ratio to volumes traded, thereby helping to ensure liquidity. But investing in small amounts of a few hundred dollars a week so as to spread volatility of prices over a long period. Pretty much in the way you would invest in a share portfolio. In the end, from an investment point of view, you need to be able to get your money converted back into fiat currencies to spend, so the important value to watch the the cryptocurrency to fiat US Dollar value, or the Euro value. My own preference is to mine an interesting coin, whilst investing about €50 a week in the same coin on the exchanges. Thus helping to sustain the coin in the market.")

  #2017
sentiment_analyzer_scores("Bitcoin - is the future freedom from banks? Is it possible? How do you think? In my opinion bitcoin and cryptocurrency in general will co - exist with todays banks. Why? Simply because it's not that easy to do the switch bearing in mind that banks are multi-billionare structures and they won't allowed something else to replace it easily. Plus you will always have people like my friend :  I can't trust the trustees system, when I lose my keys I lose everything, while with banks I am safe and I know that my money can't be lost... Even my country guarantee some kind of money to me if bank fail , for some people it is just easier to let others, banks, to do all the things for them as hey don't want to think about it. First step would be to replace PayPal and other e-wallets so that cryptocurrency become used on a major scale for online transfers. As for me, it s hard for now to say for sure if bitcoin become a freedom for banks. It have some advantages and disadvantages, but in my opinion, bitcoin will become a real future for over world.")

  #2018
sentiment_analyzer_scores("The previous exchanges report published last month provided a meaningful insight on the boom of crypto exchanges. New exchanges were launched, and the peak in demand for cryptocurrencies during December even lead to users being blocked from signing up. Cryptocurrency exchanges like the rest of the crypto ecosystem have seen their fair share of ups and downs over the past months, and this report aims to help illustrate the bigger picture. The falling average price of Bitcoin and overall bearish response in the market has had a negative impact on the exchanges. Over the course of the big dips in the market, the total trading volume has decreased. Users seem to be spending less time on exchanges per session, and this may be because people invest in a smaller variety of coins or because they are becoming more sophisticated and only investing in particular coins. This data coupled with the fact that more users see fewer coins on each exchange can further add to the observation above. As seen in the table below some of the largest exchanges including Coinbase, Gdax and Bittrex have seen a decrease in traffic growth. Users from the US still account for the majority of traffic on most exchanges. The information presented below is based on both public and private information derived from proprietary tools and used to estimate the analytics of each website. There was a minimal lack of real active data from countries including China, Russia, Turkey, Korea, and Japan (yahoo). Users that connect to exchanges through a VPN connection could have an effect on the accuracy of this data. China’s attempts to entirely ban any type of cryptocurrency trading on domestic and foreign trading sites have had an impact on web traffic from Chinese users. Since the ban of all exchanges between fiat currency and cryptocurrencies in China during September, authorities have not been satisfied with the results of these measures and have since taken further actions to ban all token trades and ICO related activities.")

  #2019
sentiment_analyzer_scores("How do you think cryptocurrency craze will be viewed a 100 years from now? Do you think it will be looked at as an investment bubble or a digital revolution? It depends on us. Crypto market survived some sort of katharsis in 2018, whne the Bitcoin bubble burst. Now is the time to make crypto more known for the rest of the world if we want this idea to survive. Hopefully, there are more and more crypto which are gaining public attention (like, for example, FuturoCoin and its partnership with Formule One team, first in history of cryptocurrencies: https://newsroom.futurocoin.com/lets-start-the-season/) so crypto should soon be familiar for people who don’t hear about it before. I've heard before about that F1 sponsorship deal, cause I was writing and article about cryptoworld - sportsworld sponsorship deals. I've heard that they are planning a fork soon, is this true? I couldn't find any official info anywhere. Anyway when it comes to such predicitons it's really difficult to guess, but i want to play that game. I say that 100 years forward, cryptocurrencies are going to be looked as an old, but revolutionary mean of payment, that started a different chapter in economy of our world. I imagine that people (if they are going to be alive as a civilization) will also see cryptocurrencies as a scam - by that I mean something like very unstable, very risky. Well in the current situation I can say that blockchain will survive for sure, it is a really useful technology and probably one of the best right now. But cryptocurrencies seem to lose their position, there are need changes, now crypto is not that trustworthy")


# plot the scores over time

import matplotlib as mlp
import matplotlib.pyplot as plt

year = [i for i in range(2013,2020)]
negativ =[0.084, 0.101, 0.035, 0.057, 0.073, 0.07, 0.074]
neutral = [0.872, 0.727, 0.735, 0.755, 0.825, 0.866, 0.803]
positiv = [0.045, 0.172, 0.23, 0.188, 0.102, 0.063, 0.123]
compound = [-0.3091, 0.9624, 0.9954, 0.9962, 0.7707, -0.5451, 0.9121]


# label for x-axis
plt.xlabel('Years')

# Label for y-axis
plt.ylabel('Scores')

# set ranges for axes manually
# Syntax: plt.axis([xmin, xmax, ymin, ymax])
plt.axis([2013, 2019, -1, 1.2])

# plot the different lines:
plt.plot(year, negativ, linestyle = '-', color='red', label = "negativ")
plt.plot(year, neutral,linestyle = '-', color='blue', label = "neutral")
plt.plot(year, positiv,linestyle = '-', color='green', label = "positiv")
plt.plot(year, compound,linestyle = '-', color='orange', label = "compound")


#show legend
plt.legend(loc = "center left", frameon=True, bbox_to_anchor=(1, 0.5))

# show grid
plt.grid(True)

# add title
plt.title("Sentiment Analysis", fontsize = 18)

# save diagram
plt.savefig("sentimentanalysis_linegraph.png", dpi = 100, bbox_inches='tight')

# Diagramm anzeigen:
plt.show()
