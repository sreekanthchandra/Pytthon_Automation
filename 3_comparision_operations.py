'''
The elif statement allows you to check multiple expressions 
'''

n = 13

if n <= 12:
    print(' \n If block ')
elif n != 13:
    print(' \n First Elif ')
elif n > 15:
    print(' \n Second Elif ')
else:
    print(' \n Else Block ')
    
'''Nested if'''
#nested if
n = -99

if n >= 0:
    if n == 0:
        print("number is Zero")
    else:
        print("number is positive")
else:
    print("number is negative")
