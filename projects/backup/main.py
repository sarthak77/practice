import os
import zipfile
import datetime


def backup():
    name=datetime.datetime.now()

    namefinal='backup_on_'+str(name)
    print (namefinal)

    os.chdir('/home/sarthak/backup')
    mainfolder='/home/sarthak/iiit/python_book/practice'

    a=zipfile.ZipFile(namefinal,'a')
    for folderName, subfolders, filenames in os.walk(mainfolder):
        print('working in folder:: '+folderName)
        print()
        for filename in filenames:
            print ('backingup '+filename)
            a.write(os.path.join(folderName,filename))
        print()
    a.close

backup()