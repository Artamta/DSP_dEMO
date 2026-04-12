import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---- Load data ----
data = pd.read_csv("/Users/ayush/Desktop/dsp/DSP_dEMO/Asgn-plotting/iip_wrt_prevyr.csv")

year = data["Year"]
mining = data["Mining"]
manf = data["Manufacturing"]
ele = data["Electricity"]
gen = data["General"]

# ---- Split positive & negative values ----
def split(arr):
    pos = np.where(arr > 0, arr, 0)
    neg = np.where(arr < 0, arr, 0)
    return pos, neg

m_pos, m_neg = split(mining)
mf_pos, mf_neg = split(manf)
e_pos, e_neg = split(ele)
g_pos, g_neg = split(gen)

# ---- Create plot ----
fig, ax = plt.subplots()

# ---- Plot stacked bars ----
ax.bar(year, m_pos, color='LightSkyBlue', label="Mining")
ax.bar(year, mf_pos, bottom=m_pos, color='IndianRed', label="Manufacturing")
ax.bar(year, e_pos, bottom=m_pos + mf_pos, color='LightSalmon', label="Electricity")
ax.bar(year, g_pos, bottom=m_pos + mf_pos + e_pos, color='Moccasin', label="General")

ax.bar(year, m_neg, color='LightSkyBlue')
ax.bar(year, mf_neg, bottom=m_neg, color='IndianRed')
ax.bar(year, e_neg, bottom=m_neg + mf_neg, color='LightSalmon')
ax.bar(year, g_neg, bottom=m_neg + mf_neg + e_neg, color='Moccasin')

# ---- Fix axis limits ----
ax.set_xlim(-0.5, len(year) - 0.5)   # X from first to last year
ax.set_ylim(-13, 50)                 # Y from -13 to 50

# ---- Remove default frame ----
for spine in ax.spines.values():
    spine.set_visible(False)

# ---- Draw separate axes ----
x_min = -0.5
x_max = len(year) - 0.5
y_min, y_max = -13, 50

# Y-axis (left)
ax.vlines(x_min, y_min, y_max, color='#444444', linewidth=0.8)

# X-axis (slightly above bottom so not touching)
gap = 0.03 * (y_max - y_min)
ax.hlines(y_min + gap, x_min, x_max, color='#444444', linewidth=0.8)

# ---- Dashed zero line ----
ax.axhline(0, color='#444444', linestyle='--', linewidth=0.6)

# ---- Labels and title ----
ax.set_title("IIP GROWTH RATE FOR INDIA", fontsize=14)
ax.set_xlabel("Financial Year", fontsize=12, labelpad=5)
ax.set_ylabel("IP Growth Rate\nw.r.t Previous Year", fontsize=12, labelpad=8)

# ---- Ticks ----
ax.tick_params(axis='x', rotation=90, labelsize=9)
ax.tick_params(axis='y', length=0, labelsize=9)

# ---- Legend (with box) ----
ax.legend(ncol=2, loc='upper left', bbox_to_anchor=(0.1, 1),
          frameon=True, edgecolor='black')

# ---- Data source ----
ax.text(0.01, 0.01,
        "Data source: https://eaindustry.nic.in/",
        transform=ax.transAxes,
        fontsize=9,
        color='lightgray')

# ---- Adjust spacing ----
plt.tight_layout()

# ---- Save ----
plt.savefig("iip_plot.png", dpi=320, bbox_inches='tight')

plt.show()