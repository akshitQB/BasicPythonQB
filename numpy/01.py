# import numpy as np

# x = np.array([1,3,5])

# y = np.array([[1,2,3],[2,6,8]])

# z = np.array([[[1,2,4],[6,4,3]],[[3,4,3],[2,4,2]]])


# print(x)
# print(y)
# print(z)


# # Creating a 1D array
# x = np.array([1, 2, 3])

# # Creating a 2D array
# y = np.array([[1, 2], [3, 4]])

# # Creating a 3D array
# z = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# print(x)
# print(y)
# print(z)

import numpy as np

x = np.array([[[1,2,3],
               [1,2,4]],

              [[1,2,4],
               [2,4,5]]])

print(x.shape)


a1=np.zeros((3,3))
a2=np.ones((3,3))
a3=np.arange(0,10,2)

print((a1),(a2),(a3))
print((a1.shape),(a2.shape),(a3.shape))