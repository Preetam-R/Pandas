# Create a DataFrame from the given data and display:

# First 3 rows

# Column names

# Data types

# Sample Input:
# data = {
#     'Name': ['A', 'B', 'C', 'D'],
#     'Age': [21, 22, 20, 23],
#     'Marks': [85, 90, 78, 88]
# }



import pandas as pd
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [21, 22, 20, 23],
    'Marks': [85, 90, 78, 88]
}

df = pd.DataFrame(data)
print("\nthe given dataframe is:\n")
print(df)

print("\nprinting the first 3 rows:\n")
print(df.head(3))

print("\nprinting the column names:\n")
print(df.columns)

print("\nprinting the data types:\n")
print(df.dtypes)