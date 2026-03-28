import pandas as pd

data = {
    "region": ["North", "South", "North", "East", "South", "East"],
    "sales": [200, 150, 300, 400, 250, 100]
}
df = pd.DataFrame(data)

# Solution
result = df.groupby("region")["sales"].agg(total="sum", average="mean").reset_index()
print(result)