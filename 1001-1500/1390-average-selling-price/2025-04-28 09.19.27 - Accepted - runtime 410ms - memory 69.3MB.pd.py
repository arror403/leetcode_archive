import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    
    # Merge the dataframes based on product_id
    merged_df = pd.merge(prices, units_sold, on='product_id', how='left')

    # Filter only the rows where purchase_date is between start_date and end_date
    valid_purchases = merged_df[(merged_df['purchase_date'] >= merged_df['start_date']) & 
                            (merged_df['purchase_date'] <= merged_df['end_date'])]

    # Calculate unit_price (units * price) for valid purchases
    valid_purchases['unit_price'] = valid_purchases['units'] * valid_purchases['price']

    # Group by product_id and calculate average price
    result = valid_purchases.groupby('product_id').agg(
        total_price=('unit_price', 'sum'),
        total_units=('units', 'sum')
    ).reset_index()

    # Calculate average_price
    result['average_price'] = result['total_price'] / result['total_units']
    result['average_price'] = result['average_price'].round(2)

    # Handle products with no sales (IFNULL equivalent)
    all_products = prices['product_id'].unique()
    final_result = pd.DataFrame({'product_id': all_products})

    final_result = pd.merge(final_result, result[['product_id', 'average_price']], on='product_id', how='left')
    final_result['average_price'] = final_result['average_price'].fillna(0)

    # Select only the required columns
    final_result = final_result[['product_id', 'average_price']]


    return final_result