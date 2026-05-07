import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    a=set(employees['employee_id'])
    b=set(salaries['employee_id'])

    return pd.DataFrame({'employee_id': list(a^b)}).sort_values(by=['employee_id'])