import numpy as np

M=[]
N=[]

for i in range(0,3):
    t=[]
    for j in range(0,3):
        x=int(input(f"Enter the{i} Row and {j} column"))
        t.append(x)
    M.append(t)

for i in range(0,3):
    t=[]
    for j in range(0,3):
        x=int(input(f"Enter the{i} Row and {j} column"))
        t.append(x)
    N.append(t)
y=lambda: '_______________________________________________'
a=np.array(M)
print(y())
print(type(a))
print(" Matrix M:\n",a)
print(y())

b=np.array(N)
print(type(b))
print(" Matrix N:\n",b)
print(y())

print(" The sum of Matrix M&N is: \n",a+b)
print(y())
print(" The product of Matrix M&N is: \n",a*b)
print(y())


