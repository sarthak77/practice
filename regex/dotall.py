"""
The dot-star will match everything except a newline.
By passing re.DOTALL as the second argument to re.compile(),
you can make the dot character match all characters,
including the newline character.
"""
import re
x=re.compile('.*')
y=x.search("wdewdwfef\n\nerferererewe")
print(y.group())


x=re.compile('.*', re.DOTALL)
y=x.search("wdewdwfef\n\nerferererewe")
print(y.group())