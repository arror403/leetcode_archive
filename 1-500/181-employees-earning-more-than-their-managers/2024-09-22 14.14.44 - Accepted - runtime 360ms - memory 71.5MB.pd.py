import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Merge employee data with manager data
    df=employee.merge(employee[['id', 'salary']],
                        left_on='managerId',
                        right_on='id',
                        suffixes=('', '_manager'))
    
    # Filter employees who earn more than their manager
    res=df[df['salary']>df['salary_manager']]['name']
    
    
    return pd.DataFrame({"Employee":res})