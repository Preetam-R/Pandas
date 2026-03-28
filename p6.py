import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "department": ["Engineering", "HR", "Engineering", "Marketing", "Engineering"],
    "salary": [90000, 60000, 65000, 75000, 80000]
}
df = pd.DataFrame(data)

# Solution
result = df[(df["department"] == "Engineering") & (df["salary"] > 70000)]
print(result)