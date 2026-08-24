import pandas as pd

# 1. Import the dataset
df = pd.read_csv("dataset.csv")

# 2. Display the original dataset
print("Original Dataset:")
print(df)

# 3. Inspect the structure of the dataset
print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

# 4. Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Check for duplicate records
print("\nNumber of Duplicate Records:")
print(df.duplicated().sum())

# 6. Remove duplicate records
df = df.drop_duplicates()

# 7. Correct inconsistent text entries
df["Gender"] = df["Gender"].replace({
    "male": "Male",
    "female": "Female"
})

df["City"] = df["City"].replace({
    "pune": "Pune",
    "mumbai": "Mumbai",
    "nashik": "Nashik"
})

# 8. Convert Age and Marks into numeric values
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# 9. Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
# Round marks to 2 decimal places
df["Marks"] = df["Marks"].round(2)

# 10. Display the cleaned dataset
print("\nCleaned Dataset:")
print(df)

# 11. Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 12. Save the cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully as cleaned_dataset.csv")