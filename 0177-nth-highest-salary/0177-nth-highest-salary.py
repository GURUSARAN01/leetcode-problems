import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    unique_salary = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salary.sort_values(ascending=False)

    if N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    if N > len(sorted_salaries):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
        
    nth_highest = sorted_salaries.iloc[N-1]
    
    return pd.DataFrame({f'getNthHighestSalary({N})':[nth_highest]})