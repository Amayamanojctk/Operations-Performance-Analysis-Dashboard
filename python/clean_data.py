import pandas as pd

# 1. Load dataset
df = pd.read_csv("../data/sales_data.csv")

# 2. Remove duplicates
df = df.drop_duplicates()

# 3. Handle missing values
df['Sales'] = df['Sales'].fillna(df['Sales'].median())
df['Quantity'] = df['Quantity'].fillna(0)

# 4. Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')

# 5. Create new columns
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year
df['Profit'] = df['Sales'] - df['Cost']

# 6. Save cleaned data
df.to_csv("../data/cleaned_sales_data.csv", index=False)

print("Data cleaning complete! File saved inside /data folder.")
