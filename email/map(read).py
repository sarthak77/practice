#FOR DETAILS REFER TO BOOK
import imapclient,pprint
#1).connecting to imap server
import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#2).log in
"""
print('ENTER EMAIL ID')
eml=input()
print('EMAIL AENTERED')
print('ENTER PASSWORD')
pwd=input()
print('PASSWORD ENTERED')
"""
eml='library7iiit@gmail.com'
pwd='hello@77'
a=imapObj.login(eml,pwd)
print(a)
pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX',readonly=True)