import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    t = list(seat['student'])

    for i in range(0, len(t) - 1, 2): t[i], t[i+1] = t[i+1], t[i]

    seat['student'] = t


    return seat.sort_values(['id'])