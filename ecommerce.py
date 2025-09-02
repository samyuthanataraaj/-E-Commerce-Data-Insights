
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"D:\tamilanskills\project5\ecommerce.csv.csv")


print("Dataset Head:")
print(df.head())
print("\nDataset Info:")
print(df.info())


df['MRP'] = pd.to_numeric(df['MRP'], errors='coerce')
df['SellPrice'] = pd.to_numeric(df['SellPrice'], errors='coerce')


df.fillna({'BrandName': 'Unknown', 'Category': 'Others'}, inplace=True)


df['Profit'] = df['MRP'] - df['SellPrice']
df['Discount_Percent'] = ((df['MRP'] - df['SellPrice']) / df['MRP']) * 100


top_products = df['Product Name'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Selling Products")
plt.xlabel("Number of Orders")
plt.ylabel("Product Name")
plt.show()


brand_revenue = df.groupby('BrandName')['SellPrice'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=brand_revenue.values, y=brand_revenue.index, palette="coolwarm")
plt.title("Top 10 Brands by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Brand Name")
plt.show()


plt.figure(figsize=(8,5))
sns.histplot(df['Discount_Percent'], bins=20, kde=True, color='orange')
plt.title("Discount Percentage Distribution")
plt.xlabel("Discount %")
plt.ylabel("Frequency")
plt.show()


category_sales = df.groupby('Category')['SellPrice'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x=category_sales.index, y=category_sales.values, palette="magma")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(7,7))
df['Product Size'].value_counts().head(6).plot.pie(autopct="%1.1f%%", startangle=90, cmap="Set3")
plt.title("Product Size Distribution")
plt.ylabel("")
plt.show()


print("\nSummary Insights:")
print("1. Top-selling products:\n", top_products)
print("\n2. Top brands by revenue:\n", brand_revenue)
print("\n3. Highest Sales Category:", category_sales.index[0])
