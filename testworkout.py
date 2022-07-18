a=5
b=6

print(a,b)
c=a
a=b
b=c
print(a,b)

a = 30
b = 45
a = a ^ b;
b = a ^ b;
a = a ^ b;
print ("After Swapping: a = ", a, " b =", b)

p = 25
q = 30
p, q = q, p
print("p =", p)
print("q =", q)

import numpy as np
a=[1,2,3,4]
a1=np.array(a)
print(a)
print(a1)
b=[[1,2,3],[4,5,6],[7,8,9]]
b1=np.array(b)
print(b)
print(b1)
c=[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]
c1=np.array(c)
print(c)
print(c1)

import numpy as np
a=np.arange(8)
print(a)
print(np.arange(10))
print(np.arange(15))

