
L=[1,2,3,4,5]
print(L)
print(type(L))
L1=[[1,2,3],[4,5,6],[7,8,9]]
print(L1)
print(L1[1])
L2=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12],[13,14,15]]]
print(L2)
print(L2[1][2])

import numpy as np
L1=[1,2,3,4,5,6]
print(L1)
print(type(L1))
L2=[[1,2,3],[4,5,6],[7,8,9]]
print(L2)
print(type(L2))
L3=[[[1,2],[2,3]],[[4,5],[5,6]],[[6,7],[7,8]]]
print(type(L3))
print(L3)
a= np.array(L1)
print(type(a))
print(a)
b=np.array(L2)
print(type(b))
print(b)
c=np.array(L3)
print(type(c))
print(c)
L4=[[1,2,3],[4,5,6],[7,8,9]]
print(L4)
o=[]
for a in range(len(L4)):
    t=[]
    for b in range(len(L4[a])):
        t.append((L4[a][b])+2)
    o.append(t)
print(o)
d=np.array(L4)
print(d+2)
