L=[]
print(type(L))
L1= [11,2,13,54,5,66,77,8]
print(L1)
print(L1[0])
print(L1[1])
print(L1[2])
print(L1[4])
print(L1[-2])
print(L1[-1])
print(sum(L1))
print(max(L1))
print(min(L1))
print(len(L1))
(L1.sort())
print(L1)

(L1.sort(reverse=True))
print(L1)
print(L1[:])
print(L1[2:])
print(L1[:3])
print(L1[2:5])

L=[]
L.append(8)
print(L)
L.append(81)
print(L)
L.append(94)
print(L)
L.insert(1,111)
print(L)
L.insert(0,99)
print(L)
L2=[8,4,2,1]
print(L2)
L1.extend(L2)
print(L1)
L3=[1,2,3,4]
print(L3)
L3.pop()
print(L3)
L3.pop()
print(L3)
L3.remove(1)
print(L3)

L1=[1,2,3]
print(dir(L1))
L2=L1.copy()
print(L2)
L4=[1,2,3,1,2,4,8]
print(L4.count(1))
print(L4.count(4))
L5=['A','B','C',9,8,7,2]
print(L5.index('C'))
print(L5.index(9))
t1=(1,2,3,4)
print(t1[2])
print(type(t1))















