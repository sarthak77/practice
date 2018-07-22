import shelve
shelffile=shelve.open('mydata')
cats=['asasad','sdsda','wdwdwdw']
shelffile['cats']=cats
shelffile.close()