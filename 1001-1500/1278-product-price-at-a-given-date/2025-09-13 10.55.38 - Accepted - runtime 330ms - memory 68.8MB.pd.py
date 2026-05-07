import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    target_date = '2019-08-16'
    
    # Convert change_date to datetime if it's not already
    df = products.copy()
    df['change_date'] = pd.to_datetime(df['change_date'])
    target_dt = pd.to_datetime(target_date)
    
    # Filter records on or before target date
    valid_changes = df[df['change_date'] <= target_dt]
    
    # Get the latest price for each product (last record chronologically)
    latest_prices = (valid_changes
                    .sort_values('change_date')
                    .groupby('product_id')
                    .last()
                    .reset_index()[['product_id', 'new_price']])
    
    # Get all unique product IDs
    all_products = pd.DataFrame({'product_id': df['product_id'].unique()})
    
    # Merge and fill missing prices with 10
    result = (all_products
             .merge(latest_prices, on='product_id', how='left')
             .fillna(10)
             .rename(columns={'new_price': 'price'}))
    
    return result[['product_id', 'price']]