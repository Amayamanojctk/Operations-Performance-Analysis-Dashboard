import pandas as pd
import os

# Load the cleaned data
df = pd.read_csv("../data/cleaned_sales_data.csv")

# Create summary reports
sales_summary = df.groupby("Category")["Sales"].sum().reset_index()
monthly_summary = df.groupby("Month")["Sales"].sum().reset_index()

# Save reports as Excel
output_path = "../excel_reports/sales_report.xlsx"

with pd.ExcelWriter(output_path) as writer:
    sales_summary.to_excel(writer, sheet_name="Category_Sales", index=False)
    monthly_summary.to_excel(writer, sheet_name="Monthly_Sales", index=False)

print("Excel report created successfully inside /excel_reports folder!")
