"""
CONTENTS::-)
1)joining paths
2)pwd and cd
3)paths
4)names
5)filesizes
6)checking path valisity
"""


"""
On Windows, paths are written using backslashes (\) as the separator
between folder names. OS X and Linux, however, use the forward slash
(/) as their path separator. If you want your programs to work on all
operating systems, you will have to write your Python scripts to
handle both cases.
"""
import os
print(os.path.join('usr','bin','spam'))
"""
If you pass it the string values of individual file and folder names
in your path, os.path.join() will return a string with a file path
using the correct path separators.
"""

#two \\ as escape characters
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))




print(os.getcwd())#to get pwd
os.chdir('/')#to change directory
print(os.getcwd())

directory='/home/sarthak/junk/aaa/b/c/d'
os.makedirs(directory)


"""
Calling os.path.abspath(path) will return a string of the absolute
path of the argument. This is an easy way to convert a relative path
into an absolute one.

Calling os.path.isabs(path) will return True if the argument is an
absolute path and False if it is a relative path.

Calling os.path.relpath(path, start) will return a string of a
relative path from the start path to path. If start is not provided,
the current working directory is used as the start path.
"""
print(os.path.abspath('.'))
print(os.path.isabs('.'))
print(os.path.relpath('.','iiit'))

"""
Calling os.path.dirname(path) will return a string of everything
that comes before the last slash in the path argument.
Calling os.path.basename(path) will return a string of everything
that comes after the last slash in the path argument.
"""
print(os.path.dirname('/iiit'))
print(os.path.basename('/iiit'))
print(os.path.split('/iiit'))#for both together
os.chdir('/home/sarthak/iiit/python_book/practice/files')
a=os.getcwd()
print(a)
print(a.split(os.path.sep))

"""
Calling os.path.getsize(path) will return the size in bytes of the
file in the path argument.
Calling os.listdir(path) will return a list of filename strings
for each file in the path argument. (Note that this function is in
the os module, not os.path.)
"""
b=a+'/basic.py'
print(os.path.getsize(b))
print(os.listdir(a))

"""
Calling os.path.exists(path) will return True if the file or folder
referred to in the argument exists and will return False if it does
not exist.

Calling os.path.isfile(path) will return True if the path argument
exists and is a file and will return False otherwise.

Calling os.path.isdir(path) will return True if the path argument
exists and is a folder and will return False otherwise.
"""