import os,zipfile
exampleZip = zipfile.ZipFile('j.zip')

#for all files&folders present in zip folder j.zip
print(exampleZip.namelist())

# particular file in j.zip folder
a=exampleZip.open('j.txt')
b=a.readlines()
print(b)

#to extract all
exampleZip.extractall('./hello')
exampleZip.extract('j.txt','./hello2')