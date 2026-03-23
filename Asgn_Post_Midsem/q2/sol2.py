import pandas as pd
import matplotlib.pyplot as plt

regions = ["central-africa", "east-asia", "europe-and-north-america", "south-asia"]
colors = ["red", "blue", "green", "orange"]

plt.figure(figsize=(8,6))

for i, region in enumerate(regions):
    life = pd.read_csv(f"output/{region}_life_2020.csv", header=None)
    gdp = pd.read_csv(f"output/{region}_gdp_2020.csv", header=None)
    trade = pd.read_csv(f"output/{region}_trade_2020.csv", header=None)

    # Convert to numeric
    gdp_vals = pd.to_numeric(gdp[3], errors='coerce')
    life_vals = pd.to_numeric(life[3], errors='coerce')
    trade_vals = pd.to_numeric(trade[3], errors='coerce')

    # Combine and clean
    df = pd.DataFrame({
        "gdp": gdp_vals,
        "life": life_vals,
        "trade": trade_vals
    }).dropna()

    plt.scatter(
        df["gdp"],
        df["life"],
        s=df["trade"] * 0.2,
        color=colors[i],
        alpha=0.6,
        label=region
    )

plt.xlabel("GDP per capita")
plt.ylabel("Life Expectancy")
plt.title("Demographic Data (2020)")
plt.legend()
plt.grid(True)
plt.show()