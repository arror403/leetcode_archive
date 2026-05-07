import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    t=date.fromisoformat('2019-08-16')
    d=defaultdict(int)

    products.sort_values(by=['change_date'], inplace=True)

    for _,r in products.iterrows():
        if date.fromisoformat(str(r['change_date'])[:10])>t: break
        d[r['product_id']]=r['new_price']

    for k in (set(products['product_id'])-set(d.keys())): d[k]=10


    return pd.DataFrame({'product_id': d.keys(), 'price': d.values()})