L1=[1,2,3,4,5,6]
L2=['A','B','C','d','e','f']
print(L1)
print(L2)
O=zip(L1,L2)
print(O)
O1=list(zip(L1,L2))
print(O1)

O2=set(zip(L1,L2))
print(O2)

O3=dict(zip(L1,L2))
print(O3)

city=['Chennai','Abc','XYZ','abcz']
pincode=[600078,60081,60089,60081]
O=list(zip(city,pincode))
O1=set(zip(city,pincode))
O2=dict(zip(city,pincode))

print(O)
print(O1)
print(O2)

city={'Chennai','Abc','XYZ','Abc'}
pincode={600078,60081,60089,60081}
O=list(zip(city,pincode))
O1=set(zip(city,pincode))
O2=dict(zip(city,pincode))

print(O)
print(O1)
print(O2)

a,b=zip(*O) # unzip(give * before the variable)
print(a)
print(b)

