import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name']=[x[0].upper()+x[1:].lower() for x in users['name']]
        
    return users.sort_values(by=['user_id'])