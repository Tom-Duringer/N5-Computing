#Entry Validation
#Tom Duringer
#14/09/23

#need these two lines to import and set local currency
import locale
locale.setlocale(locale.LC_ALL,'')

print('8 - Validated Entry Program')
print()

print('''

Your coices are:
     1. crisps at 50p
     2. Cans at 80p
     3. Chocolate at 70p
     4. Water at 40p

     ''')
#display menu
choice = int(input('Enter either 1, 2, 3 or 4 to choose: '))
while choice<1 or choice>4:
    print('sorry,', choice, 'is not recognised')
    choice=int(input('Enter either 1, 2, 3, 4 to choose: '))
#end of while block

number = int(input('how many do you want to buy? '))

#code changed to efficent selection
if choice==1:
    cost = number * 0.50
elif choice==2:
    cost = number * 0.80
elif choice==3:
    cost = number * 0.70
elif choice==4:
    cost = number * 0.40
#end of selection

print('The cost =', locale.currency(cost))
    
    
        
