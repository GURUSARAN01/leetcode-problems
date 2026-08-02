import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result = patients[patients['conditions'].str.contains('^DIAB1|\sDIAB1')]
    result =  result[['patient_id', 'patient_name', 'conditions']]
    return result