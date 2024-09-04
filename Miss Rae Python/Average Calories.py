#Average Calories
#Tom Duringer
#06/09/23

monday_calories = int(input('How many calories did you consume on Monaday? '))
tuesday_calories = int(input('How many calories did you consume on Tuesday? '))
wednesday_calories = int(input('How mnay calories did you consume on Wednesday? '))
thursday_calories = int(input('How many calories did you consume on Thursday? '))
friday_calories = int(input('How many calories did you consume on Friday? '))
saturday_calories = int(input('How mnay calories did you consume on Saturday? '))
sunday_calories = int(input('How mnay calories did you consume on Sunday? '))
print()
total_calories = monday_calories + tuesday_calories + wednesday_calories + thursday_calories + friday_calories + saturday_calories + sunday_calories

print(total_calories)
print()
print('Your average calories a day are:',total_calories//7,)
