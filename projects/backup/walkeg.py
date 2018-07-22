import os
i=1
for a,b,c in os.walk('/home/sarthak/junk/walk'):
    print(i)
    i=i+1
    print (a)
    print (b)
    print (c)