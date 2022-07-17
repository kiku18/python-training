def square(num1):
    return num1**2
def cube(num1):
    return num1**3
def add(num1,num2):
    return num1+num2
Y=lambda r:3.14*(r**2)
Z=lambda a:a**4
a=square(4)
b=square(6)
c=square(7)
d=square(9)
e=cube(4)
f=cube(6)
g=cube(7)
h=cube(9)
print(" The square  of a,b,c & d is: \n",a,b,c,d)
print(" The cube  of e,f,g & h is: \n",e,f,g,h)
print(Y(2))
print(Y(4))
print(Y(12))

print(Z(21))
print(Z(24))
print(Z(23))

O1=add(4,9)
O2=add(2,3)
print(O1,O2)

L1=[4,6,7,9]
m1=map(square,L1)
print(list(m1))
m2=map(cube,L1)
print(list(m2))
m3=map(add,L1,L1)
print(list(m3))
m4=map(Y,L1)
print(list(m4))
m5=map(Z,L1)
print(list(m5))

def agecheck(num1):
    if num1<18:
        return'Below 18'
    elif num1>=18 and num1<=25:
        return'Between 18 to 25'
    elif num1 > 25 and num1 <= 50:
        return 'Between 25 to 50'
    else:
        return'Above 50'

a=agecheck(94)
a1=agecheck(47)
a2=agecheck(12)
a3=agecheck(24)

print (" The age check   of a is:",a)
print (" The age check   of a1 is:",a1)
print (" The age check   of a2 is:",a2)
print (" The age check   of a3 is:",a3)

L2=[94,47,12,24,]
m6=map(agecheck,L2)
print(list(m6))

def tempcheck(num1):
    if num1<0:
        return'Cold temperature'
    elif num1>=0 and num1<=15:
        return'Medium temperature'
    elif num1 > 15 and num1 <= 45:
        return 'High temperature'
    else:
        return'Very high temperature'

a=tempcheck(-12)
a1=tempcheck(-3)
a2=tempcheck(12)
a3=tempcheck(17)
a4=tempcheck(27)
a5=tempcheck(47)
a6=tempcheck(42)

print (" The temp check   of a is:",a)
print (" The temp check   of a1 is:",a1)
print (" The temp check   of a2 is:",a2)
print (" The temp check   of a3 is:",a3)
print (" The temp check   of a3 is:",a4)
print (" The temp check   of a3 is:",a5)
print (" The temp check   of a3 is:",a6)

L3=[-12,-3,12,17,27,47,42]
m7=map(tempcheck,L3)
print(list(m7))

m7=list(map(tempcheck,L3))
print('Total count of recorded Cold temperature is:',m7.count('Cold temperature'))
print('Total count of recorded Medium temperature is:',m7.count('Medium temperature'))
print('Total count of recorded High temperature is:',m7.count('High temperature'))
print('Total count of recorded Very high temperature is:',m7.count('Very high temperature'))










