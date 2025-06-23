import numpy as np

#By using of zeros can create a arrays fullfill with zeros.
arr_zero= np.zeros((3,4))
print(arr_zero)

arr_one = np.ones((2,2))
print(arr_one)

# FULL Array :-  by use of np.full can fullfill with given parameter 

arr_full= np.full((3,3),2)
print(arr_full)


#Creating an Arrays with the different values

arr_diff= np.random.rand(3,3)
print(arr_diff)

#Creating an Array with the intger values .. (29-> is the starting range and 40 is ending point of the values)

arr_int=np.random.randint(29,40,size=(3,3))
print(arr_int)

#Creating Arrays with a Range of Values :(first to is rage and third is the gap)
arr_rang = np.arange(0,10,3)
print(arr_rang)

#Generate an array with a specific number of values evenly spaced .
arr_linespace=np.linspace(0,5,5)
print(arr_linespace)

#Identity and Diagonal Matrices :-

identity_arr=np.eye(3)
print(identity_arr)


i_arr=np.eye(2,5)
print(i_arr)


