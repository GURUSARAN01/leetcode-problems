import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    N=2
    if len(sorted_salaries) < N:
        return pd.DataFrame({"SecondHighestSalary":[None]})
    
    second_highest = sorted_salaries.iloc[2-1]
    return pd.DataFrame({"SecondHighestSalary": [second_highest]})