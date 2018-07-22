import traceback
"""
For example, instead of crashing your program right when an exception
occurs, you can write the traceback information to a log file and keep
your program running. You can look at the log file later, when you’re
ready to debug your program.
"""
try:
    raise Exception('error error')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
