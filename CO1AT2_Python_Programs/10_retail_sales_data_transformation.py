import pandas as pd

df = pd.DataFrame({
    "Product": ["Pen", "Book", "Bag", "Pencil"],
    "Quantity": [10, 5, 2, 20],
    "UnitPrice": [10, 50, 500, 5]
})
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]
df["Product"] = df["Product"].str.upper()
print(df.to_string(index=False))
print("\\nTotal retail sales:", df["TotalSales"].sum())
