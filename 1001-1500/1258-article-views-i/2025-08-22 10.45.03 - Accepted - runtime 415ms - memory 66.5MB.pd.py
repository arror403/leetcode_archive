import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    s=set()

    for i,r in views.iterrows():
        if r['author_id']==r['viewer_id']:
            s.add(r['author_id'])


    return pd.DataFrame({'id': sorted(s)})