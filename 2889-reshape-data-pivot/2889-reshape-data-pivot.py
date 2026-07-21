import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    out=weather.pivot(index='month', columns='city', values='temperature')
    return out