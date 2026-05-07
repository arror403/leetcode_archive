import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    d={}

    for _,r in transactions.iterrows():
        c='null' if pd.isna(r['country']) else r['country']

        t=str(r['trans_date'].year)+'-'+str(r['trans_date'].month).zfill(2)+c

        if t not in d:
            if c=='null':
                d[t]=[t[:7], pd.NA, 0, 0, 0, 0]
            else:
                d[t]=[t[:7], c, 0, 0, 0, 0]

        d[t][2]+=1

        d[t][4]+=r['amount']

        if r['state']=='approved':
            d[t][3]+=1
            d[t][5]+=r['amount']


    return pd.DataFrame(d.values(), columns=['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount'])