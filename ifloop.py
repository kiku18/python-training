if -2:
    print("I will enter")
if False:
    print("I will not enter")
if True:
    print("I will enter")
if 99:
    print("I will enter")
if 0:
    print("I will enter")

age=int(input("Enter the age"))
if age <18:
    print("less than 18")
else:
    print("greater or equal to 18")

age = int(input("Enter the age"))
country = input("Enter the country")
if age < 18 and country == "India":
    print("Below 18 in India")
elif age < 18 and country != "India":
    print(f" Below 18 {country}")
elif age >= 18 and age <= 56 and country == "India":
    print("middle age in India")
elif age >=18 and age <=56 and country!="India":
    print(f"Middle age {country}")
elif age > 56 and country == "India":
    print("Senior citizen India")
else:
    print(f" Senior citizen{country}")

m1 = int(input("Enter the mark1"))
m2 = int(input("Enter the mark2"))
m3 = int(input("Enter the mark3"))
m4 = int(input("Enter the mark4"))
m5 = int(input("Enter the mark5"))

if m1<35 or m2<35 or m3<35 or m4<35 or m5<35:
   print(" The student had failed")
else:
    total = m1 + m2 + m3 + m4 + m5
    Avg = total / 5
    if total > 450:
        print(f"the student total ={total}")
        print(f"the average of the student ={Avg}")
        print('grade A')
    elif total < 350 and total >= 300:
        print(f"the student total ={total}")
        print(f"the average of the student ={Avg}")
        print('grade B')
    elif total < 300 and total >= 275:
        print(f"the student total ={total}")
        print(f"the average of the student ={Avg}")
        print('grade C')
    else:
        print(f"the student total ={total}")
        print(f"the average of the student ={Avg}")
        print('grade D')










