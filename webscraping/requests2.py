import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    #better then previous code
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))