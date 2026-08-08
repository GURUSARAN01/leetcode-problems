import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(students, subjects,how='cross')
    examinations.rename(columns={'subject_name':'subject_name2'}, inplace=True)
    df_result = merged.merge(examinations, how='left', left_on=['student_id', 'subject_name'], right_on=['student_id','subject_name2'])
    return df_result.groupby(['student_id', 'student_name', 'subject_name'], dropna=False)['subject_name2'].count().reset_index(name='attended_exams')