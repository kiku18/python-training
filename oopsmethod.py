class sample4:
    course='python'
    def courseprint(cls):
        print(f"course selected={cls.course}")

# classname.functionname=classmethod(classname.functionname)
sample4.courseprint=classmethod(sample4.courseprint)
sample4.courseprint()

from datetime import date

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def frombirthyear(cls,name,year):
        return cls(name,date.today().year-year)

    def display(self):
         print(self.name,self.age)
    @staticmethod
    def  isadult(age):
        return age>18

p=person('Kishore',28)
p1=person.frombirthyear('Kumar',1990)
print(p1.age)
print(person.isadult(22))

class emp:
    company='Kekran mecran'
    @classmethod
    def message(cls):
        print(f"the company name={cls.company}")
        cls.func_msg()
    @staticmethod
    def func_msg():
        print('Welcome to class content')
emp.message()

class emp1:
    comp='Navis'
    @staticmethod
    def add(a,b,c):
        return a+b+c
    @classmethod
    def avg(cls):
        x=cls.add(10,20,40)
        return x/3
a=emp1.avg()
print(a)

# Inheritance example

class Parent:
    def __init__(self,fname,mname,fage,mage,plocation):
        self.fname=fname
        self.mname=mname
        self.fage=fage
        self.mage=mage
        self.plocation=plocation

    def display(self):
        print(f"The father name is: {self.fname} and The mother name is: {self.mname}, The father age is: {self.fage},The mother age is: {self.mage},My parents stay together in: {self.plocation}")

# Inheriting class Parent in child by giving the class name Parent with in class child
# here in inheritance we are declaring the init constructor of class Parent and its function in class child
# the parent class is called with its class name followed by it s function, refer line 70 to 73
class child(Parent):
    def __init__(self,fname,mname,fage,mage,plocation,cname,cage,clocation):
        Parent.__init__(self,fname,mname,fage,mage,plocation)
        Parent.display(self)
        self.cname=cname
        self.cage=cage
        self.clocation=clocation

    def display(self):
        print(f"The child name is: {self.cname} and The child age is: {self.cage}  and The child currently dwells in: {self.clocation}")


b=child('Mangalanathan','Karpagam',60,57,'Ramanathapuram','Kishore',28,'Tambaram')
b.display()

#  if not defined the print statement in function display, please call them using object as below.
# Note: use the below commands without inheriting
# print("The father name is :",(a.fname),"\n The mother name is:",(a.mname),"\n The father age is:",(a.fage), "\n The mother age is:",(a.mage),"\n My parents stay together in:",(a.plocation))
# print("The child name is:",(b.cname),"\n The child age is:",(b.cage),"\n The child currently dwells in:",(b.clocation))

