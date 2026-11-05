import pandas as pd

df = pd.DataFrame({
    "Product": ["Pen", "Book", "Bag", "Pencil"],
    "Price": [10, None, "invalid", 5]
})
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
print("Missing or invalid prices:", df["Price"].isna().sum())
df["Price"] = df["Price"].fillna(df["Price"].median())
df.to_csv("clean_products.csv", index=False)
print(df.to_string(index=False))
