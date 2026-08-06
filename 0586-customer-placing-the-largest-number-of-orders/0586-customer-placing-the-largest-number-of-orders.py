import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order_count = orders.groupby('customer_number')['order_number'].count().reset_index().sort_values(by='order_number',ascending=False)
    result = order_count.head(1)[['customer_number']]
    return result