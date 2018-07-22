import re
"""
But sometimes you care only about matching the letters
without worrying whether they’re uppercase or lowercase.
To make your regex case-insensitive, you can pass re.IGNORECASE or re.I
as a second argument to re.compile().
"""

robocop = re.compile(r'robocop', re.I)
x=robocop.search('Robocop is part man, part machine, all cop.')
print(x.group())

x=robocop.search('RoboCop is part man, part machine, all cop.')
print(x.group())