import pandas as pd

def find_products(p: pd.DataFrame) -> pd.DataFrame:
    res = p[(p['low_fats']=='Y') & (p['recyclable']=='Y')]
    return res[['product_id']]