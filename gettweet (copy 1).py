#Copyright 2019 Yanqiu "Sandro" Chen chen1997@bu.edu
#Export tweets using Twitter API
import tweepy

#Keys and Tokens

consumer_key = ''

consumer_secret = ''

access_token = ''

access_secret = ''

#Twitter API Auth
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

#Get tweets and print - rather simplistic now, rewrite regarding next steps

tweets = api.user_timeline(id='kvlly',count=10,tweet_mode="extended")

for t in tweets:

    print(t.full_text)