import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    d=defaultdict(set)
    for t,s in zip(teacher.teacher_id, teacher.subject_id): d[t].add(s)

    return pd.DataFrame({"teacher_id":[k for k in d.keys()], "cnt": [len(v) for v in d.values()]})