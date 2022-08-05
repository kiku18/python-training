print("Accessing protected member of obj2: ", obj2._a)


# demonstrate private members
# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
# Driver code
obj1 = Base()
print(obj1.a)
# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class

class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

    def reset(self):
        self.current = 0



counter = Counter()


counter.increment()
counter.increment()
counter.increment()
print(counter.value())

counter.increment()
counter.increment()
counter.current = -999

print(counter.value())

counter = Counter()


class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0


counter = Counter()
print(counter._current)
counter.increment()
print(counter._current)
a=counter.value()
print(a)


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def display(self):
        print(self.name)
        print(self.__age)

    def getAge(self):
        print(self.__age)

    def setAge(self, age):
        self.__age = age


person = Person('Dev', 30)
# accessing using class method
person.display()
# changing age using setter
person.setAge(35)
person.getAge()