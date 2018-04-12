#!usr/bin/env python
import numpy as np
import sys
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([1,2,3])
b=b.reshape(3,1)
print(a.shape[0])
for i in range(0,a.shape[0]):
    for j in range(0,a.shape[1]):
        print("%s\t%s",i,(b[j]*a[i][j]))


    
    
    
