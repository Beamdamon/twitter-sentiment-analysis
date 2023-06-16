from snscrape.modules import twitter as sntwitter
from textblob import TextBlob
import tkinter as tk
import tkinter.font as TkFont

#This program scrapes tweets from twitter and determines the sentiments of the tweets using the TextBlob sentiment function

maxResults = 100

def scraperSearch(query):

    scraper = sntwitter.TwitterSearchScraper(query)
    tweets = []

    for i, tweet in enumerate(scraper.get_items()):
        tweets.append(tweet.rawContent)
        if i >= maxResults - 1:
            break
    return tweets

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

    #Uses getTweets, setting the query and the count
    tweets = scraperSearch('Reddit')

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

    print('Total Tweets:', maxResults) 
    print('Positive:', positive) 
    print('Negative:', negative) 
    print('Neurtral:', neutral)
    
main()