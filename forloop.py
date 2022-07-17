'''
for a in range(5):
    print(a)
print('----')
for b in range(0,11):
    print(b)
print('-----')
for c in range(0,11,2):
    print(c)
print('----')
for d in 'human':
    print(d)
print('----')
for e in range(5):
    print(e,end="")
print()
for f in range(0,11):
    print(f,end="")
print('-------')
for g in range(0,11,2):
    print(g,end="")
print('-------')
for i in 'human':
    print(i,end="")
print('-----')


for a in range(5):
    print(f"----------Student information {a+1}-------------")
    m1 = int(input("Enter the mark1"))
    m2 = int(input("Enter the mark2"))
    m3 = int(input("Enter the mark3"))
    m4 = int(input("Enter the mark4"))
    m5 = int(input("Enter the mark5"))

    if m1 < 35 or m2 < 35 or m3 < 35 or m4 < 35 or m5 < 35:
        print(" The student had failed")
    else:
        total = m1 + m2 + m3 + m4 + m5
        Avg = total / 5
        if total > 450:
            print(f"the student total ={total}")
            print(f"the average of the student ={Avg}")
            print('grade A')
        elif total < 350 and total >= 300:
            print(f"the student total ={total}")
            print(f"the average of the student ={Avg}")
            print('grade B')
        elif total < 300 and total >= 275:
            print(f"the student total ={total}")
            print(f"the average of the student ={Avg}")
            print('grade C')
        else:
            print(f"the student total ={total}")
            print(f"the average of the student ={Avg}")
            print('grade D')

for a in range(1,11):
    for b in range(1,11):
        print(a,end="  ")
    print()
print('______________')
for a in range(1,11):
    for b in range(1,11):
        print(b,end="  ")
    print()
print('_________________')
for a in range(1,11):
    for b in range(1,11):
        print(a*b,end="  ")
    print()


r= int(input("Enter the number of rows"))
c= int(input("Enter the number of columns"))
for a in range(1,r+1):
    for b in range(1,c+1):
            print(f"{a}*{b}={a*b}",end=" ")
            print()



for a in range (1,6):
    for b in range(1,a+1):
        print(a,end= " ")
    print()

for a in range (1,6):
    for b in range(1,a+1):
        print(b,end=" ")
    print()

for a in range (1,6):
    for b in range(1,a+1):
        print(a*b,end=" ")
    print()

for a in range (1,6):
    for b in range(1,a+1):
        print('*',end=" ")
    print()

count=1
for a in range (1,6):
    for b in range(1,a+1):
        print(count,end=" ")
        count+=1
    print()

v=65
for a in range (1,6):
    for b in range(1,a+1):
        print(chr(v),end=" ")
        v+=1
    print()

s=42
for a in range (1,6):
    for b in range(1,a+1):
        print(chr(s),end=" ")
    print()

count=1
for a in range (1,6):
    for b in range(1,a+1):
        if count%2==0:
            print('even',end=" ")
        else:
            print('odd',end=" ")
        count+=1
    print()

count=1
for a in range (1,6):
    for b in range(1,a+1):
        if count%2==0:
            print('even',end=" ")
        else:
            print(count,end=" ")
        count+=1
    print()


count=1
for a in range (1,6):
    for b in range(1,a+1):
        if count%2==0:
            print('even',end=" ")
        else:
            print('odd',end=" ")
    count += 1
    print()

count=1
for a in range (1,6):
    for b in range(1,a+1):
        if a%2==0:
            print('*',end=" ")
        else:
            print(count,end=" ")
        count+=1
    print()


#For loop with list& set

L=[]
S=set()
d=dict()
for a in range (1,100):
    L.append(a**2)
    S.add(a**2)
    d[a]=a**2
print(L)
print(S)
print(d)

L1=[]
S1=set()
d1=dict()

for a in range(1,100):
    if a%2==0:
        L1.append('even')
        S1.add('even')
        d1[a]='even'
    else:
        L1.append('odd')
        S1.add('odd')
        d1[a]='odd'
print(L1)
print(S1)
print(d1)

pL=[]
nL=[]

for a in range(0
        ,15):
    n=int(input(f" enter the number{a+1}"))
    if n<0:
        nL.append(n)
    else:
        pL.append(n)
print(f" the sum of positive number are={sum(pL)}")
print(f" the sum of negative number are={sum(nL)}")
print(f" the max of positive ={max(pL)}")
print(f" the min of negative ={min(nL)}")
print(f" the number of positive elements={len(pL)}")


#dict using for loop

d={'milk':0.76,'orange':0.45,'pencil':0.85}
d1=dict()
print(d)
print(d.items())

for a,b in d.items():
    print(a)
    print(b)
    d1[a]=(b*0.35)+b
    print(d1)
'''
above40={}
below40 ={}
di={'a':37,'b':29,'c':42,'d':47,'e':27}
print(di)

for a,b in di.items():
    if b>=40:
        above40[a]=b
    else:
        below40[a]=b
print(above40)
print(below40)

L=[]
for b in range(1,1000):
    if b%2==0:
        if b%3==0:
            if b%4==0:
                if b%5==0:
                    L.append(b)
print(L)


























