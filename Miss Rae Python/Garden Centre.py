#Garden Centre
#Tom Duringer
#05/09/23

print('2 - Garden Centre Program')
print()

tulips_spent = int(input('How much money did you spend on tulips? '))
crocuses_spent = int(input('How much money did you spend on crocuses? '))
snowdrops_spent = int(input('How much money did you spend on snowdrops? '))
daffodils_spent = int(input('How much money did you spend on daffodils? '))

total_spend = tulips_spent + crocuses_spent + snowdrops_spent + daffodils_spent

print()
print('Total spent on bulbs was £', total_spend)
print()

if total_spend > 30 :
    print('Please accept a gift of a free potato!')
