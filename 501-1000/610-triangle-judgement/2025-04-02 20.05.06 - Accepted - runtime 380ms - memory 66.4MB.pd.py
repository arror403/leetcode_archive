import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle']=triangle.apply(lambda t: 'Yes' if ((t.x+t.y>t.z)&(t.y+t.z>t.x)&(t.x+t.z>t.y)) else 'No', axis=1)

    return triangle