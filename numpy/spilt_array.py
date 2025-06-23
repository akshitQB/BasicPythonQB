import numpy as np

array=np.arange(6)

result= np.split(array,6)

print("Array : ")
print(array)

print("\nResult after numpy.split():")
print(result)

#Unequal Spliting of arrays using

arrays =np.arange(13)

results=np.array_split(arrays,4)

print("Array:")
print(arrays)

print("After the uequal spliting : ")
print(results)

# Splitting NumPy 2D Arrays 

arr1=np.array([[3,2,1],[8,9,7],[5,6,0]])

determines = np.split(arr1, 3 , axis=1)

print("2D Array:")
print(arr1)

print("\nResult after numpy.split() along axis=1:")
print(determines)

# Vertical Splitting of Arrays using 



# Creating an example matrix
matrix = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9],
                            [10, 11, 12]])

# Vertical splitting into 2 subarrays along axis=0
result = np.vsplit(matrix, 2)

print("Matrix:")
print(matrix)
print("\nResult after numpy.vsplit():")
print(result)

# Horizontal ( column-wise ) Splitting of Arrays : using numpy.hsplit()
# arr_= np.array([1,2,3,4],
#                [5,6,7,8],
#                [9,10,11,12])

# Horizontal splitting into 2 subarrays along axis = 1
# output=np.hsplit(arr_, 2)

# print("2D Array:")
# print(arr_)

# print("\nResult after numpy.hsplit():")
# print(output)

#6 Splitting Arrays Along the third Axis using numpy.dsplit():

org_3d_array=np.arange(24).reshape((2,3,4))
print("Original Array is : ")
print(org_3d_array)

# Splitting along axis=2 (third axis)
resultt=np.dsplit(org_3d_array, 2)

print("\nresult after numpy.dsplit():")
print(resultt)