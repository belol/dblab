import numpy as np
f=open('C:/ajay/lab script/a.txt','r')
data=f.read()
f.close()
k=[]
data1=data.split('\n')
for i in data1:
    j=i.split(' ')
    j=map(float,j)
    k.append(j)
matrix=np.array(k)
a=matrix
b=matrix
K=[i for i in range(3)]
L=[i for i in range(3)]
for i in range(3):
    for j in range(3):
        for k in K:
            print('%s\t%s'%((i,k),a[i][j]))
for j in range(3):
    for k in range(3):
        for i in L:
            print('%s\t%s'%((i,k),b[j][k]))
        
