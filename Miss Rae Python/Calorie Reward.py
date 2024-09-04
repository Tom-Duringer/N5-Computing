#Calorie Reward
#Tom Duringer
#05/09/23

breakfast_calories = int(input('How many calories did you consume at breakfast? '))
lunch_calories = int(input('How many calories did you consume at lunch? '))
dinner_calories = int(input('How many calories did you consume at dinner? '))

total_calories = breakfast_calories + lunch_calories + dinner_calories

print(total_calories)

calories_burned = int(input('How many calories did you burn today? '))

net_loss = total_calories - calories_burned 
print(net_loss)

if net_loss > 100 :
    print('Here! Have a banana!')
