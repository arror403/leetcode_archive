import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    d=defaultdict(list)

    for u,a in zip(confirmations['user_id'], confirmations['action']):
        if a=='confirmed':
            d[u].append(1)
        else:
            d[u].append(0)

    t=signups['user_id']

    return pd.DataFrame({
        'user_id': list(t),
        'confirmation_rate': [round(sum(d[x])/len(d[x]), 2) if d[x] else 0 for x in t]})