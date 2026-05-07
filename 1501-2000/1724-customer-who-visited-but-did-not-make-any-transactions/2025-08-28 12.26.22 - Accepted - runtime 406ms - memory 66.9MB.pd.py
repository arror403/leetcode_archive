import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    t=set(transactions['visit_id'])
    d=defaultdict(int)

    for _,r in visits.iterrows():
        if r['visit_id'] not in t:
            d[r['customer_id']]+=1


    return pd.DataFrame({
        'customer_id': d.keys(),
        'count_no_trans': d.values()
    })