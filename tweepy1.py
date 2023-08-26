#twitter api
import tweepy




#AUTHENTICATION - logging in 

consumer_key =  open('twitter_api_key.txt','r').read()
consumer_secret =  open('twitter_api_secret.txt','r').read()
access_token = open('twitter_access_token.txt','r').read()
access_token_secret = open('twitter_access_token_secret.txt','r').read()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api = tweepy.API(auth,wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#accessing public tweets - timeline tweets


public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
# Get the User object for twitter...
user = api.get_user(screen_name='shah_janak')

print(user.screen_name)
print(user.followers_count)


for friend in user.friends():
   print(friend.screen_name)
   
#user model 

#getting a user details

user = api.get_user(screen_name='themoneyroller')
print(user.id)
print(user.name)
print(user.screen_name)
print(user.location)
#print(user.derived)
print(user.url)
print(user.description)
print(user.protected)
print(user.verified)
print(user.followers_count)
print(user.friends_count)
print(user.listed_count)
print(user.statuses_count)
print(user.created_at)


# =============================================================================
# 
# a = api.get_lists()
# print(a)
# 
#
# =============================================================================
# =============================================================================
# 
# a = api.available_trends()
# print(a)
# 
# =============================================================================

#things you can do from your own account 

#write a new tweet
api.update_status("some text")

#follow someone
api.create_friendship(screen_name ="themoneyroller")

#update your own profile
api.update_profile(description = "Algo Trader,Technical Analyst & Economy enthusiast")


#liking a tweet

api.create_favourite(tweet.id)


#latest tweets with searchterm
term = "Mumbai"
since = "2021-11-13" #you can add this keyword too
for tweet in api.search_tweets(q = term,lang ='en',rpp = 1, since = since):
    print(tweet.user.name)
    print(tweet.text)
    tweet.user.follow()  #follow the user
    tweet.favourite()   #like the tweet

#similarly you can follow all those people who have tweeted something by taking their id

#USING A CURSOR 

for tweet in tweepy.Cursor(api.search_tweets,q = term,lang ='en',rpp=100).items(100):
    print(tweet.user.name)
    print(tweet.text)
    tweet.user.follow()  #follow the user
    tweet.favourite()   #like the tweet


#finding tmr followers and following them

user = api.get_user(screen_name='themoneyroller')

for follower in user.followers():
    print(follower.screen_name)
    follower.follow()


    
#PRINTING FULL TWEETS

#latest tweets with searchterm
term = "Mumbai"
since = "2021-11-13" #you can add this keyword too
for tweet in api.search_tweets(q = term,lang ='en',rpp = 10,tweet_mode = "extended", since = since):
    if hasattr(tweet,'retweeted_status'):
        print(tweet.retweeted_status.full_text)
    else:
        print(tweet.full_text)
        

#Streaming tweets
#Subclass Stream to print IDs of Tweets received
class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        print(status.id)
        print(status.text)

# Initialize instance of the subclass
printer = IDPrinter(
  consumer_key, consumer_secret,
  access_token, access_token_secret
)

# Filter realtime Tweets by keyword
printer.filter(track=["Mumbai"])

