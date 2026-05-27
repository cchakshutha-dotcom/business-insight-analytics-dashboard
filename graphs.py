import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("final_cleaned_data.csv")

# ==============================
# CREATE SUBPLOTS (3 rows × 3 columns)
# ==============================
fig, axs = plt.subplots(3, 3, figsize=(18, 12))

# ==============================
# 1. Scatter: Quantity vs Sales
# ==============================
axs[0,0].scatter(df['quantityordered'], df['sales'])
axs[0,0].set_title("Quantity vs Sales")

# ==============================
# 2. Scatter: Price vs Sales
# ==============================
axs[0,1].scatter(df['priceeach'], df['sales'])
axs[0,1].set_title("Price vs Sales")

# ==============================
# 3. Line Chart
# ==============================
df.groupby('quantityordered')['sales'].mean().plot(ax=axs[0,2])
axs[0,2].set_title("Line: Quantity vs Sales")

# ==============================
# 4. Bar: ProductLine
# ==============================
df.groupby('productline')['sales'].sum().plot(kind='bar', ax=axs[1,0])
axs[1,0].set_title("ProductLine vs Sales")

# ==============================
# 5. Pie Chart
# ==============================
df.groupby('productline')['sales'].sum().plot(kind='pie', autopct='%1.1f%%', ax=axs[1,1])
axs[1,1].set_title("ProductLine Distribution")

# ==============================
# 6. Bar: State
# ==============================
df.groupby('state')['sales'].sum().sort_values(ascending=False).head(5).plot(kind='bar', ax=axs[1,2])
axs[1,2].set_title("Top States")

# ==============================
# 7. Bar: DealSize
# ==============================
df.groupby('dealsize')['sales'].sum().plot(kind='bar', ax=axs[2,0])
axs[2,0].set_title("DealSize vs Sales")

# ==============================
# 8. Histogram: Sales
# ==============================
axs[2,1].hist(df['sales'], bins=20)
axs[2,1].set_title("Sales Distribution")

# ==============================
# 9. Histogram: Quantity
# ==============================
axs[2,2].hist(df['quantityordered'], bins=20)
axs[2,2].set_title("Quantity Distribution")

# ==============================
# ADJUST LAYOUT
# ==============================
plt.tight_layout()
plt.show()

print("✅ All graphs shown in one sheet!")