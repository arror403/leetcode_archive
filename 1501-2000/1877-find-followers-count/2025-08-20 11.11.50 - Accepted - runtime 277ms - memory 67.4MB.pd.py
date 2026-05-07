import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    d=defaultdict(set)

    for u,f in zip(followers['user_id'], followers['follower_id']): d[u].add(f)

    res=pd.DataFrame({'user_id': d.keys(), 'followers_count': [len(v) for v in d.values()]})


    return res.sort_values('user_id')