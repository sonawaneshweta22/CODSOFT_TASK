import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get the folder where this Python file is located
folder_path = os.path.dirname(os.path.abspath(__file__))

# Load the dataset
file_path = os.path.join(folder_path, "customer_sales_eda.csv")
df = pd.read_csv(file_path)

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Distribution of product categories
print("\nProduct Category Distribution:")
print(df["Product_Category"].value_counts())

# Distribution of payment methods
print("\nPayment Method Distribution:")
print(df["Payment_Method"].value_counts())

# Distribution of gender
print("\nGender Distribution:")
print(df["Gender"].value_counts())

# Product category distribution chart
plt.figure(figsize=(8, 5))

df["Product_Category"].value_counts().plot(kind="bar")

plt.title("Product Category Distribution")
plt.xlabel("Product Category")
plt.ylabel("Number of Purchases")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Payment method distribution chart
plt.figure(figsize=(8, 5))

df["Payment_Method"].value_counts().plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Purchases")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Payment method distribution chart
plt.figure(figsize=(8, 5))

df["Payment_Method"].value_counts().plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Purchases")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show() 

# Gender distribution chart
plt.figure(figsize=(7, 5))

df["Gender"].value_counts().plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

# Convert Purchase_Date to datetime
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Create monthly sales
monthly_sales = df.groupby(
    df["Purchase_Date"].dt.to_period("M")
)["Total_Sales"].sum()

# Convert period to string for plotting
monthly_sales.index = monthly_sales.index.astype(str)

# Monthly sales trend chart
plt.figure(figsize=(10, 5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()

# Relationship between Quantity and Total Sales
plt.figure(figsize=(8, 5))

plt.scatter(df["Quantity"], df["Total_Sales"])

plt.title("Quantity vs Total Sales")
plt.xlabel("Quantity Purchased")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()

plt.show()

# Outlier detection using IQR method

Q1 = df["Total_Sales"].quantile(0.25)
Q3 = df["Total_Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["Total_Sales"] < lower_bound) |
    (df["Total_Sales"] > upper_bound)
]

print("\nOutlier Detection:")
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Number of Outliers:", len(outliers))

print("\nOutlier Records:")
print(outliers[["Customer_ID", "Product_Category", "Quantity", "Total_Sales"]])

# Business Questions

# 1. What is the total revenue?
total_revenue = df["Total_Sales"].sum()
print("\nBusiness Questions:")
print("1. Total Revenue:", round(total_revenue, 2))


# 2. Which product category generates the highest sales?
category_sales = df.groupby("Product_Category")["Total_Sales"].sum()
top_category = category_sales.idxmax()
top_category_sales = category_sales.max()

print("2. Highest Sales Category:", top_category)
print("   Sales:", round(top_category_sales, 2))


# 3. What is the average purchase value?
average_purchase = df["Total_Sales"].mean()
print("3. Average Purchase Value:", round(average_purchase, 2))


# 4. Which payment method is used most frequently?
popular_payment = df["Payment_Method"].value_counts().idxmax()
payment_count = df["Payment_Method"].value_counts().max()

print("4. Most Popular Payment Method:", popular_payment)
print("   Number of Purchases:", payment_count)


# 5. Which gender has more customers?
gender_count = df["Gender"].value_counts()
top_gender = gender_count.idxmax()

print("5. Gender with More Customers:", top_gender)
print("   Number of Customers:", gender_count.max())


# 6. Which product category has the highest number of purchases?
popular_category = df["Product_Category"].value_counts().idxmax()
purchase_count = df["Product_Category"].value_counts().max()

print("6. Most Purchased Category:", popular_category)
print("   Number of Purchases:", purchase_count)