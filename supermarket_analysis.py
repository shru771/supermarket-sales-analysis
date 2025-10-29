# 🧾 Supermarket Sales Data Analysis Project
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("SuperMarket Analysis.csv")  # Updated filename

# Show first few rows
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create all plots in one figure
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 🧮 1️⃣ Total sales by city
city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False)
sns.barplot(x=city_sales.index, y=city_sales.values, ax=axes[0,0])
axes[0,0].set_title('Total Sales by City')
axes[0,0].set_ylabel('Sales ($)')

# 🧮 2️⃣ Gender-wise sales comparison
sns.boxplot(x='Gender', y='Sales', data=df, palette='Set2', ax=axes[0,1])
axes[0,1].set_title('Sales Distribution by Gender')

# 🧮 3️⃣ Payment method usage
sns.countplot(x='Payment', data=df, palette='cool', ax=axes[1,0])
axes[1,0].set_title('Payment Method Distribution')

# 🧮 4️⃣ Monthly sales trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_sales.plot(kind='line', marker='o', ax=axes[1,1])
axes[1,1].set_title('Monthly Sales Trend')
axes[1,1].set_ylabel('Total Sales ($)')

plt.tight_layout()
plt.show()
