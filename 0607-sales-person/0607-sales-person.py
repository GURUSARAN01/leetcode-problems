import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # LEFT JOIN (sales_person, orders)
    df = pd.merge(
        sales_person, orders,
        on = 'sales_id',
        how = 'left'
    )

    # LEFT JOIN (company, df)
    df = pd.merge(
        company, df,
        on = 'com_id',
        how = 'left'
    )

    # sold to red
    red_sales = df[df['name_x'] == 'RED']['sales_id']

    # who never sold to red
    return sales_person[
        ~sales_person['sales_id'].isin(red_sales)
    ][['name']]