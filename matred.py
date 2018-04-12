from collections import defaultdict
f=open('C:/ajay/lab script/matrix.txt','r')
data=f.read()
f.close()
d=defaultdict(list)
for i in data.strip().split('\n'):
    j=i.strip().split('\t')
    d[j[0]].append(float(j[1]))
for i in d:
    print('%s\t%s'%(i,sum(d[i])))
