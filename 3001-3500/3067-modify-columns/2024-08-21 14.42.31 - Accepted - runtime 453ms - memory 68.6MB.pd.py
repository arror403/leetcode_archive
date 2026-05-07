import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[:, "salary"]=[x*2 for x in employees.loc[:,"salary"]]

    return employees