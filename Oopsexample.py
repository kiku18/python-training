# How to create empty class
class sample:
    pass

# Class with print statement
class sample1:
    print('Hi')
    print('Welcome to OOPS')
    print('Inside Class I will run')

# Class with data member
class sample2:
    name='Besant'
    location='Tambaram'
s = sample2()
print(s.name)
print(sample2.name)
print(sample2.location)

# Class with data member and member function

class sample3:
    name='XYZ'
    age=30
    def printmessage(self):
        print(f"name={self.name} and age={self.age}")

s1 = sample3()
print(s1.name)
print(s1.age)
s1.printmessage()
print(sample3.name)
print(sample3.age)
s1.printmessage()

class employee:
    def __init__(self,id,name, salary):
        self.id=id
        self.name=name
        self.salary=salary
    def printm(self):
        print(f"{self.id} and {self.name} and {self.salary}")

e=employee(1,'Kishore',50000)
e1=employee(2,'Vignesh',50000)
e2=employee(3,'Naveen',50000)
e.printm()
e1.printm()
e2.printm()

class headerprint:
    def __init__(self):
        print('---------------------------------------')
        print("Welcome to TNEB")
        print("----------------------------------------")
class footerprint:
    def __init__(self):
        print('---------------------------------------')
        print("Please Pay the bill on time other wise sub will be disconnect please pay on time")
        print("----------------------------------------")
class elebillcal:

    def __init__(self,units):
        self.units=units
    def billcal(self):
        # program for calculating electricity bill in Python

        if (self.units <= 100):
            payAmount = self.units * 1.5
            fixedcharge = 25.00
        elif (self.units <= 200):
            payAmount = (100 * 1.5) + (self.units - 100) * 2.5
            fixedcharge = 50.00
        elif (self.units <= 300):
            payAmount = (100 * 1.5) + (200 - 100) * 2.5 + (self.units - 200) * 4
            fixedcharge = 75.00
        elif (self.units <= 350):
            payAmount = (100 * 1.5) + (200 - 100) * 2.5 + (300 - 200) * 4 + (self.units - 300) * 5
            fixedcharge = 100.00
        else:
            payAmount = 0
            fixedcharge = 1500.00

        Total = payAmount + fixedcharge;
        print("\nElecticity bill=%.2f" % Total)


units=int(input("please enter the number of units you consumed in a month"))
h=headerprint()
b=elebillcal(units)
b.billcal()
f=footerprint()




