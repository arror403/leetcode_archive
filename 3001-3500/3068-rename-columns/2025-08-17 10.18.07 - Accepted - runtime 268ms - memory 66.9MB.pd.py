import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    res=pd.DataFrame()

    res['student_id']=students['id']
    res['first_name']=students['first']
    res['last_name']=students['last']
    res['age_in_years']=students['age']


    return res