x=lambda: print('Hello')
y=lambda: '_____'


a=lambda a:a*2
print(a(2))
print(a(5))
print(a(4))
print(y())
b=lambda a:a**2
print(b(2))
print(b(5))
print(b(4))
print(y())
c= lambda a,b: a+b
print(c(2,3))
print(c(5,4))
print(c(4,4))
print(y())

d=lambda i=2, j=2, k=4:(i+j)*k
print(d(4,2,3))
print(d(4,7))
print(d(14))
print(d())
print(y())

e=lambda r=0:(3.14)*(r**2)
print(e(2))
print(e(4))
print(e(7))
print(e())
print(y())

print("Addition Values")
add = lambda x = 10, y = 20, z = 30 : x + y + z
print(add(12, 14, 16)) # 12 + 14 + 16
print(add(75, 126)) # 75 + 126 + 30
print(add(222)) # 222 + 20 + 30
print(add()) # 10 + 20 + 30
print(y())

print("Multiplication Values")
multi = lambda x = 10, y = 20, z = 30 : x * y * z
print(multi(2, 4, 5)) # x = 2, y = 4, z = 5
print(multi(100, 22)) # x = 100, y = 22, z = 30
print(multi(9)) # x = 9, y = 20, z = 30
print(multi()) # 10 * 20 * 30
print(y())

double = lambda x: x * 2

print(double(5))







