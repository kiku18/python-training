# Types of Inheritance
# 1.Single
# 2.Multilevel
# 3.Multiple
# 4.Hierarchical
# 5.Hybrid

# Hierarchical  Inheritance

class Family:
    def __init__(self,Fname,Mname):
        self.Fname=Fname
        self.Mname=Mname

    def printFa(self):
        print(f" My Father Mr. {self.Fname} ,Mother Ms.{self.Mname} are the pillar of my family")

class son(Family):
    def __init__(self,Fname, Mname, Sname):
        Family.__init__(self, Fname, Mname)
        self.Sname=Sname

    def printSon(self):
        print(f" My name is {self.Sname}. I am the youngest in my family. I love my father and mother")
        Family.printFa(self)


class daughter(Family):
    def __init__(self, Fname, Mname, Dname):
        Family.__init__(self, Fname, Mname)
        self.Dname = Dname

    def printDaughter(self):
        print(f" My name is {self.Dname}. I am the Eldest in my family. I love my father and mother")
        Family.printFa(self)

a=son('Mangalanathan','Karpagam','Kishore')
b=daughter('Managalanathan','Karpagam','Sahana')

a.printSon()
b.printDaughter()





