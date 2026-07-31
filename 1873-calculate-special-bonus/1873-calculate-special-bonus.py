import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    eligible_employees = employees[~(employees["employee_id"]%2==0) & ~(employees["name"].str.startswith("M"))]
    eligible_employees=eligible_employees.merge(employees, on="employee_id", how="right").fillna(0)
    eligible_employees = eligible_employees.rename(columns={"salary_x":"bonus"})
    return (eligible_employees[["employee_id", "bonus"]].sort_values(by="employee_id",ascending=True))