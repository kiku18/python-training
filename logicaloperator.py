a=5
b=6
c=4

print((a>b) and (a>c))
print((b>a) and (b>c))
print((b>c) and (b>a))
print ((b>c) or (b>a))
print(not(a>b))
print(not(b>a))

print('\n----Comparing 3 octal values-----')
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

try:
    r = int(input("Input octal value of r: "), 8)
    print("r (decimal format):", r)
    print("r (octal format):", oct(r))
except ValueError:
    print("Please input only octal value...")

print((p>q) and (p>r))
print((q>p) and (q>r))
print((q>r) and (q>p))
print ((q>r) or (q>p))
print(not(p>q))
print(not(q>p))

print('\n----Comparing 3 hex values-----')
try:
    p = int(input("Input hex value of p: "), 16)
    print("p (decimal format):", p)
    print("p (hex format):", hex(p))
except ValueError:
    print("Please input only hex value...")
try:
    q = int(input("Input hex value of q: "), 16)
    print("q (decimal format):", q)
    print("q (hex format):", hex(q))
except ValueError:
    print("Please input only hex value...")

try:
    r = int(input("Input hex value of r: "), 16)
    print("r (decimal format):", r)
    print("r (hex format):", hex(r))
except ValueError:
    print("Please input only hex value...")

print((p > q) and (p > r))
print((q > p) and (q > r))
print((q > r) and (q > p))
print((q > r) or (q > p))
print(not (p > q))
print(not (q > p))

print('\n----Comparing 3 binary values-----')
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

try:
    r = int(input("Input binary value of r: "), 2)
    print("r (decimal format):", r)
    print("r (binary format):", bin(r))
except ValueError:
    print("Please input only binary value...")

print((p > q) and (p > r))
print((q > p) and (q > r))
print((q > r) and (q > p))
print((q > r) or (q > p))
print(not (p > q))
print(not (q > p))

