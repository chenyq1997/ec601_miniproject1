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

#Get tweets and print - improved still basic interface, output to txt

searchTerm = input("Enter Keyword/Tag to search about: ")

NoOfTerms = int(input("Enter how many tweets to search: "))

f = open('bike.txt','w')

tweets = tweepy.Cursor(api.search, q = searchTerm, lang = "en", mode = "extended").items(NoOfTerms) 

for t in tweets:

    

    #print(t.text)

    f.write(t.text)