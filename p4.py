import pandas as pd

# Find average salary department-wise.

# Sample Input:
# Dept   Salary
# IT     50000
# HR     40000
# IT     60000
# HR     45000

sal = pd.DataFrame({
    "dept":["IT","HR","IT","HR"],
    "SAL":[50000,40000,60000,45000]
})

print(sal)

grouped = sal.groupby('dept')
print("the avg salary:\n")
print(grouped.mean())

