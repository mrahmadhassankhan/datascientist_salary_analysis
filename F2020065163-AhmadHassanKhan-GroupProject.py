import matplotlib.pyplot as plt
import pandas as pd

# Create a pandas DataFrame from the list
df = pd.read_csv('/Datascientist.csv')

# Calculate IQR, upper limit, and lower limit using pandas
q1 = df['salary_in_usd'].quantile(0.25)
q3 = df['salary_in_usd'].quantile(0.75)
iqr = q3 - q1
upper_limit = q3 + 1.5 * iqr
lower_limit = q1 - 1.5 * iqr

# Filter the data to include only values lower than the upper limit
filtered_data = df[df['salary_in_usd'] < upper_limit]['salary_in_usd']

# Finding the min, max, mean, and mode
print(f"Minimum Value: {filtered_data.min()}")
print(f"Maximum Value: {filtered_data.max()}")
print(f"Mean: {filtered_data.mean()}")
print(f"Mode: {filtered_data.mode().values[0]}")
print(f"Skewness: {filtered_data.skew()}")
print(f"Standard deviation: {filtered_data.std()}")

# Plot a histogram for the filtered data
plt.hist(df['salary_in_usd'], bins=10, edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.show()

# Create a box plot for the filtered data
plt.boxplot(df['salary_in_usd'])
plt.title('BoxPlot')
plt.xlabel('Value')
plt.show()



import pandas as pd
# Replace 'your_file.csv' with the actual filename
df = pd.read_csv('/ds_salaries.csv')

se_df = df[df['experience_level'] == 'SE'].reset_index(drop=True)
mi_df = df[df['experience_level'] == 'MI'].reset_index(drop=True)
ex_df = df[df['experience_level'] == 'EX'].reset_index(drop=True)
en_df = df[df['experience_level'] == 'EN'].reset_index(drop=True)

# ouput to csv
se_df.to_csv('/se_data.csv', index=False)
mi_df.to_csv('/mi_data.csv', index=False)
ex_df.to_csv('/ex_data.csv', index=False)
en_df.to_csv('/en_data.csv', index=False)

import matplotlib.pyplot as plt
import numpy as np

# Define the column names and data values for each experience level
column_names = ['EN','MI', 'SE', 'EX']
data_values = [se_df['salary_in_usd'].mean(), mi_df['salary_in_usd'].mean(), ex_df['salary_in_usd'].mean(),en_df['salary_in_usd'].mean()]

# Create a bar plot to compare the data
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.bar(column_names, data_values, color=['blue', 'green', 'red','red'])
plt.title('Comparison of Experience Levels')
plt.xlabel('Experience Level')
plt.ylabel('Frequency')
plt.show()

# # Code Done By Aqsa
# import matplotlib.pyplot as plt

# data = [
#     2859, 18442, 22611, 24000, 32974, 33808, 38776, 40481, 45760, 45807, 45807, 46597, 46809, 49461, 50000, 50000, 52351, 52351, 54957, 55000, 58894, 62000, 62726, 63810, 63831, 65438, 65438, 66265, 68147, 68428, 69000, 70500, 71982, 72212, 75000, 75774, 76958, 77684, 78791, 79833, 80000, 84900, 87738, 88654, 91237, 91614, 93427, 99360, 100000, 104702, 105000, 108800, 109280, 110000, 115000, 115000, 116914,
# 117789, 117789, 118000, 120000, 120000, 120000, 120600, 127221, 130000, 136620, 137141, 138350, 138350, 140000, 140000, 140000, 140400, 141300, 144000, 146000, 150000, 150000, 150000, 155000, 159000, 160000, 160000, 160000, 160080, 167000, 168000, 170000, 170000, 170000, 170000, 174000, 176000, 177000, 180000, 180000, 180000, 183228, 190200, 195000, 200000, 205300, 205300, 210000, 210000, 215300, 220000, 220000, 220000, 230000, 230000, 276000, 380000, 405000,

# ]

# plt.hist(data, bins=10, edgecolor='black')
# plt.title('Histogram of Data')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.show()