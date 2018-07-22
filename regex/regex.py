
'''While there are several steps to using regular expressions in Python, each step is fairly simple.

    Import the regex module with import re.

    Create a Regex object with the re.compile() function. (Remember to use a raw string.)

    Pass the string you want to search into the Regex object’s search() method. This returns a Match object.

    Call the Match object’s group() method to return a string of the actual matched text.
'''
import re
x=input()
phone=re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo=phone.search(x)
try:
    print(mo.group())
except:
    print("phone no not found")