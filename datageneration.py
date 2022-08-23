from pymongo import MongoClient
from random import randint

client = MongoClient(port=27017)
db=client.school

student_name=['student1','student2','student3','student4','student5']
age = ['21','22','20','24','22']
location = ['chennai','trichy','madurai','kovai','bangalore']
dob = ['9/3/93','10/5/95','14/10/97','21/8/96']
for x in range(1,200000):
    school={
        'student_name':student_name[randint(0,(len(student_name)-1))],
        'age': age[randint(0,(len(age)-1))],
        'location': location[randint(0, (len(location) - 1))],
        'dob': dob[randint(0, (len(dob) - 1))],
        'group': randint(1, 3)
    }
    result=db.student2.insert_one(school)