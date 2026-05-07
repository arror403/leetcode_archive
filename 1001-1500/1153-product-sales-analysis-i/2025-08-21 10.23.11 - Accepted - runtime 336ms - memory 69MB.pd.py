import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    d={i:v for i,v in zip(product['product_id'], product['product_name'])}

    res=pd.DataFrame({
        'product_name': [d[x] for x in list(sales['product_id'])],
        'year': sales['year'],
        'price': sales['price']
    })

    return res