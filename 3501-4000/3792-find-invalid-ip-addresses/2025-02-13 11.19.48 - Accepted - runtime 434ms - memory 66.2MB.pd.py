import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    m={}
    
    for s in logs['ip']:
        IP=s.split('.')

        L=0 if len(IP)==4 else 1
        gt255=any(int(octet)>255 for octet in IP)
        leading_zeros=any(octet.startswith('0') for octet in IP)

        if any((gt255, leading_zeros, L)):
            if s in m:
                m[s]+=gt255+leading_zeros+L
            else:
                m[s]=gt255+leading_zeros+L

    m=dict(sorted(m.items(), key=lambda x: (x[1],x[0]), reverse=True))


    return pd.DataFrame({"ip":m.keys(), "invalid_count":m.values()})