#error because this module is for use in US
from twilio.rest import Client
accountSID='AC31b6edb974ce2fddfbed393dde5cd090'
authToken='0821ae48e75a538030e49f6a8caf8abc'
a=Client(accountSID,authToken)
print(a)
sender='7981759513'
receiver='9417306511'
msg=a.messages.create(
    to=receiver,
    from_=sender,
    body='hello'
)
print(msg.sid)