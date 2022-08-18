import time
sq=[]
cu=[]
def square(Threadname,endpoint,delay):
    for i in range(1,endpoint+1):
        sq.append(i**2)
        time.sleep(delay)
        print("Tread name was=",Threadname,"and sq value is =",sq)

def cube(Threadname,endpoint,delay):
    for i in range(1,endpoint+1):
        cu.append(i**3)
        time.sleep(delay)
        print("Tread name was=",Threadname,"and cu value is =",cu)


square("thread1",10,5)
print("---------------------------------------------")
cube("thread2",10,5)




