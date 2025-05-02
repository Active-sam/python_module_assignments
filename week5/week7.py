# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Task 1: Load and Explore the Dataset
# ----------------------------

# Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Display the first few rows
print("First 5 rows:")
print(df.head())

# Check data types and missing values
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Clean the dataset (no missing values in Iris dataset, but here's how you would handle them)
# df = df.dropna() or df.fillna(value)

# ----------------------------
# Task 2: Basic Data Analysis
# ----------------------------

# Basic statistics
print("\nSummary statistics:")
print(df.describe())

# Group by species and compute mean
grouped_means = df.groupby('species').mean()
print("\nAverage values by species:")
print(grouped_means)

# Interesting finding example:
print("\nObservation:")
print("Setosa has the shortest average petal length, Virginica has the longest.")

# ----------------------------
# Task 3: Data Visualization
# ----------------------------

# Set style
sns.set(style="whitegrid")

# Line chart (not applicable for Iris directly, so we simulate a time index for demo)
df_line = df.copy()
df_line["index"] = df_line.index
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_line, x="index", y="sepal_length")
plt.title("Line Chart: Sepal Length Over Index (Simulated Time)")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.show()

# Bar chart: average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="species", y="petal_length")
plt.title("Average Petal Length per Species")
plt.ylabel("Petal Length")
plt.xlabel("Species")
plt.show()

# Histogram: distribution of sepal length
plt.figure(figsize=(8, 5))
sns.histplot(df['sepal_length'], bins=20, kde=True)
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: sepal length vs petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="species")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend()
plt.show()
