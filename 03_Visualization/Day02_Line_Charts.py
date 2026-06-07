import matplotlib.pyplot as plt

years = [
    2020,
    2021,
    2022,
    2023,
    2024
]

india_defence_budget = [
    66,
    70,
    72,
    74,
    75
]

plt.plot(years, india_defence_budget)

plt.title("India Defence Spending Trend")
plt.xlabel("Year")
plt.ylabel("Spending (Billion USD)")

plt.show()
