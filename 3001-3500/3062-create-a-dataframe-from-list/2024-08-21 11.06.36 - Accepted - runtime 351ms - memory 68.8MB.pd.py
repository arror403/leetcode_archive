import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    d={"student_id" :(s[0] for s in student_data), "age": (s[1] for s in student_data)}
    return pd.DataFrame(d)