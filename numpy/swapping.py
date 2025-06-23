import numpy as np

my_arr=np.arange(12).reshape(4,3)
print("Original Array : ")
print(my_arr)


def Swap(arr,i,l):
    arr[:,[i,l]] = arr[:,[l,i]]


Swap(my_arr, 1,2)
print("After the Swapping :")
print(my_arr)