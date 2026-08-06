import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_count = courses.groupby('class')['student'].count().reset_index()
    result = class_count[class_count['student']>=5][['class']]
    return result