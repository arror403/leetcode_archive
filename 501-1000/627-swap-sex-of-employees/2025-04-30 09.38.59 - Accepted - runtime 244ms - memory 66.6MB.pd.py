import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    t=[]
    for s in salary["sex"]: t+=["f"] if s=="m" else ["m"]
    salary["sex"]=t


    return salary