#see chapter 10 for more info about logging
import logging
#to disable logging messages
#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')

"""
Here, we use the logging.debug() function when we want to print log
information. This debug() function will call basicConfig(), and a line
of information will be printed. This information will be in the format
we specified in basicConfig() and will include the messages we passed
to debug(). The print(factorial(5)) call is part of the original
program, so the result is displayed even if logging messages are
disabled.
"""