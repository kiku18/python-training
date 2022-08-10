try:
    print(a)
except NameError:
    print('Variable is not defined')
finally:
    print('I will always run')

a=5
b=0
try:
    c=a/b
except ZeroDivisionError:
    print('number is not divisible by 0')
    c= 'undefined'
finally:
    print(c)

c=14
d='xyz'
try:
    a=c/d
except TypeError:
    print('Invalid operation')

try:
    a=int(input(" Enter the number1:"))
    b=int(input(" Enter the number2:"))
    c=a+b
except ValueError:
    print('Enter integer value alone dont enter other values')


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print(x)
except:
  print("An exception occurred")

# Program to depict else clause with try-except
# Function which returns a/b

def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)

# Driver program to test above function

AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# import module sys to get the type of exception

import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)
