
import pandas as pd

# Step 1: Load the original dataset
df = pd.read_csv("messy_sales.csv")

print("ORIGINAL DATA")
print(df)
print("\nOriginal rows:", len(df))

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Remove extra spaces from text columns
text_columns = ["Product", "Category", "Region"]

for column in text_columns:
    df[column] = df[column].apply(
        lambda value: value.strip() if isinstance(value, str) else value
    )

# Step 4: Standardize capitalization
df["Product"] = df["Product"].str.title()
df["Category"] = df["Category"].str.title()
df["Region"] = df["Region"].str.title()

# Step 5: Convert dates into a consistent format
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"], errors="coerce"
)

# Step 6: Convert numeric columns into numbers
for column in ["Quantity", "Unit_Price"]:
    df[column] = pd.to_numeric(
        df[column], errors="coerce"
    )

# Step 7: Handle missing values
# Fill missing text fields with "Unknown"
df["Product"] = df["Product"].fillna("Unknown")
df["Category"] = df["Category"].fillna("Unknown")
df["Region"] = df["Region"].fillna("Unknown")

# Fill missing quantity and unit price with their medians
df["Quantity"] = df["Quantity"].fillna(
    df["Quantity"].median()
)
df["Unit_Price"] = df["Unit_Price"].fillna(
    df["Unit_Price"].median()
)

# Step 8: Create a Sales column
df["Sales"] = df["Quantity"] * df["Unit_Price"]

# Step 9: Save the cleaned dataset
df.to_csv("cleaned_sales.csv", index=False)

# Step 10: Display the results
print("\nCLEANED DATA")
print(df.to_string(index=False))

print("\nCleaning completed successfully!")
print("Remaining rows:", len(df))
print("Missing values per column:")
print(df.isnull().sum())
print("\nSaved file: cleaned_sales.csv")
