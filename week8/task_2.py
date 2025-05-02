# Basic statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# Group by 'species' and compute the mean of numerical columns
grouped_means = df.groupby('species').mean()
print("\nAverage values by species:")
print(grouped_means)

# Observation: 
# The Iris-setosa species has the smallest petal length on average,
# while the Iris-virginica species has the largest petal length.
