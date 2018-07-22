import subprocess
a=subprocess.Popen('/usr/bin/gnome-calculator')
print(a)
"""
POLL
You can think of the poll() method as asking your friend if she’s
finished running the code you gave her. The poll() method will return
None if the process is still running at the time poll() is called. If
the program has terminated, it will return the process’s integer exit
code. An exit code is used to indicate whether the process terminated
without errors (an exit code of 0) or whether an error caused the
process to terminate (a nonzero exit code—generally 1, but it may
vary depending on the program).
"""
"""
WAIT
The wait() method is like waiting for your friend to finish working
on her code before you keep working on yours. The wait() method will
block until the launched process has terminated. This is helpful if
you want your program to pause until the user finishes with the other
program. The return value of wait() is the process’s integer exit
code.

Note that the wait() call will block until you quit the launched
calculator program.
"""

calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
print(calcProc.poll() == None)
print(calcProc.wait())
print(calcProc.poll())