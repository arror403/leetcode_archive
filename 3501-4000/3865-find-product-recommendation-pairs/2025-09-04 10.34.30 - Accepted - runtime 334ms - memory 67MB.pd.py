import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    p_u=defaultdict(set)
    p_info={}
    res=[]

    for _,r in product_info.iterrows():
        p_info[r['product_id']]=r['category']

    for _,r in product_purchases.iterrows():
        p_u[r['product_id']].add(r['user_id'])
    
    for a,b in combinations(product_info['product_id'], 2):
        c=len(p_u[a]&p_u[b])
        if c>=3:
            if a<b:
                res.append([a, b, p_info[a], p_info[b], c])
            else:
                res.append([b, a, p_info[b], p_info[a], c])

    res.sort(key=lambda x: (-x[4], x[0], x[1]))


    return pd.DataFrame(res, columns=['product1_id', 'product2_id', 'product1_category', 'product2_category', 'customer_count'])