import matplotlib.pyplot as plt

# Line chart (for the sake of demo, we simulate a time trend by using index as the x-axis)
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x=df.index, y="sepal_length")
plt.title("Line Chart: Sepal Length Over Index (Simulated Time)")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.show()

# Bar chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="species", y="petal_length")
plt.title("Average Petal Length per Species")
plt.ylabel("Petal Length")
plt.xlabel("Species")
plt.show()

# Histogram: Distribution of sepal length
plt.figure(figsize=(8, 5))
sns.histplot(df['sepal_length'], bins=20, kde=True)
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="species")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend()
plt.show()
