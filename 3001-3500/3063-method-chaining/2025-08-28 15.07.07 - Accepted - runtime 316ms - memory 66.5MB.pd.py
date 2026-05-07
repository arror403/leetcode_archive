import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    t=[]

    for _,r in animals.iterrows():
        if r['weight']>100:
            t.append([r['name'], r['weight']])

    t.sort(key=lambda x: x[1], reverse=True)


    return pd.DataFrame({'name': [x[0] for x in t]})