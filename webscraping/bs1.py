import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
#print(res.text)
noStarchSoup = bs4.BeautifulSoup(res.text)
print(noStarchSoup)
