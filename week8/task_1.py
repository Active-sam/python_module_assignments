# Import necessary libraries
import pandas as pd
import seaborn as sns

# Load the Iris dataset from seaborn
df = sns.load_dataset('iris')

# Display the first few rows
print("First 5 rows:")
print(df.head())

# Check data types and missing values
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Clean the dataset (there are no missing values in this dataset, but we would normally clean here if needed)
