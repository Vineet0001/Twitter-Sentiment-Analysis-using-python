import re
import tweepy
from textblob import TextBlob

class TwitterClient(object):
    def __init__(self):
        bearer_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        self.client = tweepy.Client(bearer_token=bearer_token)

    def clean_tweet(self, tweet):
        return ' '.join(re.sub(r"(@[A-Za-z0-9_]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, max_results=10):
        try:
            tweets = self.client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=["text"])
            return [{"text": tweet.text, "sentiment": self.get_tweet_sentiment(tweet.text)} for tweet in tweets.data]
        except tweepy.TweepyException as e:
            print("Error:", str(e))
            return []

def main():
    api = TwitterClient()
    tweets = api.get_tweets(query='Donald Trump', max_results=10)
    if tweets:
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        print(f"Positive tweets percentage: {100 * len(ptweets) / len(tweets):.2f} %")
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        print(f"Negative tweets percentage: {100 * len(ntweets) / len(tweets):.2f} %")
        print(f"Neutral tweets percentage: {100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets):.2f} %")

        print("\n\nPositive tweets:")
        for tweet in ptweets[:10]:
            print(tweet['text'])

        print("\n\nNegative tweets:")
        for tweet in ntweets[:10]:
            print(tweet['text'])
    else:
        print("No tweets found or access error.")

if __name__ == "__main__":
    main()
