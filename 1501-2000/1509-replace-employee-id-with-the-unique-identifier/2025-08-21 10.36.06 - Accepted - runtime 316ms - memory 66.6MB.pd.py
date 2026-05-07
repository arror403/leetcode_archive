import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    d={i:v for i,v in zip(employee_uni['id'], employee_uni['unique_id'])}

    t=[]
    for i in employees['id']:
        if i not in d:
            t.append(None)
        else:
            t.append(d[i])


    return pd.DataFrame({'unique_id': t, 'name': employees['name']})