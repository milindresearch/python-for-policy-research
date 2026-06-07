import matplotlib.pyplot as plt

defence_spending = [
    50,
    60,
    65,
    70,
    75,
    80,
    85,
    90,
    100,
    120
]

plt.hist(defence_spending)

plt.title("Distribution of Defence Spending")
plt.xlabel("Spending (Billion USD)")
plt.ylabel("Frequency")

plt.show()
