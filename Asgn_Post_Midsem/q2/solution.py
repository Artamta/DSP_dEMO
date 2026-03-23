import pandas as pd
import matplotlib.pyplot as plt
import glob

files = glob.glob("output/*_life_2020.csv")

all_data = []

for life_file in files:
    region = life_file.split("/")[-1].replace("_life_2020.csv", "")

    gdp_file = f"output/{region}_gdp_2020.csv"
    co2_file = f"output/{region}_co2_2020.csv"
    trade_file = f"output/{region}_trade_2020.csv"

    life = pd.read_csv(life_file, header=None)
    gdp = pd.read_csv(gdp_file, header=None)
    co2 = pd.read_csv(co2_file, header=None)
    trade = pd.read_csv(trade_file, header=None)

    df = pd.DataFrame({
        "country": life[0],
        "gdp": gdp[3],
        "life": life[3],
        "co2": co2[3],
        "trade": trade[3],
        "region": region
    })

    all_data.append(df)

data = pd.concat(all_data)

for region in data["region"].unique():
    subset = data[data["region"] == region]

    plt.scatter(
        subset["gdp"],              # X-axis
        subset["life"],             # Y-axis
        s=subset["trade"] * 0.5,    # size
        c=subset["co2"],            # color
        alpha=0.6,
        label=region
    )

plt.xlabel("GDP per capita")
plt.ylabel("Life Expectancy")
plt.title("Demographic Data (2020)")
plt.legend()
plt.show()