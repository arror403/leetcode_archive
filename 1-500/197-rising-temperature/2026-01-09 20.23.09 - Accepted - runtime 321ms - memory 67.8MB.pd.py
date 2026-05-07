import pandas as pd
import numpy as np

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    res=[]

    for a,b in pairwise(zip(weather['id'], weather['temperature'], weather['recordDate'])):
        if (b[2]-a[2])/np.timedelta64(1, 'D')==1:
            if b[1]>a[1]:
                res.append(b[0])


    return pd.DataFrame({'id': res})