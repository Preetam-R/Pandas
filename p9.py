import pandas as pd

data = {
    'customer': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Bob', 'Bob'],
    'product':  ['Apple', 'Banana', 'Apple', 'Apple', 'Banana', 'Cherry', 'Banana'],
    'quantity': [3, 5, 2, 1, 4, 6, 4]
}

df = pd.DataFrame(data)
print(df)