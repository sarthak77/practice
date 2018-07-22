import requests
"""
1)The requests.get() function takes a string of a URL to download.
By calling type() on requests.get()’s return value, you can see that
it returns a Response object, which contains the response that the
web server gave for your request. 

2)You can tell that the request for this web page succeeded by
checking the status_code attribute of the Response object. If it is
equal to the value of requests.codes.ok, then everything went fine
"""
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text)