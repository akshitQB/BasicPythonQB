import numpy as np

# numpy.newaxis method to use convet the arrays
arr=np.arange(5*5).reshape(5,5)
print(arr)

arr_5D=arr[np.newaxis,...,np.newaxis,np.newaxis]
print("After the covert in to 5d")
print(arr_5D)

arr_4d=arr[np.newaxis, ... , np.newaxis]
print("After the covert into 4d array:")
print(arr_4d)


#Using numpy.expand_dims()
x =np.zeros((3,4))
y=np.expand_dims(x,  axis=2).shape
print(y)


#Insert Many New Axes in the Array

m_array=np.arange(5*5).reshape(5,5)

newaxes=(0,3,-1)
arr_5d = np.expand_dims(m_array , axis=newaxes)
print(arr_5D.shape)

# Using numpy.reshape() for a Single axis 

arrr=np.arange(6)
arrr_reshape= arrr.reshape((2, 3))

print(arrr_reshape)


#numpy.hstack() : 


a=np.array([1,2,3])
b=np.array([4,5,6])

res = np.hstack((a,b))
print(res)

#Example : Horizontal Stacking of 2d arrays

aa=np.array([[1,2,4],[5,6,7]])
bb=np.array([[8,9,10],[11,12,13]])
ress=np.hstack((aa,bb))
print(ress)     