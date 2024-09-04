#Average Solar Payment
#Tom Duringer
#06/09/23


quarter1 = int(input('Enter the payment for quarter: '))
quarter2 = int(input('Enter the payment for quarter: '))
quarter3 = int(input('Enter the payment for quarter: '))
quarter4 = int(input('Enter the payment for quarter: '))

print()

yearly_total = quarter1 + quarter2 + quarter3 + quarter4
print('The total for the year = ',yearly_total,)
print()
print('The monthly average = ',yearly_total//12,)



