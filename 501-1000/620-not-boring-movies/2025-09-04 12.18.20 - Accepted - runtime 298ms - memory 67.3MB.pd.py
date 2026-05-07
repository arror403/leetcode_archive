import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    res=cinema.loc[(cinema['id']%2==1) & (cinema['description'].str.contains('boring', na=False)==False)]

    return res.sort_values(by=['rating'], ascending=False)