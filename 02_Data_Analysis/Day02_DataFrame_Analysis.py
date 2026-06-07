# Day 02 - DataFrame Analysis

import pandas as pd

data = {
    "Country": ["India", "USA", "China"],
    "Defence_Spending": [75, 916, 296]
}

df = pd.DataFrame(data)

print(df)

print("\nTotal Spending:")
print(df["Defence_Spending"].sum())

print("\nAverage Spending:")
print(df["Defence_Spending"].mean())

print("\nHighest Spending:")
print(df["Defence_Spending"].max())
