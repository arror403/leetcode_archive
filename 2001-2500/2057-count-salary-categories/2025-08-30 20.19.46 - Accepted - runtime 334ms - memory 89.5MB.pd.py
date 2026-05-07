import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    res=[0, 0, 0]
    for v in accounts['income']:
        if v<20000:
            res[0]+=1
        elif v>50000:
            res[2]+=1
        else:
            res[1]+=1


    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': res
    })