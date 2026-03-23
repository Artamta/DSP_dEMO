import pandas as pd
import matplotlib.pyplot as plt

# Choose a few regions to keep plot clean
regions = ["central-africa", "east-asia", "europe-and-north-america", "south-asia"]
colors = ["red", "blue", "green", "orange"]

plt.figure(figsize=(9,6))

for i, region in enumerate(regions):

    # ---------- 2020 DATA ----------
    life_2020 = pd.read_csv(f"output/{region}_life_2020.csv", header=None)
    gdp_2020 = pd.read_csv(f"output/{region}_gdp_2020.csv", header=None)
    trade_2020 = pd.read_csv(f"output/{region}_trade_2020.csv", header=None)

    df_2020 = pd.DataFrame({
        "gdp": pd.to_numeric(gdp_2020[3], errors='coerce'),
        "life": pd.to_numeric(life_2020[3], errors='coerce'),
        "trade": pd.to_numeric(trade_2020[3], errors='coerce')
    }).dropna()

    # ---------- 1990 DATA ----------
    # (you need to create these files same way as 2020 but using grep 1990)
    try:
        life_1990 = pd.read_csv(f"output/{region}_life_1990.csv", header=None)
        gdp_1990 = pd.read_csv(f"output/{region}_gdp_1990.csv", header=None)
        trade_1990 = pd.read_csv(f"output/{region}_trade_1990.csv", header=None)

        df_1990 = pd.DataFrame({
            "gdp": pd.to_numeric(gdp_1990[3], errors='coerce'),
            "life": pd.to_numeric(life_1990[3], errors='coerce'),
            "trade": pd.to_numeric(trade_1990[3], errors='coerce')
        }).dropna()

    except:
        df_1990 = None

    # ---------- PLOT 2020 ----------
    plt.scatter(
        df_2020["gdp"],
        df_2020["life"],
        s=df_2020["trade"] * 0.2,
        color=colors[i],
        alpha=0.6,
        label=f"{region} (2020)"
    )

    # ---------- PLOT 1990 ----------
    if df_1990 is not None:
        plt.scatter(
            df_1990["gdp"],
            df_1990["life"],
            s=df_1990["trade"] * 0.2,
            color=colors[i],
            alpha=0.3,        # lighter → reduces clutter
            marker='x',       # different shape
            label=f"{region} (1990)"
        )

# ---------- FINAL TOUCH ----------
plt.xlabel("GDP per capita")
plt.ylabel("Life Expectancy")
plt.title("Demographic Data (1990 vs 2020)")
plt.legend()
plt.grid(True)

plt.show()