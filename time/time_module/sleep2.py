import time
time.sleep(5)
"""
Be aware that pressing CTRL-C will not interrupt time.sleep() calls
in IDLE. IDLE waits until the entire pause is over before raising the
KeyboardInterrupt exception. To work around this problem, instead of
having a single time.sleep(30) call to pause for 30 seconds, use a
for loop to make 30 calls to time.sleep(1).
"""