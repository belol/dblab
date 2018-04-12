#!usr/bin/env python
'''mapper.py'''

import sys

data = [[1,1],[1.5,2],[3,4],[5,7],[3.5,5],[4.5,5],[3.5,4.5]]

iteration = 1

for line in sys.stdin :
    line = line.strip()
    line = line.split(' ')
    for j in range(0,len(data)) :
        sum1 = 0
        for k in range(0,len(data[j])) :
            sum1 = sum1+((data[j][k] - float(line[k]))**2)
        sum1 = sum1 ** 0.5
        print('%s\t%s\t%s' %(j,iteration,sum1))
    iteration = iteration + 1


