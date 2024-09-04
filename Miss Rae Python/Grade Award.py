#Grade award
#Tom Duringer
#14/09/23

print('9 - Validated Grade Award Program')
print()

name = input('Please enter the name: ')

#validated input of number
mark = int(input('Please enter the mark from 0 - 100: '))
while mark<0 or mark>100:
    print('Sorry,',mark, 'is not recognised')
    

if mark>=70 and mark<=100:
    print('A')

elif mark<=69 and mark>=60:
    print('B')

elif mark<=59 and mark>=50:
    print('C')

elif mark<=49 and mark>=40:
    print('D')

elif mark<=39 and mark>=0:
    print('F')
          
