import pandas as pd

df = pd.DataFrame({
    "BookID": [1, 2, 2, 4],
    "Title": ["Python Basics", "Data Science", "Data Science", "AI Guide"],
    "Author": ["Ravi", "Meena", "Meena", None],
    "Year": [2020, 2022, 2022, 2019]
})
df = df.drop_duplicates()
df["Author"] = df["Author"].fillna("Unknown")
df = df.dropna(subset=["BookID", "Title"])
df.to_csv("clean_books.csv", index=False)
print(df.to_string(index=False))
print("\\nSaved clean_books.csv")
