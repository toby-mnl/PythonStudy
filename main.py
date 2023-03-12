import numpy as np
# if this is not working set up env again by typing python3.11 -m venv pythonlearning
# new_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(new_matrix)

"""
import matplotlib.pyplot as mapy

data1 = (3, 6, 10, 15, 25, 40)
simple_chart = mapy.subplot()
simple_chart.plot(data1)
mapy.show()

import numpy as np
np.arange

# creates a GUI
from tkinter import *

main = Tk()

main.mainloop()
"""

# import numpy as np

list1 = [10, 20, 30, 40, 50, 60]
print("\n")
print(type(list1))
print("\n")
print(list1)
print("\n")
arr1 = np.array(list1)
print("\n")
print(" This is a list converted to an array:")
print(arr1)
print("\n")
print(type(arr1))
print("\n")


print("\n")
print("This is an array created with steps\n")
print(np.arange(5, 31, 5))  # creates an array from 5 - 30 in steps of 5
print("\n")

print("\n")
# creates an array from 5 - 30 in steps of 5
print("This is an array created with steps and float\n")
print(np.arange(5, 31, 5, dtype=float))  # changes to float
print("\n")

arr2 = np.arange(5, 31, 5, dtype=float)
print("\n")
print("Dimension\n")
print(arr2.ndim)
print("\n")

arr3 = np.arange(9).reshape(3, 3)
arr5 = np.arange(1, 10).reshape(3, 3)
arr6 = np.arange(11, 20).reshape(3, 3)
arr7 = np.random.randint(10, 50)
print("This is an array matrix \n")
print(arr3)
print("\n")
print(arr3.ndim)
print("\n")
print("Matrix array\n")
print(arr5)
print("Matrix array\n")
print(arr6)
print("Random number\n")
print(arr7)
print("This is an array using ones\n")
print("np.ones(10, dtype=int)")
print(np.ones(10, dtype=int))
print("\n")
print("This is an array matrix  using ones\n")
print("np.ones((5, 5), dtype=int)")
print(np.ones((5, 5), dtype=int))
print("\n")
print(np.ones(10))
print("\n")
print(np.zeros(10))
print("\n")
print("This is an array matrix  using full\n")
print(np.full((5, 5), 23.5))
print("\n")
print("These are array matrix  using random,\n")
print(np.random.randint(5, 50, size=5))
print("\n")
print(np.random.randint(5, 25, size=(5, 5)))
print("\n")

print("complex array")
# d = np.array(1+2j, 2+4j)
print("d = np.array(1+2j, 2+4j)")

# print(d.type)
print("\n")
print("============arr3")
print("arr3 = np.arange(9).reshape(3, 3)")
print("\n")
print(arr3)
print("\n")
print("print(arr3[1:3, 1:3])")
print(arr3[1:3, 1:3])

print("List multiplication")
print("list1 = [10, 20, 30, 40, 50, 60]")
print("list2 = list1 * 2")
list1 = [10, 20, 30, 40, 50, 60]
list2 = list1 * 2
print("\n")
print(list2)

arr1 = np.array(list1)
print("\n")
print("arr1")
print(arr1)

arr2 = arr1 * 2
print("\n")
print("arr2")
print(arr2)

# this appends the double to the end so doing an array is much easier
print("appending a list")
for num in list1:
    list2.append(num*2)

print("\n")
print(list2)

print("arr7 = np.random.randint(10, 20, size=(5, 5))\n")
print("arr8 = np.random.randint(15, 25, size=(5, 5))\n")
arr7 = np.random.randint(10, 20, size=(5, 5))
arr8 = np.random.randint(15, 25, size=(5, 5))
print(arr7)
print(arr8)

print("Concatenate arrays")
arr10 = np.concatenate((arr7, arr8), axis=0)

print(arr10)
print("Hstack")
arr11 = np.hstack((arr7, arr8))
print(arr11)
np.vstack((arr7, arr8))
arr12 = np.hstack((arr7, arr8))
print(arr12)
print("Create Big Array")
big_array = np.random.randint(10, 50, size=(10, 8))
print(big_array)
arr13, arr14 = np.hsplit(big_array, 2)
print(arr13)
print(arr14)
arr15, arr16 = np.vsplit(big_array, 2)
print(arr15)
print(arr16)
# or can split into as many as you want
