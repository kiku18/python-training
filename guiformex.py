from tkinter import *
import csv
import sqlite3
import os.path
root=Tk()
root.title('Application Form')
root.geometry('400x700')
def save():
    conn = sqlite3.connect(r'C:\Users\kumar\application.db')
    cur = conn.cursor()
    sql = f"insert into appmark values('{IDv.get()}','{namev.get()}',{m1v.get()},{m2v.get()},{m3v.get()},'{Locationv.get()}','{Phonev.get()}')"
    print(sql)
    cur.execute(sql)
    conn.commit()
    cur.close()

    print("Value added")
    print(IDv.get())
    print(namev.get())
    print(m1v.get())
    print(m2v.get())
    print(m3v.get())
    print(Locationv.get())
    print(Phonev.get())

    fcheck=os.path.isfile(r'C:\dummy\confidential\application.csv')
    if fcheck:
        with open(r'C:\dummy\confidential\application.csv','a',newline="") as f:
            w = csv.writer(f)
            w.writerow([IDv.get(),namev.get(),m1v.get(),m2v.get(),m3v.get(),Locationv.get(),Phonev.get()])
    else:
        with open(r'C:\dummy\confidential\application.csv','a',newline="") as f:
           w = csv.writer(f)
           w.writerow(['Sno','Name','m1','m2','m3'])
           w.writerow([IDv.get(),namev.get(),m1v.get(),m2v.get(),m3v.get(),Locationv.get(),Phonev.get()])

Label(root,text="ID").grid(row=0,column=0)
IDv=IntVar()
Entry(root,textvariable=IDv).grid(row=0,column=1)
IDv.set(' ')
Label(root,text="Name").grid(row=1,column=0)
namev=StringVar()
Entry(root,textvariable=namev).grid(row=1, column=1)
Label(root,text="m1").grid(row=2,column=0)
m1v=IntVar()
Entry(root,textvariable=m1v).grid(row=2,column=1)
m1v.set(' ')
Label(root,text="m2").grid(row=3,column=0)
m2v=IntVar()
Entry(root,textvariable=m2v).grid(row=3,column=1)
m2v.set(' ')
Label(root,text="m3").grid(row=4,column=0)
m3v=IntVar()
Entry(root,textvariable=m3v).grid(row=4,column=1)
m3v.set(' ')

Label(root,text="Location").grid(row=5,column=0)
Locationv=StringVar()
Entry(root,textvariable=Locationv).grid(row=5,column=1)
Locationv.set(' ')

Label(root,text="Phone").grid(row=6,column=0)
Phonev=StringVar()
Entry(root,textvariable=Phonev).grid(row=6,column=1)
Phonev.set(' ')




Button(root,text="Submit",command=save).grid(row=7,column=1)
root.mainloop()