#Tuck Shop
#Tom Duringer
#06/09/23

print('''

Your choices are:
        1. Crisps at 50p
        2. Cans at 80p
        3. Chocolate at 70p
        4. Water at 40p
        
''')

print()

choice = int(input('Enter either 1, 2, 3 or 4  to choose: '))
number = int(input('How many do you want to buy? '))
if choice==1:
    cost = number * 50
if choice==2:
    cost = number * 80
if choice==3:
        cost = number * 70
if choice==4:
    cost = number * 40

print('The cost =1', cost, 'pence')
        
        
