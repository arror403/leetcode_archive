import pandas as pd

def find_users_with_high_tokens(prompts: pd.DataFrame) -> pd.DataFrame:
    d={}
    for u in prompts['user_id']: d[u]=[0,[]]

    for _,r in prompts.iterrows():
        d[r['user_id']][1].append(r['tokens'])
        d[r['user_id']][0]+=1

    res=[]
    for k,v in d.items():
        if v[0]<3 or len(set(v[1]))==1: continue
        res.append([k, v[0], round(sum(v[1])/v[0], ndigits=2)])

    res.sort(key=lambda x:(-x[2],x[0]))
    res=list(zip(*res))


    return pd.DataFrame({'user_id':     res[0], 
                         'prompt_count':res[1],
                         'avg_tokens':  res[2]})