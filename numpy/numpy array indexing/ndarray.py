import numpy as np

arr=np.array([[1,2,4],[4,5,6]])
arr1=np.array([[[1,2,2,3],[1,2,4,5],[7,8,9,6]],
               [[1,2,3,4],[1,35,6,2],[2,4,5,6]]])
print("shape:",arr1.shape)
print("Dimensions:",arr1.ndim)
print("Size:",arr1.size)
print("Data type:",arr.dtype)
print("Item size:",arr1.itemsize)

arr=np.linspace(0,1 ,  num=25).reshape(5,5)
print(arr)