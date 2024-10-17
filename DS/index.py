# Step 1: Import the required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load the Iris dataset
from sklearn.datasets import load_iris

# Loading Iris dataset
iris_dataset = load_iris()
iris_df = pd.DataFrame(iris_dataset['data'], columns=iris_dataset['feature_names'])
iris_df['species'] = iris_dataset['target']

# Change the species label to the species name form
iris_df['species']=iris_df['species'].apply(lambda x: iris_dataset['target_names'][x])

# Step 3: Understanding the data
print("Dataset size:", iris_df.shape)
print("\nDataset columns:", iris_df.columns)
print("\nData type:", iris_df.dtypes)
print("\n5 Top data:")
print(iris_df.head())

# Descriptive statistics
print("\nDescriptive statistics:")
print(iris_df.describe())

# Step 4: Data Visualization
# Visualization of feature distribution
sns.pairplot(iris_df, hue='species')
plt.show()

# Boxplot to see distribution and outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris_df.drop(columns='species'))
plt.title('Feature Distribution and Outliers')
plt.show()

# Visualization of correlation between features with heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(iris_df.drop(columns='species').corr(),annot=True, cmap='coolwarm')
plt.title('Correlation Between Features')
plt.show()
