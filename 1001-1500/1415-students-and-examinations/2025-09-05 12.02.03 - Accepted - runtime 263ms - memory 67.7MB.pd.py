import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    e=defaultdict(list)
    d={}

    for i,n in zip(students['student_id'], students['student_name']): d[i]=n

    for i,s in zip(examinations['student_id'], examinations['subject_name']): e[i].append(s)

    e={k:Counter(v) for k,v in e.items()}

    res=[]
    for k in students['student_id']:
        for s in subjects['subject_name']:
            res.append([k, d[k], s, e.get(k,{}).get(s,0)])
        # for a,b in e[k].items():
            # res.append([k,d[k],a,b])


    return pd.DataFrame(res, columns=['student_id', 'student_name', 'subject_name', 'attended_exams']).sort_values(by=['student_id', 'subject_name'])