import pandas as pd

# Load your structured dataset
df = pd.read_excel("final_structured_data.xlsx")

# Columns to remove
columns_to_remove = [
    "ORDERNUMBER",
    "QUANTITYORDERED",
    "ORDERLINENUMBER",
    "STATUS",
    "QTR_ID",
    "CUSTOMERNAME",
    "PHONE",
    "ADDRESSLINE2",
    "STATE",
    "TERRITORY",
    "CONTACTLASTNAME",
    "CONTACTFIRSTNAME"
]

# Remove columns
df = df.drop(columns=columns_to_remove, errors='ignore')

# Save remaining data
df.to_excel("remaining_cleaned_data.xlsx", index=False)

print("✅ Selected columns removed successfully!")



import pandas as pd

# Read Excel file (corrected)
df = pd.read_excel("sales_data_sample.xlsx")

columns_to_remove = [
    "ORDERNUMBER",
    "ORDERLINENUMBER",
    "QTR_ID",
    "MSRP",
    "PRODUCTCODE",
    "PHONE",
    "ADDRESSLINE1",
    "ADDRESSLINE2",
    "POSTALCODE",
    "TERRITORY",
    "CONTACTLASTNAME",
    "CONTACTFIRSTNAME"
]

df = df.drop(columns=columns_to_remove, errors='ignore')

# Save as CSV
df.to_csv("cleaned_data.csv", index=False)

print("✅ Columns removed and CSV file created successfully!")


import pandas as pd

# ==============================
# FILE SETTINGS
# ==============================
INPUT_FILE = "cleaned_data.csv"
OUTPUT_FILE = "cleaned_data_final.csv"   # New file to avoid permission error

# ==============================
# STATE MAPPING
# ==============================
STATE_ABBREVIATIONS = {
    "CA": "California",
    "NY": "New York",
    "TX": "Texas",
    "FL": "Florida",
    "WA": "Washington",
    "MA": "Massachusetts"
}

# ==============================
# FUNCTION: CLEAN TEXT
# ==============================
def normalize_place_name(value):
    if pd.isna(value):
        return pd.NA

    text = str(value).strip()
    if text == "":
        return pd.NA

    text_upper = text.upper()

    if text_upper in STATE_ABBREVIATIONS:
        return STATE_ABBREVIATIONS[text_upper]

    return text.title()

# ==============================
# MAIN FUNCTION
# ==============================
def main():

    # Load CSV file
    df = pd.read_csv(INPUT_FILE)

    # Convert all column names to lowercase (VERY IMPORTANT)
    df.columns = df.columns.str.lower()

    print("📊 Original columns:", df.columns.tolist())

    # ==============================
    # DATE CLEANING
    # ==============================
    if "orderdate" in df.columns:
        df["orderdate"] = pd.to_datetime(df["orderdate"], errors="coerce")

        # Remove invalid dates
        df = df[df["orderdate"].notna()]

        # Format date
        df["orderdate"] = df["orderdate"].dt.strftime("%Y-%m-%d")

    # ==============================
    # CLEAN STATE & CITY
    # ==============================
    if "state" in df.columns:
        df["state"] = df["state"].replace("", pd.NA)
        df["state"] = df["state"].apply(normalize_place_name)

    if "city" in df.columns:
        df["city"] = df["city"].replace("", pd.NA)
        df["city"] = df["city"].apply(normalize_place_name)

    # ==============================
    # FILL MISSING STATE USING CITY
    # ==============================
    if "state" in df.columns and "city" in df.columns:

        city_state_map = (
            df[df["state"].notna()]
            .groupby("city")["state"]
            .agg(lambda x: x.mode()[0] if not x.mode().empty else pd.NA)
            .to_dict()
        )

        missing_state = df["state"].isna() & df["city"].notna()
        df.loc[missing_state, "state"] = df.loc[missing_state, "city"].map(city_state_map)

    # ==============================
    # REMOVE UNWANTED COLUMNS
    # ==============================
    columns_to_drop = [
        "ordernumber",
        "orderlinenumber",
        "qtr_id",
        "msrp",
        "productcode",
        "phone",
        "addressline1",
        "addressline2",
        "postalcode",
        "territory",
        "contactlastname",
        "contactfirstname"
    ]

    # Drop only existing columns
    existing_columns = [col for col in columns_to_drop if col in df.columns]
    df = df.drop(columns=existing_columns)

    # ==============================
    # SAVE CLEANED DATA
    # ==============================
    df.to_csv(OUTPUT_FILE, index=False)

    # ==============================
    # PRINT SUMMARY
    # ==============================
    print("\n✅ DATA CLEANING COMPLETED SUCCESSFULLY!")
    print("📁 Output file:", OUTPUT_FILE)
    print("🗑️ Removed columns:", existing_columns)
    print("📊 Remaining columns:", df.columns.tolist())
    print("❗ Missing values in state:", df["state"].isna().sum() if "state" in df.columns else "N/A")


# ==============================
# RUN PROGRAM
# ==============================
if __name__ == "__main__":
    main()