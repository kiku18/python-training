from tkinter import *
import csv
import os.path
root=Tk()
root.title('Sample Form')
root.geometry('400x700')
def save():
    print("Value added")
    print(Snov.get())
    print(namev.get())
    print(m1v.get())
    print(m2v.get())
    print(m3v.get())

    fcheck=os.path.isfile(r'C:\dummy\confidential\samplefile.csv')
    if fcheck:
        with open(r'C:\dummy\confidential\samplefile.csv','a',newline="") as f:
            w = csv.writer(f)
            w.writerow([Snov.get(),namev.get(),m1v.get(),m2v.get(),m3v.get()])
    else:
        with open(r'C:\dummy\confidential\samplefile.csv','a',newline="") as f:
           w = csv.writer(f)
           w.writerow(['Sno','Name','m1','m2','m3'])
           w.writerow([Snov.get(),namev.get(),m1v.get(),m2v.get(),m3v.get()])

Label(root,text="Sno").grid(row=0,column=0)
Snov=IntVar()
Entry(root,textvariable=Snov).grid(row=0,column=1)
Snov.set(' ')
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
Button(root,text="Submit",command=save).grid(row=5,column=1)
root.mainloop()