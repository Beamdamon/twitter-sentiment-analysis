from snscrape.modules import twitter as sntwitter
from textblob import TextBlob
import tkinter as tk
import tkinter.font as TkFont

#This program scrapes tweets from twitter and determines the sentiments of the tweets using the TextBlob sentiment function

maxResults = 100

#Scrapes twitter using scscrape twitter, adds the tweet content to the tweets array.
def scraperSearch(query):

    scraper = sntwitter.TwitterSearchScraper(query)
    tweets = []

    for i, tweet in enumerate(scraper.get_items()):
        tweets.append(tweet.rawContent)
        if i >= maxResults - 1:
            break
    return tweets

#Sentiment analysis of tweets using TextBlob
def sentimentAnalysis(tweet):
    analyzedTweet = TextBlob(tweet)
    if analyzedTweet.sentiment.polarity > 0:
        return 'positive'
    if analyzedTweet.sentiment.polarity < 0:
        return 'negative'
    if analyzedTweet.sentiment.polarity == 0:
        return 'neutral'

def main():
    #Tweet sentiment counter
    positive = 0
    negative = 0
    neutral = 0

    #Uses scraperSearch, setting the query
    tweets = scraperSearch('Reddit')

    #Goes through each tweet in tweets array, determines sentiment, and upticks the counter accordingly. Then prints the tweet and its sentiment.
    for tweet in tweets:
        sentiment = sentimentAnalysis(tweet)
        if sentiment == 'positive':
            positive += 1
        if sentiment == 'negative':
            negative += 1
        if sentiment == 'neutral':
            neutral += 1

        print(tweet)
        print('Sentiment:', sentiment)
        print("")

    #Prints the total tweets, positive tweets, negative tweets, and neutral tweets
    print('Total Tweets:', maxResults) 
    print('Positive:', positive) 
    print('Negative:', negative) 
    print('Neurtral:', neutral)
    
main()