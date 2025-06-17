import numpy as np

#T use for the Trsnform the array in to row to colum and colum to row
# arr=np.array([[1,2,3],
#      [4,5,6]])
# print(arr.T)

# print(t)
# arr =np.array([[1,2,4],[1,3,5]])

# print(arr.shape)
# print(arr.dtype)
# print(arr.ndim)

# Element-wise addition
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)  # Output: [5 7 9]

# Matrix multiplication
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))



np.arange(1, 20 , 2, 
          dtype = np.float32)