

### Import Libraries


# Commented out IPython magic to ensure Python compatibility.
# Import Libraries
# Importing Numpy & Pandas for data processing & data wrangling
import numpy as np
import pandas as pd

# Importing  tools for visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Import the 'calendar' and 'datetime' module
import calendar
import datetime as dt

# Library used for ignore warnings
import warnings
warnings.filterwarnings('ignore')
# %matplotlib inline

"""### Dataset Loading"""

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/Apaulgithub/oibsip_task2/main/Unemployment%20in%20India.csv")

"""### Dataset First View"""

# Dataset First Look
# View top 5 rows of the dataset
df.head()

"""### Dataset Rows & Columns count"""

# Dataset Rows & Columns count
# Checking number of rows and columns of the dataset using shape
print("Number of rows are: ",df.shape[0])
print("Number of columns are: ",df.shape[1])

"""### Dataset Information"""

# Dataset Info
# Checking information about the dataset using info
df.info()

"""#### Duplicate Values"""

# Dataset Duplicate Value Count
dup = df.duplicated().sum()
print(f'number of duplicated rows are {dup}')

"""#### Missing Values/Null Values"""

# Missing Values/Null Values Count
df.isnull().sum()

# Visualizing the missing values
# Checking Null Value by Plotting Heatmap
sns.heatmap(df.isnull(), cbar=False)

"""### What did i know about the dataset?

* The Unemployment dataset consists of Region, Date, Unemployment Rate etc. for Indian states.
* There are 768 rows and 7 columns provided in the data.
* 27 duplicate rows present in the dataset.
* 28 Null values present in each of the columns available in dataset.

## ***2. Understanding The Variables***
"""

# Dataset Columns
df.columns

# Dataset Describe (all columns included)
df.describe(include= 'all').round(2)

"""### Check Unique Values for each variable."""

# Check Unique Values for each variable.
for i in df.columns.tolist():
  print("No. of unique values in",i,"is",df[i].nunique())

"""## ***3. Data Wrangling***

### Data Wrangling Code
"""

# Rename the columns of the DataFrame
df.columns = ['States', 'Date', 'Frequency', 'Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate', 'Region']

# Convert the 'Frequency' column to a categorical data type
df['Frequency'] = df['Frequency'].astype('category')

# Convert the 'Region' column to a categorical data type
df['Region'] = df['Region'].astype('category')

# Convert the 'Date' column to datetime format, specifying 'dayfirst' to handle date formats with day first
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Extract the month from the 'Date' column and create a new 'Month' column
df['Month'] = df['Date'].dt.month

# Create a new 'Month_int' column by converting the 'Month' column to integers, handling missing values
df['Month_int'] = df['Month'].apply(lambda x: int(x) if pd.notna(x) else x)

# Drop the 'Month' column from the DataFrame
df.drop(columns='Month', inplace=True)

# Lets create a copy of the dataset for the data of during lockdown period
df_ld = df.copy()

# Drop all the missing values from 'df' dataset
df=df.dropna()

# Define a date range mask to filter rows where 'Date' falls within the range of before lockdown period
mask = (df['Date'] >= '2019-05-31') & (df['Date'] <= '2020-03-31')

# Use the mask to select and keep only the rows that meet the date range criteria
df = df.loc[mask]

# Define a date range mask to filter rows where 'Date' falls within the range of during lockdown period
mask = (df_ld['Date'] >= '2020-04-30')

# Use the mask to select and keep only the rows that meet the date range criteria
df_ld = df_ld.loc[mask]

"""### What all manipulations have you done and insights you found?

- Rename the columns name of the DataFrame.
- Convert Frequency and Region to categorical data type.
- Convert the 'Date' column to datetime format, extract month from the 'Date' column and create a new 'Month_int' column by converting the 'Month' column to integers.
- Drop the 'Month' column from the DataFrame.
- Create a copy of the dataset for the data of during lockdown period.
- Drop all the missing values from before lockdown dataset.
- Take the range of date from 2019-05-31 to 2020-03-31 as before lockdown period and date after 2020-04-30 as during lockdown period.

## ***4. Data Vizualization, Storytelling & Experimenting with charts : Understand the relationships between variables***

#### Chart - 1 : Region Wise Estimated Unemployment Rate
"""

