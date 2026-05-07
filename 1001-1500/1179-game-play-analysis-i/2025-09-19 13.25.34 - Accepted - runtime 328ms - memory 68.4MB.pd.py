import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by=['event_date'], inplace=True)
    res=activity.groupby('player_id')['event_date'].min().reset_index()


    return res.rename(columns={'event_date': 'first_login'})