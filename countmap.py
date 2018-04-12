f = open('C:/ajay/lab script/test.txt', 'r')
data = f.read()
f.close()
# data=sys.stdin
# d=data.split(' ')
for i in data.strip().split(' '):
    print('%s\t%s'%(i,1))
