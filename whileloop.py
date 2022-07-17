i=1
while(i<10):
    print(i)
    i+=1
i=21
while(i<10):
    print(i)
    i+=1
else:
    print(f"{i} value is greater so will not go inside loop")

i=1
while(i<=5):
    j=1
    while(j<i+1):
        print(i,end=" ")
        j+=1
    i+=1
    print()

n=int(input("Enter the number:"))
l=len(str(n))
temp=n
sum=0
while(temp>0):
    digit=temp%10
    sum+=digit**l
    temp//=10

if sum==n:
    print("Armstrong number")
else:
    print("non- armstrong number")

i=1
while(i<=5):
    j=1
    while(j<i+1):
        print('*',end=" ")
        j+=1
    i+=1
    print()

i=1
count=1
while(i<=5):
    j=1
    while(j<i+1):
        print(count,end=" ")
        j+=1
        count+=1
    i+=1
    print()

i=1
a=65
while(i<=5):
    j=1
    while(j<i+1):
        print(chr(a),end=" ")
        j+=1
        a+=1
    i+=1
    print()
