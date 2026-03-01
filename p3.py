# Problem:

# Add a new column Result:

# "Pass" if Marks ≥ 40

# "Fail" otherwise

import pandas as pd

students = pd.DataFrame({
    "Name":["A","B","C","D"],
    "Marks":[85,40,52,30]
})

print(students)

students['Result'] = students['Marks'].apply(lambda x: "pass" if x >= 40 else "Fail")

print(students)

