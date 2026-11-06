import pandas as pd

print(f"\nPandas version : {pd.__version__} \n")


# Reading CSV File
df = pd.read_csv("employees.csv")
print("Display Dataframe: \n", df)

df = pd.read_csv("employees.csv", nrows=2)
print("\nRead only the first two rows :\n", df)

df = pd.read_csv(
    "employees.csv",
    usecols=["name", "salary"]
)
print("\nRead only selected columns :\n", df)

df = pd.read_csv(
    "employees.csv",
    index_col="emp_id"
)
print("\nSet a column as index:\n", df)

df1 = pd.read_csv("employees.csv", skiprows=1)
print(f"\nSkip first two rows :\n{df1}")


# Reading Excel File
print("\n\nReading Excel File")
df = pd.read_excel("employees.xlsx")
print(df)


# Reading JSON File
print("\n\nReading JSON File")
df = pd.read_json("employees.json")
print(df)


# Save as CSV
df.to_csv("output.csv", index=False)

# Save as Excel
df.to_excel("output.xlsx", index=False)

# Save as JSON
df.to_json("output.json", orient="records", indent=4)



# Read employee data
df = pd.read_csv("employees.csv")

# Filter employees earning more than 40000
filtered_df = df[df["salary"] > 40000]

# Sort by salary in descending order
filtered_df = filtered_df.sort_values(
    by="salary",
    ascending=False
)

# Save the result
filtered_df.to_csv("high_salary_employees.csv", index=False)
print("Filter employees earning more than 40000 and Sort by salary in descending order")
print(filtered_df)

print("------------")
print(df)
print("------------")
print(df.loc[0:1])


# First row
print("first row")
print(df.iloc[0])

# First row, second column
print("First row, second column")
print(df.iloc[0, 1])

# First three rows
print("First three rows")
print(df.iloc[0:3])

# First two rows and first two columns
print("First two rows and first two columns")
print(df.iloc[0:2, 0:2])


# Imagine you want to find employees earning more than ₹40,000.
result = df[df["salary"] > 40000]
print("more than ₹40,000.\n", result)


# Employees older than 25
print("Employees older than 25\n")
print(df[df["age"] > 25])

# Employees earning less than 50000
print("Employees earning less than 50000\n")
print(df[df["salary"] < 50000])

# Employees aged exactly 25
print("Employees aged exactly 25\n")
print(df[df["age"] == 25])

result = df[
    (df["age"] > 25) &
    (df["salary"] > 40000)
]
print("Age above 25 and salary above 40000\n", result)