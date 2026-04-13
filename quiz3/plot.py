import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load and clean data
data = pd.read_csv("sol.csv", header=None)
data = data[0].str.split(n=1, expand=True)
data.columns = ['count', 'country']

data['count'] = data['count'].astype(int)

# Take top 10 (important for readability)
data = data.sort_values(by='count', ascending=False).head(10)

count = data["count"]
country = data["country"]

# Convert categories to numeric positions
x = np.arange(len(country))

fig, ax = plt.subplots(figsize=(8,5))

# Plot bars
ax.bar(x, count)

# 🔥 Floating axes (THIS is what they want)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Hide extra spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Labels
ax.set_xticks(x)
ax.set_xticklabels(country, rotation=45, ha='right')

ax.set_title("Entries per Country")
ax.set_xlabel("Country")
ax.set_ylabel("Entries")

plt.tight_layout()
plt.show()