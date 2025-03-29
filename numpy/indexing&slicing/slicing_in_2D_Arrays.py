# 2d array slicing


import numpy as np

arr = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)


print(arr)

print(arr[:,1])# prints(coloms if the : is first)
print(arr[1,:])

print(arr[1:3,0:2])