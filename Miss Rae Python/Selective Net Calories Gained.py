#Selective Net Calories Gained
#Tom Duringer
#28/09/23

print('12 - Selective Net Calories Gained')
print()

calories_consumed = [0,0,0,0,0,0,0]
calories_burned = [0,0,0,0,0,0,0]
net_gained = [0,0,0,0,0,0,0]

chosen = [False,False,False,False,False,False,False,]
total = 0

for day in range(7):
    print('Day', day + 1)
    calories_consumed[day] = int(input('Enter calories consumed: '))
    calories_burned[day] = int(input('Enter calories burned: '))
    net_gained[day] = calories_consumed[day] = calories_burned[day]

for day in range(7):
    answer = input('Enter y to display day ' + str(day + 1) )
    if answer == 'y' :
        chosen[day] = True

for day in range(7):
    if chosen[day] == True:
        print(day+1,'\t\t',calories_consumed[day],'\t\t\t',
    calories_burned[day],'\t\t', net_gained[day])
        total = total + net_gained[day]

print()
print('That comes to', total, 'Calories for those days')
