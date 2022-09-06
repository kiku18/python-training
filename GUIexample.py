from tkinter import *
import csv
import os.path
root=Tk()
root.title('Sample calculator')
root.geometry('400x700')
num1=IntVar()
num2=IntVar()
result=IntVar()
S=IntVar()

def sel():
    o=S.get()
    a=num1.get()
    b=num2.get()
    if o==1:
        result.set(a+b)
    elif o==2:
        result.set(a-b)
    elif o==3:
        result.set(a*b)
    else:
        result.set("Invalid")

def Runv():
    c=chk.get()
    unch=unchk.get()
    fcheck = os.path.isfile(r'C:\dummy\confidential\output.csv')
    if c==1:
        if fcheck:
            with open(r'C:\dummy\confidential\output.csv', 'a', newline="") as f:
                w = csv.writer(f)
                w.writerow([num1.get(), num2.get(), result.get()])
        else:
            with open(r'C:\dummy\confidential\output.csv', 'a', newline="") as f:
                w = csv.writer(f)
                w.writerow(['NUMBER1', 'NUMBER2', 'RESULT'])
                w.writerow([num1.get(), num2.get(), result.get()])
    if unch==1:
        print(num1.get(), num2.get(), result.get())


Label(root,text="number1").grid(row=0,column=0)
Entry(root,textvariable=num1).grid(row=0,column=1)
Label(root,text="number2").grid(row=1,column=0)
Entry(root,textvariable=num2).grid(row=1,column=1)
Radiobutton(root,text="addition",variable=S,value=1,command=sel).grid(row=2,column=0)
Radiobutton(root,text="subtraction",variable=S,value=2,command=sel).grid(row=2,column=1)
Radiobutton(root,text="multiplication",variable=S,value=3,command=sel).grid(row=2,column=2)
chk=IntVar()
unchk=IntVar()
num1.set('')
num2.set('')
result.set('')
Checkbutton(root,text=" Save to file",variable=chk).grid(row=3,column=0)
Checkbutton(root,text=" do not save",variable=unchk).grid(row=3,column=1)
Label(root,text="Result").grid(row=4,column=0)
Entry(root,textvariable=result).grid(row=4,column=1)
Button(root,text="Submit",command=Runv).grid(row=5,column=1)
root.mainloop()

