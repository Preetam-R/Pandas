import pandas as pd

data = {
    'order_id': [1, 2, 3, 4, 5, 6],
    'product':  ['Laptop', 'T-Shirt', 'Phone', 'Jeans', 'Tablet', 'Jacket'],
    'category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing'],
    'quantity':   [2, 5, 1, 3, 2, 1],
    'unit_price': [75000, 499, 45000, 1200, 30000, 2500]
}

df = pd.DataFrame(data)
print(df)

df['total_price'] = df['quantity'] * df['unit_price']
print(df[['product', 'quantity', 'unit_price', 'total_price']])