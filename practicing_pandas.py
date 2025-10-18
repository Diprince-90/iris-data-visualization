import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
# Load Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("✅ Dataset loaded successfully.")
except Exception as e:
    print("❌ Error loading dataset:", e)

# Display first few rows
df.head()

# Check data types
df.dtypes

# Check for missing values
df.isnull().sum()

# Clean dataset
df.dropna(inplace=True)

# Descriptive statistics
df.describe()

# Group by species and compute mean
grouped = df.groupby('species').mean()
grouped

plt.figure(figsize=(14, 10))

# Line chart: Sepal length over index
plt.subplot(2, 2, 1)
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.title('Sepal Length Over Index')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()

# Bar chart: Average petal length per species
plt.subplot(2, 2, 2)
grouped['petal length (cm)'].plot(kind='bar', color='skyblue')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')

# Histogram: Sepal width distribution
plt.subplot(2, 2, 3)
plt.hist(df['sepal width (cm)'], bins=15, color='lightgreen', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')

# Scatter plot: Sepal length vs Petal length
plt.subplot(2, 2, 4)
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title('Sepal vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

plt.tight_layout()
plt.show()