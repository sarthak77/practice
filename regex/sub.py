import re

"""
Regular expressions can not only find text patterns but
can also substitute new text in place of those patterns.
The sub() method for Regex objects is passed two arguments.
The first argument is a string to replace any matches.
The second is the string for the regular expression.
The sub() method returns a string with the substitutions applied.
"""

namesRegex = re.compile(r'Agent \w+')
x=namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(x)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
x=agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(x)