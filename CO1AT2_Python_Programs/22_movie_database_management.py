import pandas as pd

df = pd.DataFrame({
    "Movie": ["Movie A", "Movie B", "Movie C", "Movie D"],
    "Genre": ["Drama", "Action", "Drama", "Comedy"],
    "Rating": [8.2, 7.5, 9.0, 6.8],
    "Year": [2020, 2022, 2021, 2019]
})
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
print("Average movie rating:", round(df["Rating"].mean(), 2))
print("\\nHighest-rated movies:")
print(df[df["Rating"] >= 8].sort_values("Rating", ascending=False).to_string(index=False))
