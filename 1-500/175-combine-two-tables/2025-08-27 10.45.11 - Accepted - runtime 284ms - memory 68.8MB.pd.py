import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    grouped=person.merge(right=address, how='left', on='personId')

    return grouped[['firstName', 'lastName', 'city', 'state']]