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

print(np.diag([1, 2, 3, 4]))
arr=(np.diag([1, 2, 3, 4]))
print(arr[::-1, ::-1])

import numpy

print("Printing Original array")

sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

print (sampleArray)

print("Array after deleting column 2 on axis 1")

sampleArray = numpy.delete(sampleArray , 1, axis = 1)

print (sampleArray)

arr = numpy.array([[10,10,10]])

print("Array after inserting column 2 on axis 1")

sampleArray = numpy.insert(sampleArray , 1, arr, axis = 1)

print (sampleArray)

# example of replacing array elements as above
import numpy

print("Printing Original array")

A1 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
A2 = numpy.array([[10,11,12],[13,14,15],[16,17,18]])
print (A1)
print (A2)

print("Array after deleting column 2 on axis 1")

A1 = numpy.delete(A1 , 1, axis = 1)

print (A1)

arr = numpy.array([[11,14,17]])

print("Array after inserting column 2 on axis 1")

A1 = numpy.insert(A1 , 1, arr, axis = 1)

print (A1)

# list to array(interview qn)

l1= [[1,2,3],[4,5,6],[7,8,9]]
l2= [[10,11,12],[13,14,15],[16,17,18]]
print(l1)
print(l2)
M1=numpy.array(l1)
M2=numpy.array(l2)
print(M1)
print(M2)
o=[]

for a in range (3):
    x = []
    for b in range(3):
        if b%2==1:
            x.append(l2[a][b])
        else:
            x.append(l1[a][b])
    o.append(x)
print(o)
a=np.array(o)
print(a)

def comment():
    '''
#b%2==0{0th column and 2nd column chnages in the 1st matrix}
#b%2==1{1st column alone changes in 1st matrix}
#b==0 changes 0th column in 1st matrix
#b==1 changes  1st column in 1st matrix
#b==2 changes 2nd column in 1st matrix

    '''

print(comment.__doc__)