# Strings
data = 'Stephane Nigaba'
print(data[0])
print(len(data))
print(data)

# Numbers
value = 123.1
print(value)
value = 10
print(value)

# Boolean
a = True
b = False
print(a, b)

a, b, c = 1, 2, 3
print(a, b, c)

# No value
a = None
print(a)

value = 99
if value == 99:
    print ('That is fast')
elif value >= 200:
    print ('That is too fast')
else:
    print ('That is safe')

# For-Loop
for i in range(10):
    print (i)
    print()


# While-Loop
i = 0
while i < 10:
    print (i)
    i += 1

# data structures
#tuple
a = (1, 2, 3)
print (a)
print()

#list
mylist = [1, 2, 3]
print("Zeroth Value:", mylist[0])
mylist.append(4)
print("List Length:", len(mylist))
for value in mylist:
    print (value)
print()

# dictionary
mydict = {'a': 1, 'b': 2, 'c': 3}
print("A value: ", mydict['a'])
mydict['a'] = 11
print("A value: ", mydict['a'])
print("Keys: ",  mydict.keys())
print("Values: ", mydict.values())
for key in mydict.keys():
    print (mydict[key])

# functions
# Sum function
def mysum(x, y):
    return x + y
# Test sum function
result = mysum(1, 3)
print()
print(result)


#arrays
# define an array
import numpy
mylist = [1, 2, 3]
myarray = numpy.array(mylist)
print()
print(myarray)
print(f"Array shape: {myarray.shape}")


# access array values
import numpy
mylist = [[1, 2, 3], [3, 4, 5]]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)
print("First row: ", myarray[0])
print("Last row: ", myarray[-1])
print("Specific row and col: ", myarray[0, 2])
print("Whole col: ", myarray[:, 2])
print()

# arithmetic
import numpy
myarray1 = numpy.array([2, 2, 2])
myarray2 = numpy.array([3, 3, 3])
print("Array 1: ", myarray1)
print("Array 2: ", myarray2)
print("Addition: ", (myarray1 + myarray2))
print("Multiplication: ", (myarray1 * myarray2))
print("Division: ", (myarray1 / myarray2))
print()

# plotting graphs
# basic line plot
import matplotlib.pyplot as plt
import numpy
myarray = numpy.array([1, 2, 100])
plt.plot(myarray)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

# basic scatter plot
import matplotlib.pyplot as plt
import numpy
x = numpy.array([1, 2, 9])
y = numpy.array([2, 4, 6])
plt.scatter(x,y)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()

# series
import numpy
import pandas
myarray = numpy.array([1, 2 ,3])
rownames = ['a', 'b','c']
myseries = pandas.Series(myarray, index=rownames)
print(myseries)
print()

#accessing data in a series
print(myseries['a'])
print()

# dataframe
import numpy
import pandas
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)
print()

#indexing data using column names
print("method 1:")
print("one column: ", mydataframe['one'])
print("method 2:")
print("one column: ", mydataframe.one)
print()



