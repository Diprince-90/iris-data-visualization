📊 Iris Dataset Analysis and Visualization
🎯 Objective
This project demonstrates how to load, explore, analyze, and visualize a dataset using Python's pandas, matplotlib, and seaborn libraries. The Iris dataset is used to showcase basic data analysis techniques and charting capabilities.

📁 Files Included
- iris_analysis.py or iris_analysis.ipynb: Main script or notebook containing all code for data loading, analysis, and visualization.
- README.md: This documentation file.

🧪 Dataset
- Source: UCI Machine Learning Repository or via sklearn.datasets.load_iris()
- - Description: The Iris dataset contains 150 samples of iris flowers with four features: sepal length, sepal width, petal length, and petal width. Each sample is labeled with one of three species: Setosa, Versicolor, or Virginica.

🔍 Tasks Completed
1. Data Loading and Exploration
- Loaded the Iris dataset using sklearn.datasets
- Converted it into a pandas DataFrame
- Displayed the first few rows using .head()
- Checked data types and missing values
- Cleaned the dataset (no missing values found)
2. Basic Data Analysis
- Computed descriptive statistics using .describe()
- Grouped data by species and calculated mean values
- Identified patterns in petal and sepal measurements across species
3. Data Visualization
Created four types of visualizations:
- 📈 Line Chart: Sepal length over sample index
- 📊 Bar Chart: Average petal length per species
- 📉 Histogram: Distribution of sepal width
- 🔬 Scatter Plot: Sepal length vs petal length, colored by species
All plots include titles, axis labels, and legends for clarity.

🛠️ Technologies Used
- Python 3.13
- pandas
- matplotlib
- seaborn
- scikit-learn

⚠️ Error Handling
- Wrapped dataset loading in a try-except block to catch file or import errors
- Checked for missing values and handled them appropriately

📌 Observations
- Setosa species consistently shows smaller petal dimensions
- Virginica has the largest petal measurements
- Clear separation between species in scatter plot suggests strong classification potential
# iris-data-visualization
