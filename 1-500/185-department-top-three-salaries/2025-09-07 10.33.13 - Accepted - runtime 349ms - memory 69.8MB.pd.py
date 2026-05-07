import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge employee and department data
    merged_df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    
    # Rank salaries within each department (descending order)
    merged_df['salary_rank'] = merged_df.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    
    # Filter top 3 salaries per department
    res = merged_df[merged_df['salary_rank'] <= 3]
    
    # Select and rename columns to match SQL output
    return res[['name_dept', 'name_emp', 'salary']].rename(columns={
        'name_dept': 'department',
        'name_emp': 'employee', 
        'salary': 'Salary'
    })
    
    # return res