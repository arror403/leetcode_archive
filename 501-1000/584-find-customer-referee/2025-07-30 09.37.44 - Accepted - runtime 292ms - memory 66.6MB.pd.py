import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    res=[]

    for n,i in zip(customer['name'], customer['referee_id']):
        if ((i is pd.NA) or (i!=2)):
            res.append(n)


    return pd.DataFrame({"name":res})