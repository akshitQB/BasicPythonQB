import numpy 


x = numpy.array([[1,2],[4,5]])
y = numpy.array([[7,8],[9,10]])

print("The  elemnt wise qure root is :")
print(numpy.sqrt(x))

print("The sumation of all matrix element is :")
print(numpy.sum(x))

print("The column wise summation of all matrix l")
print(numpy.sum(y,axis=0))

#Using sum (axis=1) print sumation of each column of matrix :
print("The column wise summation of all matrix is :")
print(numpy.sum(y,axis=1))

# Using "T" to transpose the matrix 
print("The transpose of given matrix is :")
print(x.T)



