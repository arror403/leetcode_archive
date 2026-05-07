import pandas as pd

def find_category_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
 
    # Create mapping from product_id to category
    product_to_category = {}
    for _, r in product_info.iterrows():
        product_to_category[r['product_id']] = r['category']
    
    # Group users by category
    category_users = defaultdict(set)
    for _, r in product_purchases.iterrows():
        category = product_to_category[r['product_id']]
        category_users[category].add(r['user_id'])
    
    # Find pairs of categories with at least 3 common users
    res = []
    for cat_a, cat_b in combinations(category_users.keys(), 2):
        common_users = len(category_users[cat_a] & category_users[cat_b])
        if common_users >= 3:
            # Ensure category1 < category2 for consistent ordering
            if cat_a < cat_b:
                res.append([cat_a, cat_b, common_users])
            else:
                res.append([cat_b, cat_a, common_users])
    
    # Sort by customer_count (descending), then category1 and category2 (ascending)
    res.sort(key=lambda x: (-x[2], x[0], x[1]))
    
    
    # Create DataFrame with proper column names
    return pd.DataFrame(res, columns=['category1', 'category2', 'customer_count'])