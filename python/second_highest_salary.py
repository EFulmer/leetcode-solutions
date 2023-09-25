import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
  salaries = employee.loc[:, ['salary']].sort_values(by=['salary'], ascending=False).drop_duplicates()
  if salaries.shape[0] < 2:
    salary = None
  else:
    salary = salaries.iloc[1]['salary']
  return pd.DataFrame([{'SecondHighestSalary': salary}])
