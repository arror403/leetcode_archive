import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks.sort_values('operation_day')

    d=defaultdict(int)

    for i,r in stocks.iterrows():
        if r['operation']=='Buy':
            d[r['stock_name']]-=r['price']
        else:
            d[r['stock_name']]+=r['price']

    res=pd.DataFrame({
        'stock_name': d.keys(),
        'capital_gain_loss': d.values()
    })


    return res