# Chart - 1 Bar plot visualization code for Region wise Estimated Unemployment Rate before and during lockdown

# Create a figure with two subplots side by side.
plt.figure(figsize=(14, 5))

# Subplot 1: Estimated Unemployment Rate Before Lockdown
plt.subplot(1, 2, 1)

# Create a bar plot using Seaborn to visualize the Estimated Unemployment Rate before lockdown.
sns.barplot(x='Region', y='Estimated Unemployment Rate', data=df)

# Set labels and title for the first subplot.
plt.xlabel("Region", fontsize=10)
plt.ylabel('Estimated Unemployment Rate', fontsize=10)
plt.title('Estimated Unemployment Rate Before Lockdown', fontsize=12)

# Subplot 2: Estimated Unemployment Rate During Lockdown
plt.subplot(1, 2, 2)

# Create a bar plot for the Estimated Unemployment Rate during lockdown.
sns.barplot(x='Region', y='Estimated Unemployment Rate', data=df_ld)

# Set labels and title for the second subplot.
plt.xlabel("Region", fontsize=10)
plt.ylabel('Estimated Unemployment Rate', fontsize=10)
plt.title('Estimated Unemployment Rate During Lockdown', fontsize=12)

# Display the subplots side by side.
plt.show()

"""##### What is/are the insight(s) found from the chart?

From the above charts we got to know that the Estimated Unemployment Rate are much higher during the lockdown time compare to the before lockdown.

#### Chart - 2 : Swarm Plot for State Wise Estimated Unemployment Rate
"""

# Chart - 2 Swarm plot visualization code for State Wise Estimated Unemployment Rate before and during lockdown.

# Create a figure with two subplots side by side.
plt.figure(figsize=(25, 8))

# Subplot 1: State Wise Estimated Unemployment Rate Before Lockdown
plt.subplot(1, 2, 1)

# Set the title for the first subplot.
plt.title("State Wise Estimated Unemployment Rate Before Lockdown", fontsize=16)

# Create a swarm plot to visualize the Estimated Unemployment Rate before lockdown.
sns.swarmplot(y="States", x='Estimated Unemployment Rate', data=df, size=8)

# Set labels for the first subplot.
plt.xlabel("Estimated Unemployment Rate", fontsize=16)
plt.ylabel("States", fontsize=16)

# Subplot 2: State Wise Estimated Unemployment Rate During Lockdown
plt.subplot(1, 2, 2)

# Set the title for the second subplot.
plt.title("State Wise Estimated Unemployment Rate During Lockdown", fontsize=16)

# Create a swarm plot to visualize the Estimated Unemployment Rate during lockdown.
sns.swarmplot(y="States", x='Estimated Unemployment Rate', data=df_ld, size=8)

# Set labels for the second subplot.
plt.xlabel("Estimated Unemployment Rate", fontsize=16)
plt.ylabel("States", fontsize=16)

# Display the subplots side by side.
plt.show()

"""##### What is/are the insight(s) found from the chart?

From the above charts we got to know that, in terms of State Wise Estimated Unemployment Rate, Puducherry and Jharkhand comes in top during the lockdown time. And before the lockdown period, Haryana and Tripura both are in top position for the Estimated Unemployment Rate.

#### Chart - 3 : Bar Plot for State Wise Estimated Unemployment Rate
"""

# Chart - 3 Bar for visualization code for State wise Estimated Unemployment Rate before and during lockdown time.

# Create a figure with two subplots side by side.
plt.figure(figsize=(25, 8))

# Subplot 1: Estimated Unemployment Rate Before Lockdown
plt.subplot(1, 2, 1)

# Set the title for the first subplot.
plt.title("Estimated Unemployment Rate Before Lockdown", fontsize=16)

# Create a bar plot to visualize the Estimated Unemployment Rate before lockdown.
sns.barplot(data=df.sort_values(by='Estimated Unemployment Rate', ascending=False), x="States", y="Estimated Unemployment Rate")
plt.xticks(rotation=90)
plt.xlabel('States', fontsize=16)
plt.ylabel('Estimated Unemployment Rate', fontsize=16)

