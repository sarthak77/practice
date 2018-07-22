"""
To summarize what the findall() method returns, remember the following:
When called on a regex with no groups,
 such as \d\d\d-\d\d\d-\d\d\d\d,
  the method findall() returns a list of string matches, such as ['415-555-9999', '212-555-0000'].
When called on a regex that has groups,
 such as (\d\d\d)-(\d\d\d)-(\d\ d\d\d),
  the method findall() returns a list of tuples of strings (one string for each group), such as [('415', '555', '9999'), ('212', '555', '0000')].
"""

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
x=mo.group()
print(x)


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
x=mo
print(x)