import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(products, id_vars='product_id', var_name='store', value_name='price').dropna()



    # res=pd.DataFrame()


    # for x in products['product_id']:
    #     p = products[products['product_id'] == x].iloc[0]

    #     res.append({
    #         'product_id': x,
    #         'store': 
    #         'price': p['store1']
    #     })



    # return res