import matplotlib.pyplot as plt
import pandas as pd

# Create a pandas DataFrame from the list
df = pd.read_csv('https://raw.githubusercontent.com/mrahmadhassankhan/datascientist_salary_analysis/main/filtered_data.csv')

# Create a box plot to find the outliers
plt.boxplot(df['salary_in_usd'])
plt.title('BoxPlot')
plt.show()

# Calculate IQR, upper limit, and lower limit
q1 = df['salary_in_usd'].quantile(0.25)
q3 = df['salary_in_usd'].quantile(0.75)
iqr = q3 - q1
upper_limit = q3 + 1.5 * iqr
lower_limit = q1 - 1.5 * iqr
# Filter the data to include only values lower than the upper limit
filtered_data = df[df['salary_in_usd'] < upper_limit]['salary_in_usd']
#After Filter 
q1_filtered = filtered_data.quantile(0.25)
q3_filtered = filtered_data.quantile(0.75)
iqr_filtered = q3 - q1
print(f"Q1:{q1}")
print(f"Q2:{filtered_data.quantile(0.50)}")
print(f"Q3:{q3}")
print(f"IQR:{iqr}")
# Finding the min, max, mean, and mode
print(f"Minimum Value: {filtered_data.min()}")
print(f"Maximum Value: {filtered_data.max()}")
print(f"Mean: {filtered_data.mean()}")
print(f"Mode: {filtered_data.mode()}")
print (f"Median : {filtered_data.median()}")
print(f"Skewness: {filtered_data.skew()}")
print(f"Standard deviation: {filtered_data.std()}")

# Plot a histogram for the filtered data
plt.hist(filtered_data, bins=10, edgecolor='black')
plt.title('Histogram of Salary')
plt.xlabel('Averge Salary')
plt.ylabel('Frequency')
plt.show()

se_df = df[df['experience_level'] == 'SE'].reset_index(drop=True)
mi_df = df[df['experience_level'] == 'MI'].reset_index(drop=True)
ex_df = df[df['experience_level'] == 'EX'].reset_index(drop=True)
en_df = df[df['experience_level'] == 'EN'].reset_index(drop=True)

se_df.to_csv('/se_data.csv', index=False)
mi_df.to_csv('/mi_data.csv', index=False)
ex_df.to_csv('/ex_data.csv', index=False)
en_df.to_csv('/en_data.csv', index=False)

# Define the column names and data values for each experience level
column_names = ['EN','MI', 'SE', 'EX']
data_values = [se_df['salary_in_usd'].mean(), mi_df['salary_in_usd'].mean(), ex_df['salary_in_usd'].mean(),en_df['salary_in_usd'].mean()]

# Create a bar plot to compare the data
plt.figure(figsize=(8, 6))
plt.bar(column_names, data_values, color=['blue', 'green', 'red','orange'])
plt.title('Comparison of Experience Levels')
plt.xlabel('Salary With Experience')
plt.ylabel('Frequency')
plt.show()
