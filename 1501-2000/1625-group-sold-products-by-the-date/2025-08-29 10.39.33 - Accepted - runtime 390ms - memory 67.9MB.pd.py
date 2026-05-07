import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    return activities.groupby('sell_date', as_index=False).agg(
                        num_sold=('product', lambda x: len(set(x))),
                        products=('product', lambda x: ','.join(sorted(set(x))))
                        )