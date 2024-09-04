#Dental Fillings
#Tom Duringer
#14/09/23

print('9. Dental Fillings')
print()

print('''

Your choice of filling is...
    1. temporary for £8 each
    2. amalgam for £14 each
    3. white for £43 each
    4. super white for £67 each

''')
choice = int(input('Please enter either 1, 2, 3 or 4: '))
number = int(input('How many fillings do you want done? '))

if choice==1:
    cost = number * 8
if choice==2:
    cost = number * 14
if choice==3:
    cost = number * 43
if choice==4:
    cost = number * 67

print(number, 'fillings will cost', cost, 'pounds')
