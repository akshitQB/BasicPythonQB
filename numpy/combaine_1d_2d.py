import numpy as np

#Sometime we need to combine 1D and 2D arrays and display their Element.
#numpy.nditer()
num_1d = np.arange(5)
print("One Dimenional array:")
print(num_1d)

num_2d = np.arange(10).reshape(2,5)
print("\nTwo dimensional array:")
print(num_2d)

#Combine 1-D and 2-D arrays and display their element using numpy.nditer()

for a,b in np.nditer([num_1d,num_2d]):
    print("%d:%d" % (a,b),)



