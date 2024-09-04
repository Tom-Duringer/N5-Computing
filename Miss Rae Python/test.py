#1 - Calorie Counter
#Tom Duringer
#05/09/23

print('1 - Calorie Counter Program')
print()

porridge_calories = int(input('How many calories in porridge? '))
toast_calories = int(input('How many calories in toast? '))
marmalade_calories = int(input('How many calories in marmalade? '))
coffee_calories = int(input('How many calories in coffee? '))

total_calories = porridge_calories + toast_calories + marmalade_calories + coffee_calories

print()
print('At breakfast you consumed', total_calories, 'Calories')
