import pandas as pd
import numpy as np

# Step 1: Load dataset
file_path = "sales_data_sample.xlsx"
df = pd.read_excel(file_path)

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Handle missing values

# Numeric → fill with mean
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].mean())

# Categorical → fill with mode
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Step 4: Clean text data
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip()

# Step 5: Fix column names (structured format but SAME meaning)
df.columns = df.columns.str.strip()          # remove spaces
df.columns = df.columns.str.upper()         # make consistent
df.columns = df.columns.str.replace(" ", "_")  # replace spaces with underscore

# Step 6: Convert data types where possible
for col in df.columns:
    try:
        df[col] = pd.to_numeric(df[col])
    except:
        pass

# Step 7: Handle outliers (IQR method)
for col in df.select_dtypes(include=np.number).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[col] = np.where(df[col] < lower, lower, df[col])
    df[col] = np.where(df[col] > upper, upper, df[col])

# Step 8: Save structured dataset
df.to_excel("final_structured_data.xlsx", index=False)

print("✅ Unstructured data converted to structured data successfully!")

import pandas as pd
import numpy as np

# Step 1: Load dataset
df = pd.read_excel("sales_data_sample.xlsx")

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Fix column names (clean + structured)
df.columns = df.columns.str.strip()          # remove spaces
df.columns = df.columns.str.upper()         # uppercase
df.columns = df.columns.str.replace(" ", "_")

# Step 4: Handle missing values

# Numeric → fill with mean
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].mean())

# Categorical → fill with mode
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Step 5: Clean text data
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip()

# Step 6: Convert data types
for col in df.columns:
    try:
        df[col] = pd.to_numeric(df[col])
    except:
        pass

# Step 7: Fix date column (VERY IMPORTANT)
if "ORDERDATE" in df.columns:
    df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors='coerce')

# Step 8: Handle outliers (IQR method)
for col in df.select_dtypes(include=np.number).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[col] = np.where(df[col] < lower, lower, df[col])
    df[col] = np.where(df[col] > upper, upper, df[col])

# Step 9: Remove unwanted symbols / dirty values
df.replace(["Unknown", "NA", "?"], np.nan, inplace=True)

# Step 10: Save cleaned dataset
df.to_excel("cleaned_sales_data.xlsx", index=False)

print("✅ Data cleaned successfully!")