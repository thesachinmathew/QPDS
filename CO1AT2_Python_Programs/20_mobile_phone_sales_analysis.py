import pandas as pd

df = pd.DataFrame({
    "Brand": ["Samsung", "Apple", "Vivo", "Samsung", "Apple"],
    "Model": ["A15", "iPhone 15", "V30", "S24", "iPhone 16"],
    "UnitsSold": [20, 15, 12, 10, 8],
    "Price": [18000, 70000, 30000, 65000, 80000]
})
df["Sales"] = df["UnitsSold"] * df["Price"]
print("Sales by brand:")
print(df.groupby("Brand")["Sales"].sum().to_string())
print("\\nTotal sales revenue:", df["Sales"].sum())
