import os
print(os.getcwd())
print(os.listdir())
os.chdir(r'C:\dummy')
print(os.getcwd())
print(os.listdir())
os.mkdir('pytest')
os.mkdir('DONKEY')
os.mkdir('PANDA')
os.mkdir('Mango')
f=open('duck.txt','a')
f=open('Lion.txt','a')
f=open('crow.txt','a')
f=open('num.txt','a')
f=open('gpa.xlsx','w')
f=open('gst.pptx','w')
f=open('jumbo.py','w')
f=open('news.html','a')
print(os.listdir())
os.rename('duck.txt','zebra.txt')
print(os.listdir())
os.rename('Mango','PTI')
print(os.listdir())
os.remove('Lion.txt')
os.remove('gpa.xlsx')
print(os.listdir())
os.rmdir('PANDA')
print(os.listdir())

import os.path
fileexist=os.path.isfile(r'C:\dummy\gpa.xlsx')
print(fileexist)
folderexist=os.path.isdir(r'C:\dummy\DONKEY')
print(folderexist)

if fileexist:
    print('file is already present')
else:
    f=open(r'atm.py','a')
    f.close()

if folderexist:
    print('folder already exist')
else:
    os.mkdir('jungle')


