import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("TASK3_DATA_VISUALIZATION/archive/supermarket_sales - Sheet1.csv")

# Calculate total sales for each product line
sales_by_product = df.groupby("Product line")["Total"].sum()

# Create bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_product.index, y=sales_by_product.values)

# Add title and labels
plt.title("Total Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")

# Rotate category names
plt.xticks(rotation=45)

# Display the chart
plt.savefig("bar_chart.png", bbox_inches="tight")
plt.show()

# Calculate total sales by date
sales_by_date = df.groupby("Date")["Total"].sum()

# Create line chart
plt.figure(figsize=(10, 6))
plt.plot(sales_by_date.index, sales_by_date.values)

# Add title and labels
plt.title("Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")

# Display the chart
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("line_chart.png", bbox_inches="tight")
plt.show()

# Calculate total sales by product line
sales_by_product = df.groupby("Product line")["Total"].sum()

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    sales_by_product.values,
    labels=sales_by_product.index,
    autopct="%1.1f%%",
    startangle=90
)

# Add title
plt.title("Sales Distribution by Product Line")

# Display the chart
plt.savefig("pie_chart.png", bbox_inches="tight")
plt.show()

# Create histogram of total sales
plt.figure(figsize=(10, 6))
plt.hist(df["Total"], bins=20, edgecolor="black")

# Add title and labels
plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")

# Display the chart
plt.savefig("histogram.png", bbox_inches="tight")
plt.show()

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["Unit price"], y=df["Quantity"])

# Add title and labels
plt.title("Unit Price vs Quantity")
plt.xlabel("Unit Price")
plt.ylabel("Quantity")

# Display the chart
plt.savefig("scatter_plot.png", bbox_inches="tight")
plt.show()