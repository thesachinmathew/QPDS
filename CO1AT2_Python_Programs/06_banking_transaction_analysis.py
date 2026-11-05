import pandas as pd

df = pd.DataFrame({
    "TransactionID": [1, 2, 3, 4],
    "Account": ["A101", "A102", "A101", "A103"],
    "Amount": [5000, -2000, 1500, 0],
    "Type": ["Deposit", "Withdrawal", "Deposit", "Transfer"]
})
df = df.drop_duplicates(subset=["TransactionID"])
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
print("Invalid transactions:", df["Amount"].isna().sum())
print("\\nTransactions:")
print(df.to_string(index=False))
print("\\nTotal transaction amount:", df["Amount"].sum())
