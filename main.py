import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("supermarket_sales.csv")

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Handle missing values
data = data.dropna()

# ---- Analysis ----

# 1. Sales by product line
sales_by_product = data.groupby('Product line')['Total'].sum().sort_values(ascending=False)
print("Total Sales by Product Line:\n", sales_by_product)

# 2. Daily sales trend
daily_sales = data.groupby('Date')['Total'].sum()

plt.figure(figsize=(10,5))
plt.plot(daily_sales.index, daily_sales.values, marker='o')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales ($)")
plt.grid(True)
plt.show()

# 3. Sales by Branch
branch_sales = data.groupby('Branch')['Total'].sum()

plt.bar(branch_sales.index, branch_sales.values, color=['#4CAF50','#2196F3','#FF9800'])
plt.title("Sales by Branch")
plt.xlabel("Branch")
plt.ylabel("Total Sales ($)")
plt.show()

# 4. Payment method distribution
payment_counts = data['Payment'].value_counts()

plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Payment Method Distribution")
plt.show()
