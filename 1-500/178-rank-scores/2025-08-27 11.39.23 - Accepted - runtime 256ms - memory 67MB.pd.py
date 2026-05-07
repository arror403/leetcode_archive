import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    d=Counter(scores['score'])
    d=sorted(d.items(), key=lambda x:x[0], reverse=True)

    s=chain.from_iterable([[v]*f for v,f in d])
    res=[]

    r=1
    for _,x in d:
        res+=[r]*x
        r+=1


    return pd.DataFrame({
        'score': list(s),
        'rank': res
    })