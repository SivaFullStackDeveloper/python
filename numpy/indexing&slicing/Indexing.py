import numpy as np

# zero-based indexing
arr = np.array([1, 2, 3, 4, 5]) 
print(arr[0]) # 1
print(arr[2])
print(arr[-2])

# 2D Array Indexing (Rows & Columns)
arr_random = np.random.randint(1,100,(3,3))
print(arr_random)
print(arr_random[2,1])