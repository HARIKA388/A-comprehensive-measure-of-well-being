# Find null values in each column of X
print(X.isnull().sum())

# Fill null values with the mean of each column
X = X.fillna(X.mean())

# Verify that there are no null values left
print(X.isnull().sum())