"""
1)
you must open the file in write binary mode by passing the string
'wb' as the second argument to open(). Even if the page is in
plaintext (such as the Romeo and Juliet text you downloaded earlier),
you need to write binary data instead of text data in order to
maintain the Unicode encoding of the text.

2)
The iter_content() method returns “chunks” of the content on each
iteration through the loop. Each chunk is of the bytes data type,
and you get to specify how many bytes each chunk will contain.
One hundred thousand bytes is generally a good size, so pass 100000
as the argument to iter_content().
"""

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()