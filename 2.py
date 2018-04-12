#!usr/bin/env python
import numpy as np
c=np.array([0,0,0])
import numpy as np
import sys
for line in sys.stdin:
    line=line.strip()
    words=line.split('\t')
    word=words[0]
    word=int(word)
    count=words[0]
    count=int(count)
    for i in range(1,3):
        if word==0:
            c[word]=c[word]+count
        elif word==1:
            c[word]=c[word]+count
        elif word==2:
            c[word]=c[word]+count
for i in range(0,c.shape):
    print(c[i])
    
