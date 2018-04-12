from collections import defaultdict
d=defaultdict(list)
f=open('C:/ajay/lab script/test1.txt','r')
data=f.read()
f.close()
for i in data.strip().split('\n'):
    j=i.strip().split('\t')
    d[j[0]].append(float(j[1]))
for i in d:
    print('%s\t%s'%(i,sum(d[i])))
    
