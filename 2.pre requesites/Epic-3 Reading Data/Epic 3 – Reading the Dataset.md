Epic 3 – Reading the Dataset

Objective



The purpose of Epic 3: Reading the Dataset is to load the Human Development Index (HDI) dataset into Python so it can be explored, analyzed, and used for building a machine learning model.



The dataset is stored as a CSV (Comma-Separated Values) file and is read using the Pandas library.



Step 1: Import the Pandas Library



Pandas is a Python library used for handling and analyzing data.

&#x20;

&#x20; **import pandas as pd**

Step 2: Read the Dataset



Use the read\_csv() function to load the dataset.



Example:



df = pd.read\_csv("HDI.csv")



or



df = pd.read\_csv("/content/HDI.csv")



if using Google Colab.



Here:



pd → Alias for the Pandas library.

read\_csv() → Reads a CSV file.

df → A DataFrame that stores the dataset in a table format.

Step 3: Display the Dataset



View the first five rows of the dataset.



print(df.head())



Example output:



Country	Life Expectancy	Mean Years Schooling	Expected Years Schooling	GNI per Capita	HDI

India	67.2	6.7	12.6	6590	0.633

Norway	82.5	13.0	18.1	66894	0.961

Japan	84.8	13.4	15.2	42274	0.925

Step 4: Check Dataset Information



Use the info() function.



df.info()



This displays:



Number of rows

Number of columns

Column names

Data types

Missing values



Example:



**<class 'pandas.core.frame.DataFrame'>**

**Entries: 193**

**Columns: 6**

**Step 5: Check Dataset Shape**



**Find the number of rows and columns.**



**print(df.shape)**



Example:



(193, 6)



Meaning:



193 rows

6 columns

Step 6: Display Column Names

print(df.columns)



Example output:



**Index(\['Country',**

&#x20;      **'Life Expectancy',**

&#x20;      **'Mean Years Schooling',**

&#x20;      **'Expected Years Schooling',**

&#x20;      **'GNI per Capita',**

&#x20;      **'HDI'],**

&#x20;     **dtype='object')**

**Step 7: Check Missing Values**

**print(df.isnull().sum())**



This shows how many missing values are present in each column.



Example:



Country                      0

Life Expectancy              0

Mean Years Schooling         2

Expected Years Schooling     1

GNI per Capita               0

HDI                          0

Step 8: View Statistical Summary

print(df.describe())



This provides statistics such as:



Count

Mean

Standard Deviation

Minimum value

Maximum value

25%, 50%, and 75% percentiles



These statistics help understand the overall distribution of the numerical data.



Why is Epic 3 Important?



Reading the dataset is the first step in any machine learning project because it:



Loads the data into Python.

Verifies that the dataset has been imported correctly.

Displays the structure and contents of the dataset.

Identifies missing values or incorrect data types.

Helps understand the data before preprocessing and model training.

Workflow of Epic 3

Start

&#x20;  │

&#x20;  ▼

Import Pandas Library

&#x20;  │

&#x20;  ▼

Load HDI CSV Dataset

&#x20;  │

&#x20;  ▼

Create DataFrame (df)

&#x20;  │

&#x20;  ▼

Display First Rows (head)

&#x20;  │

&#x20;  ▼

Check Dataset Information (info)

&#x20;  │

&#x20;  ▼

Check Shape and Columns

&#x20;  │

&#x20;  ▼

Check Missing Values

&#x20;  │

&#x20;  ▼

Display Statistical Summary

&#x20;  │

&#x20;  ▼

Dataset Ready for Preprocessing

