import tweepy
import json
import time


# Twitter API Keys
consumer_key = "C8ilzBNCjUI9crRlI69qi3371"
consumer_secret = "OzrK2FFXIZOGLecyQsqBJyf5BWljlO8MUCwwAlHlJQlCxCHjnC"
access_token = "942863847211388933-66b5mL0ozko8DNnwOjR72GLlw6P4DsR"
access_token_secret = "aCOl5jwbTZJ5LkZly94iTahzjgbXVhtDEv5g4d3dwUhQ7"

# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1