import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue=queue.sort_values('turn')

    w=list(accumulate(queue['weight']))

    t=next((i-1 for i,v in enumerate(w) if v>1000), len(w)-1)


    return pd.DataFrame({'person_name': [queue.iloc[t]['person_name']]})