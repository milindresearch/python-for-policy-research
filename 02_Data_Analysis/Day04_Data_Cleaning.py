import pandas as pd

df = pd.read_csv("../05_Datasets/defence_budget.csv")

print("Original Data")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

print("\nCleaned Data")
print(df)
