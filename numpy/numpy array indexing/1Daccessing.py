import numpy as np

#1D Arrays Indexing
arr = np.array([12,13,14,14,15])
print(arr[2])


#2D Arrays Indexing

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix[2,2])

#3D Arrays Indexing

cube=np.array([
    [[1,2,4],
     [2,3,4],
     [4,5,6]],

     [[10,11,12],
      [23,34,54],
      [56,44,67]]])
     
print(cube[0,1,1])

# Slicing Arrays 

arr1=np.array([0,1,2,3,4,5])
# print(arr1[1:3])

#Slicing Multidimensional Arrays : 

arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2[0:2,1:3])


#Boolean Indexing

arr3=np.array([10,15,16,26,24,45,65,75])

print(arr3[arr3<20])

#We can also use logical operators like and or not here ..above

#Fancy Indexing : 

arr4 =np.array([2,3,5,6,8,4,7,9,0,53,6,7,95])
indices=[0,4,6]
print(arr4[indices])


# Integer Array Idexing

arr5=np.array([1,2,3,4,5])
print(arr[[0,1,3]])



#Ellipsis(..)in  indexing

cube1=np.random.rand(4,4,4)

#Using np.newaxis to Add New Dimensions.

arr6=np.array([1,2,3])
print(arr6[:,np.newaxis])

#Modifying Array Elements 
arr7 = np.array([1,2,3,4])
arr[0:2] = 99
print(arr)