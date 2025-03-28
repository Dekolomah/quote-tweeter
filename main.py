import tweepy
import random

# Hardcoded Twitter API credentials
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAEQNxQEAAAAAJayc94AArQmdujffu1oZcJaTHQc%3Dm11RCh2QqqquArqRdMEyKMLEg8nmvUTj8ehfmDd6o8aLwADy0X"
API_KEY = "JoRYIt4dcYciMR9yJLcFkUQ8z"
API_SECRET_KEY = "gXujJkq02RqcO9po6eFehDUPgrdn1FWUuNR0ZbADPeMjUNiBSc"
ACCESS_TOKEN = "1834736136582774784-OdWh1pcHOgIcRYtvQfFeLW0XZ4KYPv"
ACCESS_TOKEN_SECRET = "5ylGG5XwLtptYNRaxfhwOGNwVZmPO9hxYnocpIfUyImlb"

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
