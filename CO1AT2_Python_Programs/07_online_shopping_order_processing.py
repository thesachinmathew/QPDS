import pandas as pd

orders = pd.DataFrame({
    "OrderID": [1001, 1002, 1003, 1004],
    "Customer": ["Asha", "Bala", "Charan", "Divya"],
    "Amount": [1200, 800, 2500, 600],
    "Status": ["Delivered", "Pending", "Delivered", "Cancelled"]
})
orders["Amount"] = pd.to_numeric(orders["Amount"], errors="coerce")
orders = orders.drop_duplicates(subset=["OrderID"])
completed = orders[orders["Status"] == "Delivered"]
completed.to_csv("completed_orders.csv", index=False)
print("Completed orders:")
print(completed.to_string(index=False))
print("\\nTotal completed sales:", completed["Amount"].sum())
