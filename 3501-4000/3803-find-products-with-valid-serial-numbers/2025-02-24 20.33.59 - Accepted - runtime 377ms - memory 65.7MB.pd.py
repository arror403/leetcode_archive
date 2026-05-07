import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    res=[]
    for ID, name, d in zip(products['product_id'], products['product_name'], products['description']):
        for s in d.split():
            if len(s)<2: 
                continue
            if s[0]=='S' and s[1]=='N':
                f=1
                for x in s[2:].split('-'):
                    if x.isnumeric() and len(x)==4:
                        continue
                    else:
                        f=0
                        break

                if f: res.append([ID, name, d])

    res.sort(key=lambda x:x[0])

    return pd.DataFrame({'product_id':[x[0] for x in res],
                        'product_name':[x[1] for x in res],
                        'description':[x[2] for x in res]})