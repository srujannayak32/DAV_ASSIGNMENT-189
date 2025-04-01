import numpy as np
import pandas as pd

# Load the dataset (Update the path if needed)
df = pd.read_csv(r'C:\Users\sruja\Downloads\DAV_ASSIGNMENT-189\Electric Vehicle Population Data.csv')

# Display dataset info
print("DataFrame Info:")
print(df.info())

### ---------------- UNIT 1: NUMPY OPERATIONS ---------------- ###

# Convert DataFrame to NumPy Array
data_array = df.to_numpy()
print("\nNumpy Array:\n", data_array[:5])  # Display first 5 rows

# Data Types in NumPy
print("\nData Types:", data_array.dtype)

# Creating an array
arr1 = np.array([1, 2, 3, 4, 5])
print("\nCreated Array:", arr1)

# Indexing and Slicing
print("\nFirst Element:", data_array[0][0])
print("\nFirst 5 Rows:", data_array[:5])

# Reshaping Array
reshaped_arr = data_array[:10].reshape(5, -1)  # Reshaping the first 10 rows
print("\nReshaped Array:\n", reshaped_arr)

# Concatenation & Splitting
arr2 = np.arange(10).reshape(2, 5)
arr3 = np.arange(10, 20).reshape(2, 5)
concatenated_arr = np.concatenate((arr2, arr3), axis=0)
print("\nConcatenated Arrays:\n", concatenated_arr)

split_arr = np.split(concatenated_arr, 2)
print("\nSplit Arrays:", split_arr)

# Universal Functions (Square Root)
sqrt_arr = np.sqrt(concatenated_arr)
print("\nSquare Root:\n", sqrt_arr)

# Aggregations
print("\nSum:", concatenated_arr.sum())
print("\nMean:", concatenated_arr.mean())

# Broadcasting
broadcasted_sum = arr2 + np.array([1, 2, 3, 4, 5])  # Adding a row vector
print("\nBroadcasted Sum:\n", broadcasted_sum)

# Boolean Masking
bool_mask = concatenated_arr > 5
print("\nBoolean Mask:\n", bool_mask)

# Fancy Indexing (Fixed)
indices = np.array([0, 1])  # Safe indexing
print("\nFancy Indexing:", arr1[indices])

# Fast Sorting
sorted_arr = np.sort(arr1)
print("\nSorted Array:", sorted_arr)

### ---------------- UNIT 2: PANDAS OPERATIONS ---------------- ###

# Series Object
series_example = df['Make']
print("\nSeries Object:\n", series_example.head())

# DataFrame Object
print("\nDataFrame Sample:\n", df.head())

# Indexing and Selecting
print("\nSelecting Column (Make):\n", df['Make'].head())

# Universal Functions
df['Electric Range'] = df['Electric Range'].fillna(0)  # Handling NaN before applying functions
print("\nElectric Range Mean:", df['Electric Range'].mean())

# Index Alignment
df['New Column'] = df['Electric Range'] * 2  # Creating a new column
print("\nNew Column Sample:\n", df[['Electric Range', 'New Column']].head())

# Handling Missing Data
df = df.apply(lambda col: col.fillna("Missing") if col.dtype == "object" else col.fillna(0))


# Hierarchical Indexing
df.set_index(['State', 'County'], inplace=True)
print("\nHierarchical Indexing:\n", df.head())

### ---------------- UNIT 3: COMBINING DATASETS ---------------- ###

# Reset index for combining
df.reset_index(inplace=True)

# Creating sample DataFrames for merging
df1 = df[['Make', 'Model', 'Electric Range']].head(5)
df2 = df[['Make', 'Model', 'Base MSRP']].head(5)

# Concat
concat_df = pd.concat([df1, df2], axis=1)
print("\nConcatenated DataFrame:\n", concat_df)

# Append
appended_df = pd.concat([df1, df2], ignore_index=True)
print("\nAppended DataFrame:\n", appended_df)

# Merge
merged_df = pd.merge(df1, df2, on=['Make', 'Model'], how='inner')
print("\nMerged DataFrame:\n", merged_df)

# Joins
joined_df = df1.join(df2, lsuffix='_left', rsuffix='_right')
print("\nJoined DataFrame:\n", joined_df)

# Aggregation and Grouping
grouped_df = df.groupby('Make').agg({'Electric Range': 'mean'})
print("\nGrouped DataFrame:\n", grouped_df.head())

# Pivot Table
pivot_table = df.pivot_table(values='Electric Range', index='Make', aggfunc='mean')
print("\nPivot Table:\n", pivot_table.head())
