"""
Some PDF documents have an encryption feature that will keep them
from being read until whoever is opening the document provides a
password. Enter the following into the interactive shell with the
PDF you downloaded, which has been encrypted with the password
rosebud:
"""


import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
print(pdfReader.isEncrypted)
#error
#pdfReader.getPage(0)
pdfReader.decrypt('rosebud')
pageObj=pdfReader.getPage(0)
print(pageObj)