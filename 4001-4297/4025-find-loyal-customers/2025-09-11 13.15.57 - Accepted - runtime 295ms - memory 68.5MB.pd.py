import pandas as pd

def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    
    df = customer_transactions.copy()
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    
    # Create binary columns for purchases and refunds
    df['is_purchase'] = (df['transaction_type'] == 'purchase').astype(int)
    df['is_refund'] = (df['transaction_type'] == 'refund').astype(int)
    
    # Group and aggregate everything at once
    agg_dict = {
        'is_purchase': 'sum',
        'is_refund': 'sum', 
        'transaction_date': ['min', 'max']
    }
    
    customer_stats = df.groupby('customer_id').agg(agg_dict)
    customer_stats.columns = ['purchase_count', 'refund_count', 'first_date', 'last_date']
    
    # Vectorized calculations
    duration_days = (customer_stats['last_date'] - customer_stats['first_date']).dt.total_seconds() / 86400
    total_transactions = customer_stats['purchase_count'] + customer_stats['refund_count']
    refund_ratio = customer_stats['refund_count'] / total_transactions
    
    # Apply all filters at once
    loyal_mask = (
        (duration_days >= 30) & 
        (refund_ratio < 0.2) & 
        (customer_stats['purchase_count'] >= 3)
    )
    
    loyal_customers = customer_stats[loyal_mask].index.tolist()
    return pd.DataFrame({'customer_id': sorted(loyal_customers)})