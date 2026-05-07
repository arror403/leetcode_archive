import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    d=defaultdict(set)

    for _,r in activities.iterrows(): d[r['sell_date']].add(r['product'])

    res=pd.DataFrame({
        'sell_date': d.keys(),
        'num_sold': [len(x) for x in d.values()],
        'products': [','.join(sorted(list(x))) for x in d.values()]
    })


    return res.sort_values(by=['sell_date'])