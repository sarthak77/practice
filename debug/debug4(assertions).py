"""
An assertion is a sanity check to make sure your code isn’t doing something obviously wrong. These sanity checks are performed by assert statements. If the sanity check fails, then an AssertionError exception is raised. In code, an assert statement consists of the following:

    The assert keyword

    A condition (that is, an expression that evaluates to True or False)

    A comma

    A string to display when the condition is False

For example, enter the following into the interactive shell:
"""
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
"""
Here we’ve set podBayDoorStatus to 'open', so from now on, we fully
expect the value of this variable to be 'open'. In a program that uses
this variable, we might have written a lot of code under the assumption
that the value is 'open'—code that depends on its being 'open' in order
to work as we expect. So we add an assertion to make sure we’re right
to assume podBayDoorStatus is 'open'. Here, we include the message
'The pod bay doors need to be "open".' so it’ll be easy to see what’s
wrong if the assertion fails.
"""