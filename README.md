# NHANES_Visualization
Data Analysis and Visualization with NHANES Data
This repository contains Python scripts for analyzing and visualizing data from the NHANES 2015-2016 dataset. The analyses and visualizations performed include various aspects such as relationships between body measurements, demographic factors, and blood pressure readings. The following key components are included:

1. Scatter Plots and Joint Plots
Regression Plot: Visualizes the relationship between 'BMXLEG' and 'BMXARML' without fitting a regression line.
Joint Plot (Histogram): Displays the joint distribution of 'BMXLEG' and 'BMXARML' with histograms on the margins.

2. Facet Grids
Facet Grid by Gender: Scatter plots of 'BMXLEG' vs. 'BMXARML', differentiated by gender.
Facet Grid by Race/Ethnicity and Gender: Scatter plots of 'BMXLEG' vs. 'BMXARML' grouped by race/ethnicity and gender.

3. Correlation Analysis
Correlation Coefficients: Computes and prints the correlation between 'BMXLEG' and 'BMXARML' for females and males separately.
Blood Pressure Correlation: Analyzes and prints the correlation between systolic and diastolic blood pressure measurements.

4. Educational and Marital Status Analysis
Crosstab Analysis: Creates and normalizes a crosstab of education level and marital status.
Group-by Analysis: Computes and prints the proportions of various educational and marital status combinations, grouped by gender.

5. Data Filtering and Conditions
Filtering Data: Demonstrates how to filter the dataset based on conditions such as waist circumference and leg length.

6. Violin Plots
Educational Attainment and Age: Visualizes age distribution by educational attainment and gender.
BMI by Age Group: Shows BMI distribution by age group and gender.

7. Multivariate Normal Distribution
Distribution Plots: Generates histograms and scatter plots to visualize joint and marginal distributions of two variables sampled from a multivariate normal distribution.

Prerequisites
Python 3.x
Pandas
NumPy
Matplotlib
Seaborn
SciPy

Usage
Clone this repository: git clone https://github.com/yourusername/your-repository.git
Navigate to the directory: cd your-repository
Ensure all dependencies are installed.
Run the scripts to generate visualizations and analyses from the NHANES dataset.
Feel free to modify and adapt the scripts to suit your own data analysis needs.
