a=30
b=40

print(a)
print(b)
print(bin(a))
print(bin(b))
print(a&b)
print(a|b)
print(a^b)
print(~a)

p=45
q=71
print(p)
print(q)
print(f"The binary value of p is", bin(p))
print(f"The hex value of p is", hex(p))
print(f"The octal value of p is", oct(p))

print(f"The binary value of q is", bin(q))
print(f"The hex value of q is", hex(q))
print(f"The octal value of q is", oct(q))

# Calculating hexadecimal values using function
print('\n----Calculating hex  values-----')
a = "B"
b = "C"
sum = hex(int(a, 16) + int(b, 16))
print(f"The sum of {a} and {b} is:", sum[2:])

a = "BE"
b = "DF"
sum = hex(int(a, 16) + int(b, 16))
print(f"The sum of {a} and {b} is:", sum[2:])
product = hex(int(a, 16) * int(b, 16))
print(f"The product of {a} and {b} is:", product[2:])

# Calculating Octal decimal values using function
print('\n----Calculating octal  values-----')
a = "123"
b = "456"
sum = oct(int(a, 8) + int(b, 8))
print(f"The sum of {a} and {b} is:", sum[2:])
product = oct(int(a, 8) * int(b, 8))
print(f"The product of {a} and {b} is:", product[2:])

a = "654"
b = "321"
c = "235"
sum = oct(int(a, 8) + int(b, 8) + int(c, 8))
product = oct(int(a, 8) * int(b, 8) * int(c, 8))
print(f"The product of {a}, {b} and {c} is:",product[3:])
print(f"The sum of {a}, {b} and {c} is:",sum[3:])


# Calculating binary values using function
print('\n----Calculating binary  values-----')
a = "110110100001"
b = "1010101101"
sum = bin(int(a, 2) + int(b, 2))
print(f"The sum of {a} and {b} is:", sum[2:])

a = "1001"
b = "101"
sum = bin(int(a, 2) + int(b, 2))
print(f"The sum of {a} and {b} is:", sum[2:])
product = bin(int(a, 2) * int(b, 2))
print(f"The product of {a} and {b} is:", product[2:])

# get value from users
print('\n----Arithmetic operation of 2 hex values-----')
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

print(f"The sum of {p} and {q} is:", (p+q))
print(f"The product of {p} and {q} is:", (p*q))
print(f"The difference of {p} and {q} is:", (p-q))

print('\n----Arithmetic operation of 2 octal values-----')
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

print(f"The sum of {p} and {q} is:", (p+q))
print(f"The product of {p} and {q} is:", (p*q))
print(f"The difference of {p} and {q} is:", (p-q))

print('\n----Arithmetic operation of 2 binary values-----')
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

print(f"The sum of {p} and {q} is:", (p+q))
print(f"The product of {p} and {q} is:", (p*q))
print(f"The difference of {p} and {q} is:", (p-q))

