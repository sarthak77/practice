import smtplib
#1).connecting to smpt server
"""
Once you have the domain name and port information for your email
provider, create an SMTP object by calling smptlib.SMTP(), passing
the domain name as a string argument, and passing the port as an
integer argument.
"""
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
print(type(smtpObj))
"""
If the smptlib.SMTP() call is not successful, your SMTP server might
not support TLS on port 587. In this case, you will need to create an
SMTP object using smtplib.SMTP_SSL() and port 465 instead.
->>smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
"""
#2).sending smpt hello message
print(smtpObj.ehlo())
"""
Once you have the SMTP object, call its oddly named ehlo() method to
“say hello” to the SMTP email server. This greeting is the first step
in SMTP and is important for establishing a connection to the server.
You don’t need to know the specifics of these protocols. Just be sure
to call the ehlo() method first thing after getting the SMTP object
or else the later method calls will result in errors. The following
is an example of an ehlo() call and its return value:
If the first item in the returned tuple is the integer 250 (the code
for “success” in SMTP), then the greeting succeeded.
"""
#3).starting tls encryption
"""
If you are connecting to port 587 on the SMTP server (that is, you’re
using TLS encryption), you’ll need to call the starttls() method next.
This required step enables encryption for your connection. If you are
connecting to port 465 (using SSL), then encryption is already set up,
and you should skip this step.
"""
print(smtpObj.starttls())
"""
starttls() puts your SMTP connection in TLS mode. The 220 in the
return value tells you that the server is ready.
"""
#4).login
print('ENTER EMAIL ID')
eml=input()
print('EMAIL ENTERED')
print('ENTER PASSWORD')
pwd=input()
print('PASSWORD ENTERED')
print(smtpObj.login(eml,pwd))
"""
Pass a string of your email address as the first argument and a
string of your password as the second argument. The 235 in the return
value means authentication was successful. Python will raise an
smtplib.SMTPAuthenticationError exception for incorrect passwords.
"""
#5).sendmail
msg='hello'
a=smtpObj.sendmail(eml,'sarthak02singhal@gmail.com','Subject: \n'+msg)
print(a)
"""
your email,recipient email,msg

The return value from sendmail() is a dictionary. There will be one
key-value pair in the dictionary for each recipient for whom email
delivery failed. An empty dictionary means all recipients were
successfully sent the email.
"""
#6).quiting
smtpObj.quit()
#The 221 in the return value means the session is ending.