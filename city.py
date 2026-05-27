import pandas as pd

# ==============================
# FILE SETTINGS
# ==============================
INPUT_FILE = "cleaned_data.csv"
OUTPUT_FILE = "final_cleaned_data.csv"

# ==============================
# STATE MAPPING
# ==============================
STATE_ABBREVIATIONS = {
    "CA": "California", "NY": "New York", "TX": "Texas",
    "FL": "Florida", "WA": "Washington", "MA": "Massachusetts",
    "NJ": "New Jersey", "PA": "Pennsylvania", "CT": "Connecticut"
}

# ==============================
# FUNCTION
# ==============================
def normalize_place_name(value):
    if pd.isna(value):
        return pd.NA

    text = str(value).strip()

    if text == "":
        return pd.NA

    text = text.replace(".", "")
    upper = text.upper()

    if upper in STATE_ABBREVIATIONS:
        return STATE_ABBREVIATIONS[upper]

    return text.title()

# ==============================
# MAIN FUNCTION
# ==============================
def main():

    df = pd.read_csv(INPUT_FILE)

    df.columns = df.columns.str.lower()

    print("📊 Missing values BEFORE:\n", df.isna().sum())

    # ==============================
    # DATE CLEANING
    # ==============================
    if "orderdate" in df.columns:
        df["orderdate"] = pd.to_datetime(df["orderdate"], errors="coerce")
        df = df[df["orderdate"].notna()]
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
    # FILL MISSING CITY
    # ==============================
    if "city" in df.columns:
        df["city"] = df["city"].fillna("Unknown")

    # ==============================
    # FILL MISSING STATE USING CITY
    # ==============================
    if "state" in df.columns and "city" in df.columns:

        mapping = (
            df[df["state"].notna()]
            .groupby("city")["state"]
            .agg(lambda x: x.mode()[0] if not x.mode().empty else "Unknown")
            .to_dict()
        )

        df["state"] = df["state"].fillna(df["city"].map(mapping))

        # still missing → fill as Unknown
        df["state"] = df["state"].fillna("Unknown")

    # ==============================
    # FILL NUMERICAL VALUES
    # ==============================
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    # ==============================
    # SAVE FILE
    # ==============================
    df.to_csv(OUTPUT_FILE, index=False)

    print("\n✅ Missing values AFTER:\n", df.isna().sum())
    print("📁 Output file:", OUTPUT_FILE)


# ==============================
# RUN
# ==============================
if __name__ == "__main__":
    main()