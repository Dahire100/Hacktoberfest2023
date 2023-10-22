import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
df = pd.read_csv('data.csv')

# Get some descriptive statistics of the data
df.describe()

# Create a histogram of the 'age' column
plt.hist(df['age'])
plt.xlabel('Age')
plt.ylabel('Number of people')
plt.title('Distribution of age in the dataset')
plt.show()

# Create a scatter plot of 'age' vs 'height'
plt.scatter(df['age'], df['height'])
plt.xlabel('Age')
plt.ylabel('Height')
plt.title('Relationship between age and height')
plt.show()

# Create a box plot of 'salary' by 'gender'
plt.boxplot([df[df['gender'] == 'M']['salary'], df[df['gender'] == 'F']['salary']], labels=['Male', 'Female'])
plt.xlabel('Gender')
plt.ylabel('Salary')
plt.title('Distribution of salary by gender')
plt.show()

# Group the data by 'state' and calculate the mean 'salary' for each group
mean_salaries_by_state = df.groupby('state')['salary'].mean()

# Create a bar plot of the mean salaries by state
plt.bar(mean_salaries_by_state.index, mean_salaries_by_state.values)
plt.xlabel('State')
plt.ylabel('Mean salary')
plt.title('Mean salary by state')
plt.show()
