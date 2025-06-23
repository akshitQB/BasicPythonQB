import numpy as np

a =np.ma.array([1,2,3], mask=[0,1,0])
b=np.ma.array([4,5,6], mask=[0,0,1])

res=np.ma.concatenate([a,b])
print(res)

# Example : we are concatenating two 2D masked arrays along axis=1 , which means horizontally

aa=np.ma.array([[1,2],[3,4]], mask=[[0,1],[0,0]])
bb=np.ma.array([[5,6],[7,8]] , mask=[[0,0],[1,0]])

ress=np.ma.concatenate([aa,bb],axis=1)
print(ress)

#Numpy dstack() method 

a1 = np.array([1, 2, 3])
b1 = np.array([4, 5, 6])

result = np.dstack((a1, b1))

print(result)
print("Shape:", result.shape)