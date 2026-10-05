import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Task 1: Read the CSV file into a DataFrame
df = pd.read_csv(BASE_DIR / "Cars93_missing.csv")
print(df.head())
print("Shape:", df.shape)

# Task 2: Convert a Series into a DataFrame with its index as a column
models = df["Model"]
print("Series:")
print(models.head())
models_df = models.reset_index()
print("\nDataFrame:")
print(models_df.head())

# Task 3: Change column values based on a condition
condition = df["Price"] > 30
print("\nBefore:")
print(df.loc[condition, ["Model", "Price"]].head())
df.loc[condition, "Price"] = 30
print("\nAfter:")
print(df.loc[condition, ["Model", "Price"]].head())

# Task 4: Display column names and count missing values
print("\nColumn names:")
print(df.columns.tolist())
print("\nMissing values per column:")
print(df.isna().sum())
print("\nTotal missing values:")
print(df.isna().sum().sum())


# Task 5: Swap two columns using a function
def swap_columns(dataframe, first_column, second_column):
    columns = dataframe.columns.tolist()

    first_position = columns.index(first_column)
    second_position = columns.index(second_column)

    columns[first_position], columns[second_position] = (
        columns[second_position],
        columns[first_position],
    )

    return dataframe[columns]


df_swapped = swap_columns(df, "Manufacturer", "Model")
print("\nBefore swapping:")
print(df.columns.tolist())
print("\nAfter swapping:")
print(df_swapped.columns.tolist())
# Sort columns alphabetically
df_sorted = df_swapped.sort_index(axis=1)
print("\nAlphabetically sorted columns:")
print(df_sorted.columns.tolist())

# Task 6: Remove extreme values based on Weight
lower_limit = df["Weight"].quantile(0.05)
upper_limit = df["Weight"].quantile(0.95)
keep_rows = df["Weight"].between(lower_limit, upper_limit) | df["Weight"].isna()
df_trimmed = df.loc[keep_rows].copy()
print("\nLower limit:", lower_limit)
print("Upper limit:", upper_limit)
print("Rows before:", len(df))
print("Rows after:", len(df_trimmed))
print("Rows removed:", len(df) - len(df_trimmed))

# Task 7: Replace missing Weight values with the mean
print("\nMissing weights before:")
print(df_trimmed["Weight"].isna().sum())
average_weight = df_trimmed["Weight"].mean()
df_trimmed["Weight"] = df_trimmed["Weight"].fillna(average_weight)
print("\nAverage weight:", average_weight)
print("\nMissing weights after:")
print(df_trimmed["Weight"].isna().sum())

# Task 8: Create two DataFrames from dictionaries
students_data = {
    "StudentID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
}
scores_data = {
    "StudentID": [1, 2, 3],
    "Score": [85, 90, 78],
}

students_df = pd.DataFrame(students_data)
scores_df = pd.DataFrame(scores_data)
# Merge using a shared key
merged_df = pd.merge(students_df, scores_df, on="StudentID")
print("\nMerged DataFrame:")
print(merged_df)

# # Add the Score column side by side using row indexes
combined_df = pd.concat(
    [students_df, scores_df[["Score"]]],
    axis=1,
)
print("\nCombined DataFrame:")
print(combined_df)

# Task 9: Create and save a histogram
print("\nStarting Task 9")
print("Matplotlib backend:", plt.get_backend())
df_trimmed["Weight"].hist(bins=10, edgecolor="black")
plt.title("Distribution of Car Weights")
plt.xlabel("Weight")
plt.ylabel("Number of Cars")
plt.tight_layout()
image_path = Path(__file__).with_name("weight_histogram.png")
plt.savefig(image_path)
print("Chart saved to:", image_path)
plt.show()

# Task 10: Create a correlation matrix
selected_columns = [
    "Weight",
    "Horsepower",
    "EngineSize",
    "MPG.city",
]

correlation_matrix = df_trimmed[selected_columns].corr()

print("\nCorrelation matrix:")
print(correlation_matrix.round(2))
