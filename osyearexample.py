import os
path=os.chdir('C:\dummy\Year')
print(os.getcwd())
year=[2001,2002,2003,2004,2005,2006,2008,2009]
currentpath=os.getcwd()

for i in range (len(year)):
    os.mkdir(str(year[i]))
    path=f"{currentpath}\{str(year[i])}"
    os.chdir(path)
    for j in range(1,13):
        os.mkdir(str(j))
    os.chdir(currentpath)
        
        


