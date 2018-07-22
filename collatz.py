def collatz(x):

    x=int(x)
    if x%2 == 0:
        return(x/2)
    else:
        return(3*x+1)

print('Enter your number')
temp=input()
try:
    temp=int(temp)
    while temp!=1:
        temp=collatz(temp)
        temp=int(temp)
        print(temp)
except:
    print('invalid input')

