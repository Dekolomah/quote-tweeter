import tweepy
import json
import os

# API credentials
bearer_token = "AAAAAAAAAAAAAAAAAAAAAEQNxQEAAAAAJayc94AArQmdujffu1oZcJaTHQc%3Dm11RCh2QqqquArqRdMEyKMLEg8nmvUTj8ehfmDd6o8aLwADy0X"
api_key = "JoRYIt4dcYciMR9yJLcFkUQ8z"
api_secret_key = "gXujJkq02RqcO9po6eFehDUPgrdn1FWUuNR0ZbADPeMjUNiBSc"
access_token = "1834736136582774784-OdWh1pcHOgIcRYtvQfFeLW0XZ4KYPv"
access_token_secret = "5ylGG5XwLtptYNRaxfhwOGNwVZmPO9hxYnocpIfUyImlb"

# Initialize Tweepy Client
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret_key,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# List of quotes
quotes = [
    "If your dreams don't scare you, they're not big enough.",
    "Love yourself first, because you'll be with you forever.",
    "In a world where you can be anything, be kind.",
    "Every day may not be good, but there's good in every day.",
    "In silence, we hear our loudest thoughts.",
    "We're all stardust, so aim for the stars.",
    "Are you brave enough to see beauty in chaos, divinity in the abyss?",
    "Words have power. Use them wisely or they'll control you.",
    "The opposite of love is not hate, it's indifference.",
    "If you could time travel, which moment would you revisit?",
    "The best camera is your memory.",
    "Only for today, I will smile...",
    "Who am I? A question I often ask myself.",
    "The most beautiful things are felt, not seen or touched.",
    "True friends are those who find common ground.",
    "All you need sometimes is tea and a good book.",
    "To get the universe, think vibes, not just facts.",
    "Strengths and weaknesses, two sides of the same coin.",
    "Nothing beats seeing your ideas become reality.",
    "Your character speaks louder than your wealth or status.",
    "True faith is wishing others well as you do yourself.",
    "Speak positivity or silence is golden.",
    "Patience is key in pain and desire alike.",
    "Real wealth is being content with what you have.",
    "Treat others how you want to be treated"
]

# Remove any leading or trailing whitespace and quotes from each quote
quotes = [quote.strip('"\n ') for quote in quotes]

# File to store the current index
INDEX_FILE = "quote_index.json"

# Load the current index from file, or start at 0
def load_index():
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'r') as f:
            data = json.load(f)
            return data.get("index", 0)
    return 0

# Save the current index to file
def save_index(index):
    with open(INDEX_FILE, 'w') as f:
        json.dump({"index": index}, f)

# Main logic
if __name__ == "__main__":
    try:
        # Load the current index
        index = load_index()

        # Reset index if it exceeds the number of quotes
        if index >= len(quotes):
            index = 0

        # Post the tweet
        tweet = client.create_tweet(text=quotes[index])
        print(f"Tweet '{quotes[index]}' posted successfully. ID: {tweet.data['id']}")

        # Increment the index and save it
        index = (index + 1) % len(quotes)
        save_index(index)

    except Exception as e:
        print(f"Error posting tweet: {e}")
