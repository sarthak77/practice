"""
PyPDF2 does not have a way to extract images, charts, or other media
from PDF documents, but it can extract text and return it as a Python
string.
"""
import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())