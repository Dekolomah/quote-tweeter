import os
import tweepy
import random

# Retrieve Twitter API credentials from environment variables
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Authenticate with Twitter API using Tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# List of sample quotes to tweet
quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "In the middle of difficulty lies opportunity. – Albert Einstein",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "The best way to predict the future is to create it. – Peter Drucker"
]

def tweet_quote():
    try:
        # Select a random quote
        quote = random.choice(quotes)
        # Post the tweet
        api.update_status(quote)
        print(f"Successfully tweeted: {quote}")
    except tweepy.TweepyException as e:
        print(f"Error tweeting: {e}")

if __name__ == "__main__":
    # Verify authentication
    try:
        api.verify_credentials()
        print("Authentication successful")
        tweet_quote()
    except tweepy.TweepyException as e:
        print(f"Authentication failed: {e}")
