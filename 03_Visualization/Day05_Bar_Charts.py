import matplotlib.pyplot as plt

countries = [
    "India",
    "USA",
    "China",
    "Russia",
    "UK"
]

spending = [
    75,
    916,
    296,
    109,
    82
]

plt.bar(countries, spending)

plt.title("Defence Spending by Country")
plt.xlabel("Country")
plt.ylabel("Spending (Billion USD)")

plt.show()
