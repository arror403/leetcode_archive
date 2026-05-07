import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    d_even=defaultdict(int)
    d_odd=defaultdict(int)
    t=set()

    for _,r in transactions.iterrows():
        t.add(r['transaction_date'])

        if (a:=r['amount'])%2: 
            d_odd[r['transaction_date']]+=a
        else: 
            d_even[r['transaction_date']]+=a

    res=pd.DataFrame({
        'transaction_date': list(t),
        'odd_sum': [d_odd[x] for x in t],
        'even_sum': [d_even[x] for x in t]
    })


    return res.sort_values(by=['transaction_date'])