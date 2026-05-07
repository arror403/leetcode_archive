import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    c=user_content['content_text']
    converted_text=[]

    for x in c:
        r=[]
        for s in x.split():
            if '-' not in s:
                r.append(s[0].upper()+s[1:].lower())
            else:
                tmp=[]
                for y in s.split('-'):
                    tmp.append(y[0].upper()+y[1:].lower())

                r.append('-'.join(tmp))
                
        converted_text.append(' '.join(r))

    # print(r)
    return pd.DataFrame({'content_id': list(user_content['content_id']),
                         'original_text': c, 
                         'converted_text': converted_text})