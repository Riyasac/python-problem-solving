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
print("\nAge above 25 and salary above 40000\n", result)

result = df[
    (df["age"] > 28) |
    (df["salary"] > 50000)
]
print("\nAge above 28 or salary above 50000\n", result)

result = df[~(df["salary"] > 40000)]
print("\nEmployees not earning more than 40000\n", result)

# Selecting a single column
names = df["name"]
print("\nNames of employees\n", names)

# Selecting multiple columns
selected_columns = df[["name", "salary"]]
print("\nSelected columns\n", selected_columns)

# Selecting rows based on a list of values
result = df[df["name"].isin(["Rahul", "Priya"])]
print("\nSelected rows\n", result)

result = df[df["salary"].between(30000, 50000)]
print("\nEmployees earning between 30000 and 50000\n", result)

result = df[df["salary"].isna()]
print("\nEmployees with missing salary\n", result)

result = df[df["salary"].notna()]
print("\nEmployees with non-missing salary\n", result)

result = df.query("salary > 40000 and age > 25")
print("\nEmployees earning more than 40000 and age above 25\n", result)

# Ranking employees based on salary
df["salary_rank"] = df["salary"].rank(
    ascending=False
)
print("\nEmployees with salary rank\n", df)

# Finding the top 3 highest paid employees
result = df.nlargest(3, "salary")
print("\nTop 3 highest paid employees\n", result)

# Find the three employees with the lowest salaries.
result = df.nsmallest(3, "salary")
print("\nFind the three employees with the lowest salaries. \n", result)

# Sort the DataFrame by salary in descending order
result = df.sort_values(
    by="salary",
    ascending=False
)
# Reset the index
result = result.reset_index(drop=True)
print(result)

# Adding a new column to the DataFrame
df["department"] = [
    "IT",
    "HR",
    "Finance",
    "Sales",
]
print("\nDataFrame with new column:\n", df)

# Adding a new column with a default value
df["company"] = "ABC Technologies"
print("\nDataFrame with new column default value:\n", df)

# Inserting a new column at a specific position
df.insert(
    1,
    "email",
    "employee@example.com"
)
print("\nDataFrame with inserted column:\n", df)

# Using the assign() method to add new columns
new_df = df.assign(
    bonus=df["salary"] * 0.10,
    total_salary=df["salary"] * 1.10
)
print("\nDataFrame with new columns using assign():\n", new_df)


# Dropping a column from the DataFrame
new_df = df.drop(columns=["age"])
print("\nDataFrame with column dropped:\n", new_df)

# Dropping a row from the DataFrame
df = df.drop_duplicates()
print("\nDataFrame with duplicate rows dropped:\n", df)


# Adding more rows to demonstrate dropping duplicates
new_rows = pd.DataFrame({
    "emp_id": [105, 106],
    "name": ["John", "Jane"],
    "age": [30, 30],
    "salary": [50000, 60000]
})
df = pd.concat([df, new_rows], ignore_index=True)
print("\nDataFrame after adding new rows:\n", df)

# Dropping duplicate rows based on a specific column
df = df.drop_duplicates(
    subset=["age"]
)
print("\nDataFrame with duplicate rows dropped based on age:\n", df)


