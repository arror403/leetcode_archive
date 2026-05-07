import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    m=list(customers['email'])
    d=set()
    res=[]

    for i,r in customers.iterrows():
        if r['email'] not in d:
            d.add(r['email'])
            res.append({
                'customer_id': r['customer_id'],
                'name': r['name'],
                'email': r['email']
            })


    return pd.DataFrame(res)