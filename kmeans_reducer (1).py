#!usr/bin/env python
'''reducer.py'''

import sys
import os
data = [[1,1],[1.5,2],[3,4],[5,7],[3.5,5],[4.5,5],[3.5,4.5]]


dict1 = {}
dict2 = {}

old_centroid = []

iteration = 1
for line in sys.stdin :
    line = line.strip()
    line = line.split('\t')
    old_centroid.append([float(line[0]),float(line[1])])
    if(dict1.has_key(line[0])):
        if(float(dict1[line[0]]) > float(line[2])) :
            dict1[line[0]] = line[2]
            dict2[line[0]] = line[1]

    else :
        dict1[line[0]] = line[2]
        dict2[line[0]] = line[1]
    iteration = iteration + 1

new_centroid = []

sum1 = []
sum2 = []
cnt1 = 0
cnt2 = 0

for i in range(0,len(dict2)) :
    if int(dict2.values()[i]) == 1 :
        sum1.append(data[i])
        cnt1 = cnt1+1
    else :
        sum2.append(data[i])
        cnt2 = cnt2+1

val1 = 0
val2 = 0
for i in range(0,len(sum1)) :
    val1 = val1+sum1[i][0]
    val2 = val2+sum1[i][1]
val1 = val1/cnt1
val2 = val2/cnt1
new_centroid.append([val1,val2])

val1 = 0
val2 = 0
for i in range(0,len(sum2)) :
    val1 = val1+sum2[i][0]
    val2 = val2+sum2[i][1]
val1 = val1/cnt2
val2 = val2/cnt2
new_centroid.append([val1,val2])

dist = []

for i in range(0,2) :
        val = 0
        for j in range(0,2):
                val = val + (new_centroid[i][j]-old_centroid[i][j])**2
        val = val ** (1/2)
        dist.append(val)

flag = 0
for i in range(0,2):
        if(dist[i]<0.5) :
                flag = flag+1
os.remove("input.txt")
f = open('input.txt','a+')
for i in range(0,2) :
   f.write('%s %s\n' %(new_centroid[i][0],new_centroid[i][1]))

if flag < 2 :
        os.system("cat input.txt | python mapper.py | python reducer.py")
