
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the cleaned dataset
df = pd.read_csv("cleaned_sales.csv")

# Step 2: Display the dataset
print("SALES DATA ANALYSIS")
print("-" * 40)
print(df.to_string(index=False))

# Step 3: Calculate total sales
total_sales = df["Sales"].sum()

# Step 4: Calculate average order value
# First calculate sales for each order
order_sales = df.groupby("Order_ID")["Sales"].sum()
average_order_value = order_sales.mean()

# Step 5: Find the top products by sales
product_sales = df.groupby("Product")["Sales"].sum()
product_sales = product_sales.sort_values(ascending=False)

# Step 6: Calculate sales by category
category_sales = df.groupby("Category")["Sales"].sum()
category_sales = category_sales.sort_values(ascending=False)

# Step 7: Calculate sales by region
region_sales = df.groupby("Region")["Sales"].sum()
region_sales = region_sales.sort_values(ascending=False)

# Step 8: Display key metrics
print("\nKEY METRICS")
print("-" * 40)
print(f"Total Sales: {total_sales:,.2f}")
print(f"Total Orders: {df['Order_ID'].nunique()}")
print(f"Average Order Value: {average_order_value:,.2f}")

print("\nSALES BY PRODUCT")
print(product_sales)

print("\nSALES BY CATEGORY")
print(category_sales)

print("\nSALES BY REGION")
print(region_sales)

# Step 9: Save the analysis tables
product_sales.to_csv("sales_by_product.csv")
category_sales.to_csv("sales_by_category.csv")
region_sales.to_csv("sales_by_region.csv")

# Step 10: Create a category sales chart
category_sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# Step 11: Create a region sales chart
region_sales.plot(kind="bar", title="Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# Step 12: Save a short text report
with open("Sales_Analysis_Report.txt", "w", encoding="utf-8") as file:
    file.write("SALES DATA ANALYSIS REPORT\n")
    file.write("=" * 35 + "\n")
    file.write(f"Total Sales: {total_sales:,.2f}\n")
    file.write(f"Total Orders: {df['Order_ID'].nunique()}\n")
    file.write(f"Average Order Value: {average_order_value:,.2f}\n\n")
    file.write("Sales by Product:\n")
    file.write(product_sales.to_string())
    file.write("\n\nSales by Category:\n")
    file.write(category_sales.to_string())
    file.write("\n\nSales by Region:\n")
    file.write(region_sales.to_string())

print("\nAnalysis completed successfully!")
print("Reports and charts have been saved.")
