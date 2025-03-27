import numpy as np 

# Creating Random Arrays
#Random Values Between 0 and 1 (np.random.rand())
arr = np.random.rand(50,30)
print(arr)

# 3x3 matrix with random ints from 1 to 100

random_array = np.random.randint(1,100,(4,5))
print(random_array)