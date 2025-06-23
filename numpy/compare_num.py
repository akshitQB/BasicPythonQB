import numpy as np

an_array=np.array([1,2],[3,4])
another_array = np.array([1,2] , [3,4])

comparison = an_array == another_array
equal_arryas = comparison.all()

print(equal_arryas)



arr2D = np.array([[11,12,11,11],
                  [13,11,12,11],
                  [16,11,12,11],
                  [11,11,12,11]])

unique=np.unique(arr2D , return_inverse=True) 

print('Unique Rows:', unique,sep='\n')

