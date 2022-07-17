
import csv
import os.path
fcheck=os.path.isfile(r'C:\dummy\confidential\samplefile.csv')
sno=int(input("Enter the sno"))
name=input("Enter the name")
m1=int(input("Enter the m1"))
m2=int(input("Enter the m2"))
m3=int(input("Enter the m3"))
import datetime


if fcheck:
    with open(r'C:\dummy\confidential\samplefile.csv','a',newline="") as f:
        w = csv.writer(f)
        w.writerow([sno,name,m1,m2,m3])


else:
    with open(r'C:\dummy\confidential\samplefile.csv','a',newline="") as f:
        w = csv.writer(f)
        w.writerow(['sno','name','m1','m2','m3'])
        w.writerow([sno, name, m1, m2, m3])






