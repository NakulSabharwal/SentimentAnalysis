import csv
import tweepy
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import operator
# Step 1 - Authenticate
consumer_key= 'ffsbeAoOlbji49uLR5xE8ujGi' #CONSUMER_KEY_HERE
consumer_secret= 'bSBzfEXCg0Y7IBTG3zYFFHsZGulupPgXxD0AEuvHYGtcSAFgwq' #CONSUMER_SECRET_HERE

access_token='806827617974251520-iYfFm9LwUAgPInHpb6TkYvpQCw6cQeL' #ACCESS_TOKEN_HERE
access_token_secret='V1UHLzGbXcicJfM5bbt8vxgppm52WmeQhi7KXVTeouk6K' #ACCESS_TOKEN_SECRET_HERE

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
