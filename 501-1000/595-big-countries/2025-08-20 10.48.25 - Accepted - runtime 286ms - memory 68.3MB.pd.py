import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    x,y,z=[],[],[]

    for n,p,a in zip(world['name'], world['population'], world['area']):
        if a>=3000000 or p>=25000000:
            x.append(n)
            y.append(p)
            z.append(a)


    return pd.DataFrame({'name': x, 'population': y, 'area': z})