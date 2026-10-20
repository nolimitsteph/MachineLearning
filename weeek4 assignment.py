# from pathlib import Path
# import numpy
# import matplotlib.pyplot as plt
# from pandas import read_csv
#
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# # `data` renamed to `pima`
# pima = read_csv("diabetes.csv", names=names)
#
#
# # 1. Mean of a list, compared with numpy.mean
# def my_mean(values):
#     return sum(values) / len(values)
#
#
# print("my_mean:   ", my_mean([1, 2, 3, 4]))
# print("numpy.mean:", numpy.mean([1, 2, 3, 4]))
# # 2. Summarisiing the DataFrame
# print(pima.describe())
# # 3. Scatter plot of age against mass (BMI)
# plt.scatter(pima['age'], pima['mass'], alpha=0.5)
# plt.xlabel('age (years)')
# plt.ylabel('mass (BMI)')
# plt.title('Age vs. mass in the Pima dataset')
# plt.show()
#
# # Bonus: mass has zeros, which are really missing values. Compare the means.
# print("mean mass with zeros:   ", pima['mass'].mean())
# print("mean mass without zeros:", pima.loc[pima['mass'] > 0, 'mass'].mean())

#Code for the small tasks in
from pathlib import Path
import numpy
import pandas
from pandas import read_csv
#Part 1: Python basics
value = 250
if value == 99:
    print('That is fast')
elif value > 200:
    print('That is too fast')     # now this branch runs
else:
    print('That is safe')

mydict = {'a': 1, 'b': 2, 'c': 3}
mydict['d'] = 4
print("Keys:", list(mydict.keys()))


def mymul(x, y):
    return x * y

print("mymul(3, 4) =", mymul(3, 4))
#Part 2: NumPy
a = numpy.array([[1, 2, 3], [4, 5, 6]])
print("a[:, 1] =", a[:, 1])
print("a.T =\n", a.T)

# Part 4: Pandas
mydataframe = pandas.DataFrame(
    numpy.array([[1, 2, 3], [4, 5, 6]]),
    index=['a', 'b'],
    columns=['one', 'two', 'three'],
)
mydataframe['four'] = [7, 8]
print(mydataframe)
print(mydataframe.loc['a'])

#Part 5: Loading data
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv("diabetes.csv", names=names)
print(data.head())
print(data.dtypes)