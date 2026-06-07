import pandas as pd

df = pd.read_csv("../05_Datasets/defence_budget.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nSummary Statistics")
print(df.describe())
