#!/usr/bin/env python3

import numpy as np



# Define a function to pretty print the results
def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}')


x = np.array([1, 22.4, 5, 35, 4, 6.7, 3, 8, 40])
y = np.array([['a', 'b'], ['c', 'd'], [3, 3]])

# Creating an array:
pretty_print('My_First_Array: ', x)

# Using function ndim, shape, size and dtype for array

pretty_print('Array Dimensions: ', x.ndim)
pretty_print('Array Shape: ', x.shape)
pretty_print('Array Size: ', x.size)
pretty_print('Array Data Type: ', x.dtype)

# Creating an matrix:
pretty_print('My_First_Matrix: ', y)

# Using function ndim, shape, size and dtype for Matrix

pretty_print('Matrix Dimensions: ', y.ndim)
pretty_print('Matrix Shape: ', y.shape)
pretty_print('Matrix Size: ', y.size)
pretty_print('Matrix Data Type: ', y.dtype)

# 1 dimension array using the functions arange and rand

pretty_print('Range_Array', np.arange(1, 11))
pretty_print('Random_Array', np.random.rand(5))
# pretty_print('Random_Int_Array', np.random.randint(1, 20, 5))

# 2 dimensions matrix using the functions zeros and rand

pretty_print('Zeros_Matrix', np.zeros((3, 3)))
pretty_print('Random_Matrix', np.random.rand(3, 3))

# An array containing 20 times the value 7. Reshape it to a 4 x 5 Matrix

z = (np.ones(20) * 7)
pretty_print('My_Array', z)
pretty_print('My_Reshaped_Matrix', z.reshape(4, 5))

# Create a 6 x 6 matrix and manipulation

r = np.arange(1, 37)
rm = r.reshape(6, 6)
pretty_print('My_Reshaped_Matrix', rm)
pretty_print('First Element:', rm[0, 0])
pretty_print('Last_Two_Rows:', rm[4:6, :])
pretty_print('Two_Mid_Col_and_Rows:', rm[2:4, 2:4])
pretty_print('Sum of values for each column: ', np.sum(rm, axis=0))