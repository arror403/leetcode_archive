import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    res=[]
    d=defaultdict(list)
    # p=set(person['personId'])&set(address['personId'])

    for _,r in person.iterrows(): d[r['personId']]+=[r['lastName'], r['firstName']]

    # for t in p:
    #     if t in address['personId']:
    #         res.append([d[t][1], d[t][0], ra['city'], ra['state']])
    #     else:
    #         res.append([d[t][1], d[t][0], None, None])

    for rp in person['personId']:
        f=1
        for _,ra in address.iterrows():
            if rp==ra['personId']:
                f=0
                res.append([d[rp][1], d[rp][0], ra['city'], ra['state']])
        if f:
            res.append([d[rp][1], d[rp][0], None, None])


    return pd.DataFrame({
        'firstName': [x[0] for x in res],
        'lastName': [x[1] for x in res],
        'city': [x[2] for x in res],
        'state': [x[3] for x in res]
    })