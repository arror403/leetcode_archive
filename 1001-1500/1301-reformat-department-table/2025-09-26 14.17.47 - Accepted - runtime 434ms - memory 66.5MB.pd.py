import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    res = {}
    for p in set(department['id']):
        res[p] = {"Jan_Revenue":pd.NA,"Feb_Revenue":pd.NA,"Mar_Revenue":pd.NA,
                  "Apr_Revenue":pd.NA,"May_Revenue":pd.NA,"Jun_Revenue":pd.NA,
                  "Jul_Revenue":pd.NA,"Aug_Revenue":pd.NA,"Sep_Revenue":pd.NA,
                  "Oct_Revenue":pd.NA,"Nov_Revenue":pd.NA,"Dec_Revenue":pd.NA}
    
    for _,r in department.iterrows(): res[r['id']][r['month']+"_Revenue" ]=r['revenue']
    
    result_data = []
    for id_val, revenues in res.items():
        row = {'id': id_val}
        row.update(revenues)
        result_data.append(row)
    

    return pd.DataFrame(result_data)