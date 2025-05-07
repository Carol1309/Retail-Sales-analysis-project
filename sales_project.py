# Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Dataset
df = pd.read_csv('D:/Downloads/retail_sales.csv')

# Data Cleaning & Feature Engineering
df['Date'] = pd.to_datetime(df['Date'])  # Convert date to datetime
df['Sales'] = df['Quantity'] * df['UnitPrice'] * (1 - df['Discount'])  # Calculate net sales

#  Descriptive Statistics
print("Dataset Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())
print("\nSummary Statistics:\n", df.describe())

# Total Sales by Category
sales_by_category = df.groupby('ProductCategory')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Category:\n", sales_by_category)

#  Total Sales Over Time
sales_by_date = df.groupby('Date')['Sales'].sum()

#  Visualization Setup
plt.figure(figsize=(14, 8))
sns.set_style('whitegrid')

#  1. Sales Trend Over Time
plt.subplot(2, 1, 1)
sales_by_date.plot()
plt.title('Daily Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales ($)')

#  2. Sales by Product Category
plt.subplot(2, 2, 3)
sales_by_category.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.ylabel('Sales ($)')

#  3. Top 10 Highest Transactions
top_sales = df.sort_values(by='Sales', ascending=False).head(10)
plt.subplot(2, 2, 4)
sns.barplot(x=top_sales['Sales'], y=top_sales['ProductCategory'])
plt.title('Top 10 Sales Transactions')
plt.xlabel('Sales ($)')

plt.tight_layout()
plt.show()