# Subplot 2: Estimated Unemployment Rate During Lockdown
plt.subplot(1, 2, 2)

# Set the title for the second subplot.
plt.title("Estimated Unemployment Rate During Lockdown", fontsize=16)

# Create a bar plot to visualize the Estimated Unemployment Rate during lockdown.
sns.barplot(data=df_ld.sort_values(by='Estimated Unemployment Rate', ascending=False), x="States", y="Estimated Unemployment Rate")
plt.xticks(rotation=90)
plt.xlabel('States', fontsize=16)
plt.ylabel('Estimated Unemployment Rate', fontsize=16)

# Display the subplots side by side.
plt.show()

"""##### What is/are the insight(s) found from the chart?

From the above charts we got to know that, states like: Tripura, Haryana and Himachal Pradesh are in top on before lockdown time for Estimated Unemployment Rate. But, Puducherry, Jharkhand and Bihar comes in top during the lockdown time for Estimated Unemployment Rate.

#### Chart - 4 : State Wise Estimated Employed Workforce
"""

# Chart - 4 Bar plot visualization code for state wise Estimated Employed Workforce

# Create a figure with two subplots side by side.
plt.figure(figsize=(25, 8))

# Subplot 1: Estimated Employed Workforce Before Lockdown
plt.subplot(1, 2, 1)

# Set the title for the first subplot.
plt.title("Estimated Employed Workforce Before Lockdown", fontsize=16)

# Create a bar plot to visualize the Estimated Employed Workforce before lockdown.
sns.barplot(data=df.sort_values(by='Estimated Employed', ascending=False), x="States", y="Estimated Employed")

# Rotate x-axis labels for better readability.
plt.xticks(rotation=90)

# Set labels for the first subplot.
plt.xlabel('States', fontsize=16)
plt.ylabel('Estimated Employed', fontsize=16)

# Subplot 2: Estimated Employed Workforce During Lockdown
plt.subplot(1, 2, 2)

# Set the title for the second subplot.
plt.title("Estimated Employed Workforce During Lockdown", fontsize=16)

# Create a bar plot to visualize the Estimated Employed Workforce during lockdown.
sns.barplot(data=df_ld.sort_values(by='Estimated Employed', ascending=False), x="States", y="Estimated Employed")

# Rotate x-axis labels for better readability.
plt.xticks(rotation=90)

# Set labels for the second subplot.
plt.xlabel('States', fontsize=16)
plt.ylabel('Estimated Employed', fontsize=16)

# Display the subplots side by side.
plt.show()

"""##### What is/are the insight(s) found from the chart?

From the above charts we got to know that, states like: Uttar Pradesh, Maharashtra and West Bengal are in top on before lockdown time for Estimated Employed Workforce. Again, Uttar Pradesh, Maharashtra and West Bengal are in top also during the lockdown time for Estimated Employed Workforce.

#### Chart - 5 : State Wise Estimated Labour Participation Rate
"""

# Chart - 5 Bar plot visualization code for state wise Estimated Labour Participation Rate

# Create a figure with two subplots side by side.
plt.figure(figsize=(25, 8))

# Subplot 1: Estimated Labour Participation Rate Before Lockdown.
plt.subplot(1, 2, 1)

# Set the title for the first subplot.
plt.title("Estimated Labour Participation Rate Before Lockdown", fontsize=16)

# Create a bar plot to visualize the Estimated Labour Participation Rate before lockdown.
sns.barplot(data=df.sort_values(by='Estimated Labour Participation Rate', ascending=False), x="States", y="Estimated Labour Participation Rate")

# Rotate x-axis labels for better readability.
plt.xticks(rotation=90)

# Set labels for the first subplot.
plt.xlabel('States', fontsize=16)
plt.ylabel('Estimated Labour Participation Rate', fontsize=16)

# Subplot 2: Estimated Labour Participation Rate During Lockdown.
plt.subplot(1, 2, 2)

# Set the title for the second subplot.
plt.title("Estimated Labour Participation Rate During Lockdown", fontsize=16)

