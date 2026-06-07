import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "https://raw.githubusercontent.com/milindresearch/python-for-policy-research/main/05_Datasets/defence_budget.csv"
)

plt.bar(
    df["Country"],
    df["Defence_Spending_Billion_USD"]
)

plt.title("Defence Spending by Country")
plt.xlabel("Country")
plt.ylabel("Billion USD")

plt.show()
