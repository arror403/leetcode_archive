import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    df = performance_reviews.copy()
    df['review_date'] = pd.to_datetime(df['review_date'])
    
    # Add ranking
    df['rnk'] = df.groupby('employee_id')['review_date'].rank(method='min', ascending=False)
    
    # Keep only top 3 reviews
    df = df[df['rnk'] <= 3]
    
    # Get the three ratings for comparison
    df_wide = df.pivot(index='employee_id', columns='rnk', values='rating')
    
    # Filter for improving employees
    mask = (df_wide[1] > df_wide[2]) & (df_wide[2] > df_wide[3])
    improving = df_wide[mask].copy()
    
    # Calculate improvement score
    improving['improvement_score'] = improving[1] - improving[3]
    
    # Add names and format result
    result = (improving[['improvement_score']]
              .reset_index()
              .merge(employees[['employee_id', 'name']], on='employee_id')
              .sort_values(['improvement_score', 'name'], ascending=[False, True]))
    
    
    return result[['employee_id', 'name', 'improvement_score']]