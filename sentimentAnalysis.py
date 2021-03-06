import csv
import tweepy
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import operator
# Step 1 - Authenticate
consumer_key= '' #CONSUMER_KEY_HERE
consumer_secret= '' #CONSUMER_SECRET_HERE

access_token='' #ACCESS_TOKEN_HERE
access_token_secret='' #ACCESS_TOKEN_SECRET_HERE

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

topic = 'India'

with open('%s.csv'%topic,'wb') as new_file:
	new_file.write('tweet,sentiment\n')
	public_tweets = api.search(topic,count=100)
	for tweet in public_tweets:
	    #print(tweet.text)
	    #Step 4 Perform Sentiment Analysis on Tweets
	    analysis = TextBlob(tweet.text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
	    print(analysis.sentiment)
	    print("")
	    new_file.write('%s,%s\n'%(str(tweet.text.encode('utf8')),str(analysis.sentiment)))
