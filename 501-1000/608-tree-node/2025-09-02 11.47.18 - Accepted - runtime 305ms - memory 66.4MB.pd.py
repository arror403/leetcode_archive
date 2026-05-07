import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    p=set(tree['p_id'])
    res=[]

    for _,r in tree.iterrows():
        if pd.isna(r['p_id']):
            res.append([r['id'],'Root'])
        
        elif r['id'] in p:
            res.append([r['id'],'Inner'])

        else:
            res.append([r['id'],'Leaf'])


    return pd.DataFrame({
        'id': [x[0] for x in res],
        'type': [x[1] for x in res]
    })