# Create a bar plot to visualize the Estimated Labour Participation Rate during lockdown.
sns.barplot(data=df_ld.sort_values(by='Estimated Labour Participation Rate', ascending=False), x="States", y="Estimated Labour Participation Rate")

# Rotate x-axis labels for better readability.
plt.xticks(rotation=90)

# Set labels for the second subplot.
plt.xlabel('States', fontsize=16)
plt.ylabel('Estimated Labour Participation Rate', fontsize=16)

# Display the subplots side by side.
plt.show()

"""##### What is/are the insight(s) found from the chart?

From the above charts we got to know that, states like: Telangana, Tripura, Meghalaya and Assam are in top for Estimated Labour Participation Rate, on before lockdown time. And Meghalaya, Telangana, Tripura and Andhra Pradesh are in top, during the lockdown time for Estimated Labour Participation Rate.

#### Chart - 6 : Correlation Heatmap
"""

# Create new DataFrames
df1_stats = df[['Estimated Unemployment Rate','Estimated Employed', 'Estimated Labour Participation Rate']]

df2_stats = df_ld[['Estimated Unemployment Rate','Estimated Employed', 'Estimated Labour Participation Rate']]

# Chart - 6 Correlation heatmap visualization code

# Create a figure with two subplots side by side.
plt.figure(figsize=(25, 8))

# Subplot 1: Correlations of Variables Before Lockdown.
plt.subplot(1, 2, 1)

# Set the title for the first subplot.
plt.title("Correlations of Variables Before Lockdown", fontsize=16)

# Create a heatmap to visualize the correlations between variables in df1_stats.
sns.heatmap(df1_stats.corr(), annot=True, linewidths=0.1, fmt='.2f', square=True)

# Subplot 2: Correlations of Variables During Lockdown.
plt.subplot(1, 2, 2)

# Set the title for the second subplot.
plt.title("Correlations of Variables During Lockdown", fontsize=16)

# Create a heatmap to visualize the correlations between variables in df2_stats.
sns.heatmap(df2_stats.corr(), annot=True, linewidths=0.1, fmt='.2f', square=True)

# Display the subplots side by side.
plt.show()

"""##### What is/are the insight(s) found from the chart?

From the above heatmaps we got to know that, Estimated Unemployment Rate and Estimated Employed are negatively highly correlated for both, before and during lockdown time.

# **Conclusion**

In this data science project, we embarked on a comprehensive analysis of the unemployment rate, a critical economic indicator, with a particular focus on the unprecedented challenges brought about by the Covid-19 pandemic. Our exploratory data analysis yielded valuable insights that shed light on the dynamics of unemployment in India.

1. We observed a significant surge in the Estimated Unemployment Rate during the Covid-19 lockdown, underscoring the profound impact of the pandemic on the labor market.

2. Our state-wise analysis highlighted the states that bore the brunt of this crisis. Puducherry and Jharkhand stood out with the highest Estimated Unemployment Rates during the lockdown, while Haryana and Tripura held the top positions before the pandemic.

3. The transition from pre-lockdown to lockdown was marked by shifts in the states with the highest Estimated Unemployment Rates. Tripura, Haryana, and Himachal Pradesh led the rankings before the lockdown, whereas Puducherry, Jharkhand, and Bihar claimed the top spots during the lockdown.

4. Notably, states like Uttar Pradesh, Maharashtra, and West Bengal exhibited consistent challenges in maintaining high levels of Estimated Employed Workforce both before and during the lockdown.

5. Our analysis of Estimated Labour Participation Rate identified states that showed resilience in labor force participation. Telangana, Tripura, Meghalaya, and Assam topped the list before the lockdown, while Meghalaya, Telangana, Tripura, and Andhra Pradesh excelled during the lockdown.

6. We uncovered a robust negative correlation between Estimated Unemployment Rate and Estimated Employed, highlighting the intricate relationship between these two crucial employment indicators, both before and during the lockdown.

This project not only provided valuable insights into the economic impact of the Covid-19 pandemic but also demonstrated the power of data science in understanding and addressing complex socio-economic challenges. The findings contribute to informed decision-making and policy formulation, and underscore the importance of data-driven approaches in mitigating the effects of future crises.
"""
