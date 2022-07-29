# Types of Inheritance
# 1.Single
# 2.Multilevel
# 3.Multiple
# 4.Hierarchical
# 5.Hybrid


# Single Inheritance example

class Parent:
    def __init__(self,fname,mname,fage,mage,plocation):
        self.fname=fname
        self.mname=mname
        self.fage=fage
        self.mage=mage
        self.plocation=plocation

    def printparent(self):
        print(f"The father name is: {self.fname} and The mother name is: {self.mname}, The father age is: {self.fage},The mother age is: {self.mage},My parents stay together in: {self.plocation}")

class child(Parent):
    def __init__(self,fname,mname,fage,mage,plocation,cname,cage,clocation):
        Parent.__init__(self,fname,mname,fage,mage,plocation)
        self.cname=cname
        self.cage=cage
        self.clocation=clocation

    def printchild(self):
        print(f"The child name is: {self.cname} and the child age is: {self.cage}  and the child currently dwells in: {self.clocation}")
        Parent.printparent(self)

a = child('Mangalanathan', 'Karpagam', 60, 57, 'Ramanathapuram', 'Kishore', 28, 'Tambaram')
a.printchild()


