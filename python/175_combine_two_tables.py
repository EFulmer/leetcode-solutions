import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = person.merge(address, 'left', on="personId")
    return result[["firstName", "lastName", "city", "state"]]
