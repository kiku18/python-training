# Types of Inheritance
# 1.Single
# 2.Multilevel
# 3.Multiple
# 4.Hierarchical
# 5.Hybrid

# Multiple Inheritance

class Gparent:
    def __init__(self,Fgfname,Fgmname,Fgfage,Fgmage,Fgplocation,Mgfname,Mgmname,Mgfage,Mgmage,Mgplocation):
        self.Fgfname=Fgfname
        self.Fgmname=Fgmname
        self.Fgfage=Fgfage
        self.Fgmage=Fgmage
        self.Fgplocation=Fgplocation
        self.Mgfname = Mgfname
        self.Mgmname = Mgmname
        self.Mgfage = Mgfage
        self.Mgmage = Mgmage
        self.Mgplocation = Mgplocation

    def printGparent(self):
        print(f"The Paternal grandfather name is: {self.Fgfname} and The Paternal grandmother name is: {self.Fgmname} \n The Paternal grandfather age is: {self.Fgfage} \nThe Paternal grandmother age is: {self.Fgmage} \n My  Paternal grandparents stay together in: {self.Fgplocation} \nThe Maternal grandfather name is: {self.Mgfname} and The Maternal grandmother name is: {self.Mgmname} \n The Maternal grandfather age is: {self.Mgfage} \n The Maternal grandmother age is: {self.Mgmage} \n My Maternal grandparents stay together in: {self.Mgplocation}")

class Parent:
    def __init__(self,fname,mname,fage,mage,plocation):
        self.fname = fname
        self.mname = mname
        self.fage = fage
        self.mage = mage
        self.plocation = plocation

    def printParent(self):
        print(f"The father name is: {self.fname} and The mother name is: {self.mname} \n The father age is: {self.fage} \n The mother age is: {self.mage} \n My parents stay together in: {self.plocation}")

class child(Gparent,Parent):
    def __init__(self, Fgfname, Fgmname, Fgfage, Fgmage, Fgplocation, Mgfname, Mgmname, Mgfage, Mgmage, Mgplocation,fname, mname, fage, mage, plocation, cname, cage, clocation):
        Gparent.__init__(self, Fgfname, Fgmname, Fgfage, Fgmage, Fgplocation, Mgfname, Mgmname, Mgfage, Mgmage,Mgplocation)
        Parent.__init__(self, fname, mname, fage, mage, plocation)
        self.cname = cname
        self.cage = cage
        self.clocation = clocation

    def printchild(self):
        Gparent.printGparent(self)
        Parent.printParent(self)
        print(f"The child name is: {self.cname} and the child age is: {self.cage}  and the child currently dwells in: {self.clocation}")

# Fgfname,Fgmname,Fgfage,Fgmage,Fgplocation,Mgfname,Mgmname,Mgfage,Mgmage,Mgplocation,fname,mname,fage,mage,plocation,cname,cage,clocation
a = child('Sadhasivam', 'Muthumeena', 93, 89, 'Sivaganga', 'Muthanandam', 'Nachiyar', 83, 79, 'Ramanathapuram','Mangalanathan', 'Karpagam', 60, 57, 'Ramanathapuram', 'Kishore', 28, 'Tambaram')
a.printchild()


