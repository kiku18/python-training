import datetime
from tkinter import *
root=Tk()
root.geometry('1600x700')
root.title('GUI Frames')
TOPF=Frame(root,bg="#a21b1b",width=1600,height=50)
TOPF.pack(side=TOP)
BottomF=Frame(root,bg="#ff0854",width=1600,height=50)
BottomF.pack(side=BOTTOM)
F1=Frame(root,bg="red",width=900,height=700)
F1.pack(side=LEFT)
F2=Frame(F1,bg="blue",width=850,height=400)
F2.pack(side=TOP)
F2.pack(padx=15,pady=15)
F3=Frame(F1,bg="yellow",width=850,height=175)
F3.pack(side=BOTTOM)
F3.pack(padx=15,pady=15)
F4=Frame(root,bg="#f9b750",width=600,height=700)
F4.pack(side=RIGHT)
F5=Frame(F4,bg="green",width=600,height=350)
F5.pack(side=TOP)
F5.pack(padx=50,pady=100)

root.mainloop()


