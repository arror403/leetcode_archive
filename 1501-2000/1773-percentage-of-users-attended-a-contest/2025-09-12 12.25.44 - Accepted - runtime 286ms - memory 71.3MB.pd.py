import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    L=len(users['user_id'])
    c=defaultdict(set)

    for a,b in zip(register['contest_id'], register['user_id']): c[a].add(b)

    percent=[len(p)/L*100 for p in c.values()]

    res=pd.DataFrame({'contest_id':c.keys(), 'percentage': percent}).round({'percentage': 2})


    return res.sort_values(['percentage', 'contest_id'], ascending=[False, True])