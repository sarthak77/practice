passwordFile = open('a.txt')
secretPassword = passwordFile.read().rstrip('\n')
print('Enter your password.')
typedPassword = input()
print(typedPassword)
print(secretPassword)
if typedPassword == secretPassword:
   print('Access granted')
   if typedPassword == '12345':
      print('That password is one that an idiot puts on their luggage.')
else:
   print('Access denied')
