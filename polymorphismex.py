# inbuilt polymorphism
a = 6
b = 7
print(a+b)
a ='Kishore'
b ='Kumar'
print(a+b)
a ='Hello'
print(len(a))
a =[1,2,3,4,5,6]
print(len(a))

# polymorphism with function
def add3numbers(num1=0,num2=0,num3=0):
    return num1+num2+num3
a= add3numbers(5,6,7)
b= add3numbers(5,6)
c= add3numbers(5)
d= add3numbers()
print(a,b,c,d)

# polymorphism with class

class USA:
    def population(self):
        print("33 Million")

    def countrytype(self):
        print('Developed country')

    def location(self):
        print('North America')

class India:
    def population(self):
        print("1.3 Billion")

    def countrytype(self):
        print('Developing country')

    def location(self):
        print('Asia')

u= USA()
i= India()

for a in(u,i):
    a.population()
    a.location()
    a.countrytype()

# polymorphism with inheritance

class Bird:
    def __init__(self):
        print('I am bird class')
    def flight(self):
        print("Most birds cannot fly")

class sparrow(Bird):
    def flight(self):
        print('I can fly')

class penguin(Bird):
    def flight(self):
        print('I cannnot fly')

class Eagle(Bird):
    def flight(self):
        print('I can fly')

s=sparrow()
p=penguin()
e=Eagle()

for a in(s,p,e):
    a.flight()





