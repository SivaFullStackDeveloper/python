import numpy as np
# 1D arry
print("----1D array-----")
arr = np.array([1,2,3,6,4,5])
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.size)
print("----2D array-----")
# 2D array

array_of_2D_Array = np.array([[1,2,3],[4,5,6]])

print(array_of_2D_Array)
print(array_of_2D_Array.shape)
print(array_of_2D_Array.shape)
print(array_of_2D_Array.dtype)
print(array_of_2D_Array.size)
print("----3D array-----")
# 3D array

array_of_3D_Array =np.array([[[1,2,3]],[[5,6,3]]],dtype='int16')
print(array_of_3D_Array)
print(array_of_3D_Array.ndim)
print(array_of_3D_Array.shape)
print(array_of_3D_Array.dtype)
print(array_of_3D_Array.size)

# create zero array
zeroArray = np.zeros((6,4))
print(zeroArray)

#Ones Array (np.ones()) create array full of 1

oneAray = np.ones((2,3))
print(oneAray)

# creating full array 

full_array = np.full((4,6),7)
print(full_array)
