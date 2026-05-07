import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    m=-inf

    for v,f in Counter(my_numbers['num']).items():
        if f==1:
            m=max(m, v)


    return pd.DataFrame({'num': [m]}) if m!=-inf else pd.DataFrame({'num': [pd.NA]})