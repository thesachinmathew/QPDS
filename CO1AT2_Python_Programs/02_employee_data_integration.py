import pandas as pd

employees = pd.DataFrame({
    "EmployeeID": [101, 102, 103],
    "Name": ["Anu", "Bala", "Charan"],
    "DepartmentID": [1, 2, 4]
})
departments = pd.DataFrame({
    "DepartmentID": [1, 2, 3],
    "Department": ["HR", "IT", "Sales"]
})
merged = employees.merge(departments, on="DepartmentID", how="left", indicator=True)
print("Employees without a matching department:", (merged["_merge"] == "left_only").sum())
merged = merged.drop(columns="_merge")
merged.to_csv("employee_department.csv", index=False)
print(merged.to_string(index=False))
