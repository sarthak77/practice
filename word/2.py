import docx
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('demo.docx'))

"""
The getText() function opens the Word document, loops over all the
Paragraph objects in the paragraphs list, and then appends their text
to the list in fullText. After the loop, the strings in fullText are
joined together with newline characters.
"""