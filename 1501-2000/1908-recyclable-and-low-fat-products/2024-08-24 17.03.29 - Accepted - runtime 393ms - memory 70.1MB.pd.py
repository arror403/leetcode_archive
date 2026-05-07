import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "product_id": [r['product_id'] for _,r in products.iterrows() 
                       if r['low_fats']=='Y' and r['recyclable']=='Y'] })