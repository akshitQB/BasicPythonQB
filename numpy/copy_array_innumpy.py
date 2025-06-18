import numpy as np

# arr=np.array([1,2,4,5,6,7])

# c=arr.copy()

# print("id of arr", id(arr))


#np.copy() by use of it can copy the numpy array.
arr=np.array([1.2,2.22,33.4,44.4,55.5,66.6,77.7,88.8,00.00,12.12])
# print("first array:")
# print(arr)

cparray=np.copy(arr)

# print(cparray)


#Appendig Using List Comprehensio And numpy.concaenate

arr2= np.array([1,2,3,4,5,6])

arr3=np.array([[[1,2,4],[2,4,5],[5,6,7]],
               [[11,12,13],
                [14,15,16],
                [17,18,19]]])
v_upend= [np.array([7,8]),np.array([9,10])]


combined=np.concatenate([arr]+v_upend)
# print(combined)

# print("3d arrays : ")
# new_uppend=[np.array([99,88,44])]
# new_combined=np.concatenate((arr3)+new_uppend)

# print(new_combined)

# Concatenating 1D arrays (similar to appending)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
concatenated_array = np.concatenate((array1, array2))

# Concatenating 2D arrays along a specific axis (e.g., appending rows)
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
concatenated_rows = np.concatenate((matrix1, matrix2), axis=0) # Appends rows
print(concatenated_rows)