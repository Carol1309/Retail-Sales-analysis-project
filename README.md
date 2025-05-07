# Retail-Sales-analysis-project
# 📘 Project Overview
This project focuses on performing a comprehensive analysis of a retail sales dataset to uncover business insights. The dataset contains 100 transaction records including product details, categories, pricing, discounts, and dates. The goal is to analyze sales performance over time, evaluate product categories, and identify key patterns that could support decision-making in marketing, inventory, and strategy.

# 🎯 Objectives
- Clean and preprocess sales data  
- Calculate total sales per transaction  
- Analyze sales trends over time  
- Identify high-performing product categories  
- Visualize key metrics using graphs  

# 🧾 Dataset Features

| Column Name       | Description                               |
|-------------------|-------------------------------------------|
| `Date`            | Date of the transaction                   |
| `ProductID`       | Unique identifier for the product         |
| `ProductCategory` | Product's category (e.g., Toys, Clothing) |
| `Quantity`        | Number of units sold                      |
| `UnitPrice`       | Price per unit of product                 |
| `Discount`        | Discount applied (as a fraction)          |

# 🧼 Data Cleaning and Feature Engineering
- Converted the `Date` column to datetime format  
- Created a new column `Sales` using the formula:  
  `Sales = Quantity × UnitPrice × (1 - Discount)`  
- Verified data integrity: no missing values were found  

# 📊 Key Insights
- **Toys** emerged as the top-grossing product category  
- **Sales peaks** were observed during the end-of-year holiday period (late December)  
- The **average transaction** generated ~$1,325 in revenue  
- **Top 10 transactions** accounted for a significant portion of total sales, indicating a few high-value purchases  

# 📈 Visualizations
- 📅 Line Plot: Daily total sales trend  
- 📊 Bar Chart: Total sales by product category  
- 🔝 Bar Plot: Top 10 highest-value transactions  

# ✅ Conclusion
This analysis provides a foundational understanding of sales performance and customer purchasing behavior. The insights can be used by stakeholders to optimize product offerings, improve promotions, and plan inventory more effectively.

