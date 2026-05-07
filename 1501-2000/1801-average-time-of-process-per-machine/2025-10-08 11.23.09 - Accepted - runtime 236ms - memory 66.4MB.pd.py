import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    d={}
    res=defaultdict(list)

    for i in set(activity['machine_id']):
        for j in set(activity['process_id']):
            d[(i,j)]=-1

    for _,r in activity.iterrows():
        t=-r['timestamp'] if r['activity_type']=='start' else r['timestamp']
        if d[(r['machine_id'], r['process_id'])]==-1:
            d[(r['machine_id'], r['process_id'])]=t
        else:
            d[(r['machine_id'], r['process_id'])]+=t

    # print(d)
    for k,v in d.items(): 
        if v==-1: continue
        res[k[0]].append(v)


    return pd.DataFrame({'machine_id': res.keys(),
                         'processing_time': [round(sum(x)/len(x), ndigits=3) for x in res.values()]})