import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    t=[]

    for i,r in products.iterrows():
        if pd.isna(r['quantity']): # kind weird...
            t.append(0)
        else:
            t.append(r['quantity'])

    products['quantity']=t


    return products


# In [14]: None == None
# Out[14]: True

# In [15]: np.nan == np.nan
# Out[15]: False

# In [16]: pd.NaT == pd.NaT
# Out[16]: False

# In [17]: pd.NA == pd.NA
# Out[17]: <NA>