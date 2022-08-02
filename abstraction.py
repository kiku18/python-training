from abc import ABC
class car(ABC):         #abc is a default module ie already available on python.to see modules run python in cmd prompt and type help('modules')
    def mileage(self):
        pass

class tesla(car):
    def mileage(self):
        print("30kmpl")

class tata(car):
    def mileage(self):
        print('30kmpl')

t=tesla()
ta=tata()
t.mileage()
ta.mileage()


class besant:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displaypage(self):
        print(self.age)

o=besant('abc',25)
o.displaypage()
print(o.name)

class student:
    __name=None        #no _=public,1_=projected,2__=private
    _roll=None         #if public it can be called in another class ie can be inherited anywhere
    _branch=None        #if private it can be called within the same class only ie no inheritance
                        #if projected it can be called in another class ie can be inherited

    def __init__(self,name,roll,branch):
        self.__name=name
        self._roll=roll
        self._branch=branch



    def privateaccess(self):
        print(self.__name)

class s(student):
    def __init__(self,name,roll,branch):
        student.__init__(self,name,roll,branch)

    def _displayrollandbranch(self):
        print(self._roll)
        print(self._branch)

    #def displayo(self):
        #print(self._name)
o=s('abc',123,'it')
#o.displayo()
o._displayrollandbranch()
o.privateaccess()