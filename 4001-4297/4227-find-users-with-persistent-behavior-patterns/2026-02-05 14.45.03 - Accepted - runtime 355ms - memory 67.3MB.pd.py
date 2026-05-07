import pandas as pd

def find_behaviorally_stable_users(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by='action_date', inplace=True)
    d=defaultdict(list)
    res=[]

    for _,r in activity.iterrows():
        d[str(r['user_id'])+' '+r['action']].append(r['action_date'])

    for k,v in d.items():
        dt=1
        for a,b in pairwise(v):
            if (pd.Timestamp(b)-pd.Timestamp(a))==pd.to_timedelta('1 days 00:00:00'):
                dt+=1
        if dt>=5:
            res.append(k.split()+[dt]+[v[0]]+[v[-1]])

    R=pd.DataFrame({'user_id':[int(x[0]) for x in res]
                ,'action':[x[1] for x in res]
                ,'streak_length':[x[2] for x in res]
                ,'start_date':[x[3] for x in res]
                ,'end_date':[x[4] for x in res]})

    R.sort_values(by=['streak_length','user_id'], ascending=[False,True], inplace=True)

    return R