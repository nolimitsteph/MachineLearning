# View first 20 rows
from pandas import read_csv, set_option

filename = "pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
peek = data.head(20)
print(peek)
print()


# dimensions of the data
print("dimensions of the data")
shape = data.shape
print(shape)
print()

#data type for each attribute
print("data type for each attribute")
types = data.dtypes
print(types)
print()


#descriptive statistics
print("descriptive statistics")
set_option('display.width', 100)
set_option('display.precision', 3)
description = data.describe()
print(description)
print()


# class distribution
class_counts = data.groupby('class').size()
print("class counts")
print(class_counts)
print()

# correlation between attributes
print("correlation between attributes")
set_option('display.width', 100)
set_option('display.precision', 3)
correlations = data.corr(method='pearson')
print(correlations)
print()

#skew of univariate distributions
skew = data.skew()
print("Skew of univariate distributions")
print(skew)
print()

