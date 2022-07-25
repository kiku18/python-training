print('\n----Comparing 2 integer values-----')
a= int(input("Enter the number1:"))
b= int(input("Enter the number2:"))
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

print('\n----Comparing 2 binary values-----')
try:
    p = int(input("Input binary value of p: "), 2)
    print("p (decimal format):", p)
    print("p (binary format):", bin(p))
except ValueError:
    print("Please input only binary value...")
try:
    q = int(input("Input binary value of q: "), 2)
    print("q (decimal format):", q)
    print("q (binary format):", bin(q))
except ValueError:
    print("Please input only binary value...")

print(p==q)
print(p!=q)
print(p>q)
print(p<q)
print(p>=q)
print(p<=q)

print('\n----Comparing 2 hex values-----')
try:
    p = int(input("Input hex value of p: "), 16)
    print("p (decimal format):", p)
    print("p (hex format):",hex(p))
except ValueError:
    print("Please input only hexadecimal value...")
try:
    q = int(input("Input hex value of q: "), 16)
    print("q (decimal format):", q)
    print("q (hex format):", hex(q))
except ValueError:
    print("Please input only hexadecimal value...")

print(p==q)
print(p!=q)
print(p>q)
print(p<q)
print(p>=q)
print(p<=q)

print('\n----Comparing 2 octal values-----')
try:
    p = int(input("Input octal value of p: "), 8)
    print("p (decimal format):", p)
    print("p (octal format):", oct(p))
except ValueError:
    print("Please input only octal value...")
try:
    q = int(input("Input octal value of q: "), 8)
    print("q (decimal format):", q)
    print("q (octal format):", oct(q))
except ValueError:
    print("Please input only octal value...")


print(p==q)
print(p!=q)
print(p>q)
print(p<q)
print(p>=q)
print(p<=q)
