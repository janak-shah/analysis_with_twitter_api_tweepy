#twitter api 
#pip install tweepy

import tweepy 


#AUTHENTICATION - logging in 

consumer_key = open('twitter_api_key.txt', 'r').read()
consumer_secret = open('twitter_api_secret.txt','r').read()
access_token = open('twitter_access_token.txt','r').read()
access_token_secret = open('twitter_access_token_secret.txt','r').read()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)  #creating an API object 


try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    
    
#basically a tweet is a dictionary 

#ACCESSING TIMELINE TWEETS , PUBLIC TWEETS


# =============================================================================
# public_tweets = api.home_timeline()
# 
# #print(public_tweets)  #this will print a list of tweets (list of dictionaries)
# 
# 
# for tweet in public_tweets:
#     print(tweet.user.screen_name)
#     print(tweet.text)  #accessing through key value pair 
# 
# 
# =============================================================================
##Get the user object for twitter

user = api.get_user(screen_name = "shah_janak")
print(user.name)
print(user.followers_count)

#print(user.friends)

for friend in user.friends():
    print(friend.screen_name)


print(user.id)
print(user.name)
print(user.location)
print(user.url)
print(user.description)
print(user.followers_count)
print(user.friends_count)
print(user.listed_count)
print(user.statuses_count)
print(user.created_at)

#things you can do from your own account
#api.update_status("Good opportunity to buy this dip in cryptocurrencies #Bitcoin #BTC")

#follow someone
#api.create_friendship(screen_name ="priyalajani")

#update your own profile
api.update_profile(description = "Algo Trader,Technical Analyst, Crypto & Economy enthusiast")


#liking a tweet
#api.create_favourite(tweet.id)

#latest tweets with search term 

# =============================================================================
# term = "Bitcoin"
# since = "2021-11-24"  #you can add this keyword too
# 
# 
# for tweet in api.search_tweets(q = term,lang = 'en' ):
#     print(tweet.text)
#     print(tweet.user.name)
#     print(tweet.id)
# #    tweet.user.follow()
# 
# #USING A CURSOR 
# =============================================================================

# =============================================================================
#     
# for tweet in tweepy.Cursor(api.search_tweets,q = term,lang = 'en',since = since, rpp =100).items(100):
#     print(tweet.user.name)
#     print(tweet.text)
#     
# =============================================================================
#finding tmr followers and following them 
# =============================================================================
# user = api.get_user(screen_name = "themoneyroller")
# 
# for follower in user.followers():
#     try:
#         print(follower.screen_name)
#         follower.follow()
#     except Exception as e:
#         print(e)
# 
# =============================================================================

#PRINTING FULL TWEETS

term = "Bitcoin"
since = "2021-11-24"  #you can add this keyword too


for tweet in api.search_tweets(q = term,lang = 'en', since = since, tweet_mode = "extended" ):
    if hasattr(tweet,'retweeted_status'):
        print(tweet.retweeted_status.full_text)
    else:
        print(tweet.full_text)

# STREAMING TWEETS 


class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        print(status.id)
        print(status.text)

#initialize an instance of this subclass

printer = IDPrinter(
  consumer_key, consumer_secret,
  access_token, access_token_secret
)

#filter realtime tweets by keyword
printer.filter(track = ["Bitcoin", "solana"])


