import matplotlib.pyplot as plt

gdp = [2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

defence_spending = [50, 55, 60, 68, 75, 85]

plt.scatter(gdp, defence_spending)

plt.title("GDP Growth vs Defence Spending")
plt.xlabel("GDP Growth (%)")
plt.ylabel("Defence Spending (Billion USD)")

plt.show()
