from tkinter import *
from pymongo import MongoClient
client=MongoClient(port=27017)
db=client.studentgui
root=Tk()
root.title('student management system')
root.geometry('400x200')
def submit():
    studentid=sid.get()
    studentname=sname.get()
    studentphonenumber=sphone.get()
    studentlocation=slocation.get()
    studentage=sage.get()
    # record="{'studentid':'",studentid,"','studentname':'",studentname,"','studentphonenumber':",studentphonenumber,",'studentlocation':'",studentlocation,"','studentage':",studentage,"}"
    record = {
        'studentid': studentid,
        'studentname': studentname,
        'studentphonenumber': studentphonenumber,
        'studentlocation': studentlocation,
        'studentage': studentage
    }
    print(record)
    db.studentdetails.insert_one(record)
    root.destroy()
sid=StringVar()
sname=StringVar()
sphone=IntVar()
slocation=StringVar()
sage=IntVar()
Label(root,text="student_id").grid(row=0,column=0)
Entry(root,textvariable=sid).grid(row=0,column=1)

Label(root,text="student_name").grid(row=1,column=0)
Entry(root,textvariable=sname).grid(row=1,column=1)

Label(root,text="student_phonenumber").grid(row=2,column=0)
Entry(root,textvariable=sphone).grid(row=2,column=1)
sphone.set("")

Label(root,text="student_location").grid(row=3,column=0)
Entry(root,textvariable=slocation).grid(row=3,column=1)

Label(root,text="student_age").grid(row=4,column=0)
Entry(root,textvariable=sage).grid(row=4,column=1)

sage.set("")
Button(root,text="submit to mongodb",command=submit).grid(row=5,column=1)
root.mainloop()