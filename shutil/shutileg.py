import shutil #to copy,move,rename,delete files using python
import os
def hello():
    path='/home/sarthak/iiit/python_book/practice/shutil/j1.txt'
    dest='/home/sarthak/iiit/python_book/practice/shutil/junk/j1copied.txt'
    shutil.copy(path,dest)

"""
While shutil.copy() will copy a single file, shutil.copytree() will
copy an entire folder and every folder and file contained in it.
Calling shutil.copytree(source, destination) will copy the folder at
the path source, along with all of its files and subfolders, to the
folder at the path destination. The source and destination parameters
are both strings. The function returns a string of the path of the
copied folder.
"""

"""
similarly use shutil.move(path,dest)
"""

###DELETING###
"""
You can delete a single file or a single empty folder with functions
in the os module, whereas to delete a folder and all of its contents,
you use the shutil module.

Calling os.unlink(path) will delete the file at path.

Calling os.rmdir(path) will delete the folder at path.
This folder must be empty of any files or folders.

Calling shutil.rmtree(path) will remove the folder at path, and all
files and folders it contains will also be deleted.
"""
