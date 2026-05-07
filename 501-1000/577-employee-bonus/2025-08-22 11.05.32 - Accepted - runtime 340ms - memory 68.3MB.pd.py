import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Merge Employee and Bonus tables using a left join
    res = pd.merge(employee, bonus, on='empId', how='left')

    # Filter rows where bonus is less than 1000 or missing
    res = res[(res['bonus'] < 1000) | res['bonus'].isnull()]

    # Select "name" and "bonus" columns
    res = res[['name', 'bonus']]


    return res