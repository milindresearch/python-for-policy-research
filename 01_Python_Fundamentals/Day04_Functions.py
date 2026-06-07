# Day 04 - Functions

def calculate_defence_budget(gdp, percentage):
    budget = gdp * (percentage / 100)
    return budget

india_gdp = 4000

defence_budget = calculate_defence_budget(india_gdp, 2.0)

print("Estimated Defence Budget:", defence_budget)
