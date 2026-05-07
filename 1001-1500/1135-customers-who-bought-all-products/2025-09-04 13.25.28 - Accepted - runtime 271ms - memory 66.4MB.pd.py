import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    d=defaultdict(set)
    ap=set(product['product_key'])

    for c,p in zip(customer['customer_id'], customer['product_key']): d[c].add(p)

    
    return pd.DataFrame({'customer_id': [k for k,v in d.items() if v==ap]})