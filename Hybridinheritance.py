# Types of Inheritance
# 1.Single
# 2.Multilevel
# 3.Multiple
# 4.Hierarchical
# 5.Hybrid

# Hybrid  Inheritance

class Family:
    def __init__(self,Fname,Mname):
        self.Fname=Fname
        self.Mname=Mname

    def printfa(self):
        print(f" My Father Mr. {self.Fname} ,Mother Ms.{self.Mname} are the pillar of my family")

class son(Family):
    def __init__(self,Fname,Mname,Sname):
        Family.__init__(self,Fname,Mname)
        self.Sname=Sname
    def S(self):
        print(f'My name is{self.Sname}')
        print('I am the only son')
        Family.printfa(self)

class daughter(Family):
    def __init__(self,Fname,Mname,Dname):
        Family.__init__(self,Fname,Mname)
        self.Dname=Dname
    def D(self):
        print(f'My name is {self.Dname}')
        print('I am the only daughter')
        Family.printfa(self)

class Eldest(daughter,Family):
    def __init__(self,Fname,Mname,Dname):
        Family.__init__(self,Fname,Mname)
        self.Dname = Dname

    def Eld(self):
        print(f' {self.Dname} you are the eldest')


class Youngest(son, Family):
    def __init__(self, Fname, Mname, Sname):
        Family.__init__(self, Fname, Mname)
        self.Sname = Sname

    def Young(self):
        print(f' {self.Sname} you are the youngest')

a=son('Mangalanathan','Karpagam','Kishore')
b=daughter('Mangalanathan','Karpagam','Sahana')
c=Youngest('Mangalanathan','Karpagam','Kishore')
d=Eldest('Mangalanathan','Karpagam','Sahana')

a.S()
b.D()
c.Young()
d.Eld()







