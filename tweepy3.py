#twitter api 

#pip install tweepy

import tweepy

#AUTHENTICATION - logging in 
consumer_key = open('twitter_api_key.txt','r').read()
consumer_secret =  open('twitter_api_secret.txt','r').read()
access_token = open('twitter_access_token.txt','r').read()
access_token_secret = open('twitter_access_token_secret.txt','r').read()


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication complete")
except Exception as e:
    print(e)
    print("Error during Authentication")
    
#accessing public tweets - timeline tweets

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
#get the user object from twitter
user = api.get_user(screen_name = 'shah_janak')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)

#getting a users details 
print(user.id)
print(user.name)
print(user.location)
print(user.url)
print(user.description)
print(user.created_at)

#things you can do from your own account 

#write a new tweet 
#api.update_status("The markets have been a rollercoaster ride. Hang in there. Dont fall off")


#follow someone
api.create_friendship(screen_name = "themoneyroller")


#update your own profile
api.update_profile(description = "Algo Trader,Technical Analyst, Crypto, Movie Lover & Economy enthusiast")

#liking a tweet 
#api.create_favorite(tweet.id)


#latest tweet with a search term 
# =============================================================================
# term = "Yoga"
# since = "2021-12-28"
# for tweet in api.search_tweets(q=term,lang ='en',since = since,count =100):
#     print(tweet.user.name)
#     print(tweet.text)
#     tweet_id = tweet.id
#     print(tweet_id)
# #    api.create_favorite(tweet_id)
#     
# =============================================================================

#findint tmr followers and follow them

# =============================================================================
# user = api.get_user(screen_name = "themoneyroller")
# 
# for follower in user.followers():
#     print(follower.screen_name)
#     follower.follow()
#     
# =============================================================================

#USING CURSOR 

#latest tweets with search term using Cursor 
# =============================================================================
# term = "Exercise"
# since = "2021-12-28"
# for tweet in tweepy.Cursor(api.search_tweets,q = 'term',lang = 'en',rpp = 100).items(100):
#     print(tweet.user.name)
#     print(tweet.text)
#     tweet.user.follow()
# # =============================================================================
# #     tweet_id = tweet.id
# #     print(tweet_id)
# #     api.create_favorite(tweet_id)
# # 
# # =============================================================================
# 



# #PRINTING FULL TWEET TEXT 
# =============================================================================

#latest tweet with a search term 
# =============================================================================
# term = "Bitcoin"
# since = "2021-12-28"
# for tweet in api.search_tweets(q=term,lang ='en',since = since,tweet_mode = 'extended',count =100):
#     if hasattr(tweet, 'retweeted_status'):
#         print(tweet.retweeted_status.full_text)
#     else:
#         print(tweet.full_text)
# 
# =============================================================================


#Streaming Tweets
#Subclass Stream to print IDs

class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        print(status.id)
        print(status.text)


printer = IDPrinter(
  consumer_key, consumer_secret,
  access_token, access_token_secret
)

#filter realtime text by keyword
printer.filter(track=["Ratan Tata",])


