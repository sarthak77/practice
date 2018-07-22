"""Python’s regular expressions are greedy by default,
which means that in ambiguous situations they will match
 the longest string possible. 
 The non-greedy version of the curly brackets, 
 which matches the shortest string possible,
  has the closing curly bracket followed by a question mark.
"""
import re
a=re.compile(r'(ha){3,5}')
mo1=a.search('hahahahaha')
x=mo1.group()
print(x)

a=re.compile(r'(ha){3,5}?')
mo2=a.search('hahahahaha')
x=mo2.group()
print(x)