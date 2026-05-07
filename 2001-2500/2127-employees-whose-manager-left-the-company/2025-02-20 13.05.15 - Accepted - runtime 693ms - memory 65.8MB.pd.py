import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    employee_ids = set(employees['employee_id'])
    
    res = []
    for eid, mid, s in zip(employees['employee_id'], employees['manager_id'], employees['salary']):
        if s < 30000:
            # Only include if manager_id is not null AND manager_id doesn't exist as an employee_id
            if not pd.isna(mid) and mid not in employee_ids:
                res.append(eid)
                
    return pd.DataFrame({'employee_id': sorted(res)})