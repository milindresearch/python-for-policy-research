# Day 01 - Pandas Basics

import pandas as pd

countries = {
    "Country": ["India", "United States", "China"],
    "Defence_Spending_Billion_USD": [75, 916, 296]
}

df = pd.DataFrame(countries)

print(df)
