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
print(sum[2:])

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


