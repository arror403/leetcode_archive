import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"tweet_id":[i for i,v in zip(tweets.tweet_id, tweets.content) if len(v)>15]})