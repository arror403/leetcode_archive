import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"tweet_id":tweets[tweets.content.str.len()>15].tweet_id})