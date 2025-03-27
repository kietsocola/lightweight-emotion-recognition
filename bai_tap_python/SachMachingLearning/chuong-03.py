# Strings
data = 'hello world'
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

# Multiple Assignment
a, b, c = 1, 2, 3
print(a, b, c)

# No value
a = None
print(a)

value = 99
if value == 99:
    print('That is fast')
elif value > 200:
    print('That is too fast')
else:
    print('That is safe')

# For-Loop
for i in range(10):
    print(i)

# While-Loop
i = 0
while i < 10:
    print(i)
    i += 1

a = (1, 2, 3)
print(a)

# Lists
mylist = [1, 2, 3]
print(f"Zeroth Value: {mylist[0]}")
mylist.append(4)
print(f"List Length: {len(mylist)}")
for value in mylist:
    print(value)

# Dictionaries
mydict = {'a': 1, 'b': 2, 'c': 3}
print(f"A value: {mydict['a']}")
mydict['a'] = 11
print(f"A value: {mydict['a']}")
print(f"Keys: {list(mydict.keys())}")
print(f"Values: {list(mydict.values())}")
for key in mydict.keys():
    print(mydict[key])

# Sum function
def mysum(x, y):
    return x + y

# Test sum function
result = mysum(1, 3)
print(result)

# Define an array with NumPy
import numpy as np
mylist = [1, 2, 3]
myarray = np.array(mylist)
print(myarray)
print(myarray.shape)

# Access values in a NumPy array
mylist = [[1, 2, 3], [3, 4, 5]]
myarray = np.array(mylist)
print(myarray)
print(myarray.shape)
print(f"First row: {myarray[0]}")
print(f"Last row: {myarray[-1]}")
print(f"Specific row and col: {myarray[0, 2]}")
print(f"Whole col: {myarray[:, 2]}")

# Arithmetic with NumPy
myarray1 = np.array([2, 2, 2])
myarray2 = np.array([3, 3, 3])
print(f"Addition: {myarray1 + myarray2}")
print(f"Multiplication: {myarray1 * myarray2}")

# Basic line plot
import matplotlib.pyplot as plt
myarray = np.array([1, 2, 3])
plt.plot(myarray)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()

# Basic scatter plot
x = np.array([1, 2, 3])
y = np.array([2, 4, 6])
plt.scatter(x, y)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()

# Series with Pandas
import pandas as pd
myarray = np.array([1, 2, 3])
rownames = ['a', 'b', 'c']
myseries = pd.Series(myarray, index=rownames)
print(myseries)
print(myseries[0])
print(myseries['a'])

# DataFrame with Pandas
myarray = np.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pd.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)

print("Method 1:")
print(f"One column: {mydataframe['one']}")
print("Method 2:")
print(f"One column: {mydataframe.one}")
