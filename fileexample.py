'''
filez= open('myownfile.txt','w')
filez.write('Hello to python\n')
filez.write('Welcome to Chennai\n')
L=['Hi\n''I am\n',' from Chennai\n']
print(L)
filez.writelines(L)
filez.close()

filez=open('myownfile.txt','r')
print(filez.read())
'''

import re
filer= open('myex.txt','r')
jp=filer.read()
x=re.sub("sleep",'awake',jp)
print(x)
filer=open('myex.txt','w')
filer.writelines(x)
filer.close()

from tamil import utf8
string = u"கிஷோர்"
letters = utf8.get_letters(string)
print(len(letters))
# 3. Not 4.
print(letters)
# [u'\u0b8e', u'\u0b83', u'\u0b95\u0bc1']
for letter in letters:
   print(letter)
# கி
# ஷோ
# ர்