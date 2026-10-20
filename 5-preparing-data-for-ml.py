# Rescale data (between 0 and 1)
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer, Binarizer

filename = 'pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values


# separate array into input and output components
print("Separate the array into input and output components")
X = array[:,0:8]
Y = array[:,8]
"""nderstanding X = array[:, 0:8]
This extracts the first eight columns as the input features, which will be used to make predictions.
- : before the comma means select all rows.
- 0:8 after the comma means select columns starting at index 0 up to, but not including, index 8.
The selected features are preg, plas, pres, skin, test, mass, pedi, and age.

Understanding Y = array[:, 8]
This extracts the ninth column, at index 8, as the output or target.
- : means all rows.
- 8 means column index 8, which is the class column.
In this dataset, 0 represents no diabetes and 1 represents diabetes.
Code	What it selects
array[100:200]	Rows 100–199, all columns
array[100:201]	Rows 100–200, all columns
array[100:201, :]	Rows 100–200, explicitly all columns
array[100:201, 0:8]	Rows 100–200, first 8 columns
array[100:201, 8]	Rows 100–200, only the class column
array[100, :]	Just row 100, all columns
array[:, 0]	All rows, only the preg column
array[:, 0:3]	All rows, first 3 columns
array[:10]	First 10 rows
array[-10:]	Last 10 rows
3. Understanding the syntax
The general pattern is:
array[rows, columns]

"""

scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)
# summarize transformed data
set_printoptions(precision=3)


#standardize the data
print("Standarze the data")
# separate array into input and output components
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
# summarize transformed data
set_printoptions(precision=3)
print(rescaledX[0:5,:])
print()

# normalise data
print("Normalise data")
# separate array into input and output components
scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)
# summarize transformed data
set_printoptions(precision=3)
print(normalizedX[0:5,:])
print()

# separate array into input and output components
print("Binarise the data")
binarizer = Binarizer(threshold=0.0).fit(X)
binaryX = binarizer.transform(X)
# summarize transformed data
set_printoptions(precision=3)
print(binaryX[0:5,:])
print()



