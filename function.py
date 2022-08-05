def square(a):
    print(a**2)
def cube(a):
    print(a ** 3)

n=int(input(" Enter the number:"))
square(f'The square of the given number is:',n)
cube(f'The cube of the given number is:',n)
square(n+5)
cube(n+5)

a=int(input(" Enter the nmumber1:"))
b=int(input(" Enter the nmumber2:"))
c=int(input(" Enter the nmumber3:"))

def largestofthreenumbers(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>z and y>z:
        print(y)
    else:
        print(z)

largestofthreenumbers(a,b,c)

def logincheck(username,password):
    if username=="admin" and password=="admin":
        return"valid login"
    elif username!="admin" and password=="admin":
        return"invalid username"
    elif username=="admin" and password!="admin":
        return"invalid password"
    else:
        return "Both are incorrect"

a=logincheck('admin','admin')
print(a)

b=logincheck('admin','admin123')
print(b)

def checkoddnumber(n):

    '''

    :param n: we need to pass number as arguments
    :return: It will return whether number is odd or not.
    Date         modification date   modified by    version
    12-12-2012   12-12-2012          Kishore        1.0
    14-12-2012   14-12-2012          kumar          1.1

    '''

    if n%2==1:
        return True
    else:
        return False

O=checkoddnumber(15)
if O:
    print('odd number')
else:
    print('even number')
print(checkoddnumber.__doc__)


