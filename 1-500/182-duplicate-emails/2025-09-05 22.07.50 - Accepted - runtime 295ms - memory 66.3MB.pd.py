import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'Email': [v for v,f in Counter(person['email']).items() if f>1]})