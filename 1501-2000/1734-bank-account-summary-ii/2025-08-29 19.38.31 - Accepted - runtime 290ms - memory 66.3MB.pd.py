import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    d_account=defaultdict(int)
    d_name={a:b for a,b in zip(users['account'], users['name'])}

    for a,t in zip(transactions['account'], transactions['amount']): d_account[a]+=t

    res=[[d_name[k], d_account[k]] for k,v in d_account.items() if v>10000]
        

    return pd.DataFrame({
        'NAME': [x[0] for x in res],
        'BALANCE': [x[1] for x in res]
    })