import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel("Auto_Mobile_Data.xlsx")

# Drop unnecessary columns
df = df.drop(columns=["Unnamed: 0", "index"])

# Price by body style
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="body-style", y="price")
plt.title("Car Price by Body Style")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/price_by_bodystyle.png")
plt.close()

# Horsepower vs Price
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="horsepower", y="price", hue="body-style")
plt.title("Horsepower vs Price")
plt.tight_layout()
plt.savefig("images/horsepower_vs_price.png")
plt.close()

# Correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df.select_dtypes(include="number").corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation")
plt.tight_layout()
plt.savefig("images/correlation_heatmap.png")
plt.close()
