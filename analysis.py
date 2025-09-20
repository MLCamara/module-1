import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("ev_adoption_data.csv")

# Create EVs per 1000 people column
df["EVs_per_1000"] = df["EV_Registrations"] / (df["Population"] / 1000)

# Scatter plot: EVs per 1000 vs Charging Stations
plt.figure(figsize=(7,5))
sns.scatterplot(data=df, x="Charging_Stations", y="EVs_per_1000", hue="City", s=100)
plt.title("EV Adoption vs Charging Infrastructure")
plt.xlabel("Charging Stations")
plt.ylabel("EVs per 1,000 People")
plt.grid(True)
plt.savefig("ev_vs_charging.png")
plt.close()

# Scatter plot: EVs per 1000 vs Median Income
plt.figure(figsize=(7,5))
sns.scatterplot(data=df, x="Median_Income", y="EVs_per_1000", hue="City", s=100)
plt.title("EV Adoption vs Median Income")
plt.xlabel("Median Income ($)")
plt.ylabel("EVs per 1,000 People")
plt.grid(True)
plt.savefig("ev_vs_income.png")
plt.close()

# Heatmap: correlation matrix
plt.figure(figsize=(8,6))
corr = df[["EVs_per_1000", "Median_Income", "Charging_Stations", "Gas_Price"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix of EV Adoption Factors")
plt.savefig("ev_corr_heatmap.png")
plt.close()

print("Analysis complete. Figures saved as PNG files.")
