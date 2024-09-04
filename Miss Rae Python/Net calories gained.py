#Net calories gained
#Tom Duringer
#21/09/23

print('14 - Net Calories Gained')
print()
#Create arrays
calories_consumed = [0,0,0,0,0,0,0]
calories_burned = [0,0,0,0,0,0,0]
net_gain = [0,0,0,0,0,0,0]
# create total

total = 0

#Take in results for week and store in arrays
for day in range(7):
    print('Day', day + 1)
    calories_consumed[day] = int(input('Enter calories consumed: '))
    calories_burned[day] = int(input('Enter caloried burned: '))
    net_gain[day] = calories_consumed[day] - calories_burned[day]

print('day \t Calories consumed \t Calories burned \t Net gain')
for day in range(7):
    print(day+1,'\t\t\',calories_consumed[day],','\t\t\t',calories_burned[day],'\t\t', net_gain[day])
    total = total + net_gain[day]
print()
print('That comes to', total, 'Calories over the week')

          
                                      
