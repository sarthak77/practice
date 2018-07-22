import os
a=open('j.txt','r')
print(a.readlines())#1 line at a time
b=a.read()
print(b)
m=open('jj.txt','w')
m.write('defeefef\n')
m.close()
n=open('jj.txt','a')
n.write('ddwded')
n.close()
