import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    res=cinema.query("id % 2 == 1 and not description.str.contains('boring', na=False)")
    
    return res.sort_values(by=['rating'], ascending=False)