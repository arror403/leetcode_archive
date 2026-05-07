import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    e=[v for v,f in Counter(employee['employee_id']).items() if f==1]
    d={}

    for _,r in employee.iterrows():
        eid=r['employee_id']
        if eid in e:
            d[eid]=r['department_id']
        if r['primary_flag']=='Y':
            d[eid]=r['department_id']


    return pd.DataFrame({'employee_id':d.keys(), 'department_id':d.values()})