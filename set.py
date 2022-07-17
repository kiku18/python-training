S1=set()
S2={1,2,3}
print(type(S1))
print(type(S2))
S3={1,2,3,4,5,'a',1,2}
print(S3)
S4={9,7,2,1,'a','z',99}
print(S4)
S5={1,2,3,4,5}
print(S5)
S5.add(9)
print(S5)
S5.add(3)
print(S5)
S5.add(33)
print(S5)
S6=set('Hello')
print(S6)
S7={'Hello'}
print(S7)
S7={1,2,3,4}
S7.add(9)
print(S7)
S7.discard(3)
print(S7)
S7.clear()
print(S7)
S8={7,9,12,13,1,2}
print(S8)
#S8.update((12,13),(21,23))
print(S8)


S1={1,2,3,4,5,7,8}
S2={1,2,4,5,9,7}
S3={1,4,3,2,9,7}

S4=S1.union(S2)
S5=S1.intersection(S2)
S6=S1.difference(S2)
S7=S1.symmetric_difference(S2)
print(S4)
print(S5)
print(S6)
print(S7)

S8=S1|S2
print(S8)
S9=S1&S2
print(S9)

set1={1,2,3}
set2={5,6,7}
print(set1)
print(set2)
set1.update(set2)
print(set1)
print(set2)













