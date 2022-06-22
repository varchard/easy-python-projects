import math

def change_calculator(charge, tendered):
    if charge > tendered:
        return 'insufficient payment'
    change = int(tendered*100) - int(charge*100)
    dollars = math.floor(tendered - charge)
    cents = change - (int(dollars)*100)
    pennies = 0
    nickles = 0
    dimes = 0
    quarters = 0
    while (cents % 5) != 0:
        pennies += 1
        cents -= 1
            
    while cents != 0:
        if cents % 25 == 0:
            quarters = int(cents/25)
            cents = 0
        elif cents % 10 == 0:
            if (cents - 50) > 0:
                quarters = 2
                cents -= 50
            dimes = int(cents/10)
            cents = 0
        else:
            nickles +=1
            cents -= 5
    return f'change is {dollars}$, {quarters} quarters, {dimes} dimes, {nickles} nickles and {pennies} pennies'        


while True:
    try:
        cost = float(input('What is the cost of the item to purchase? '))
        break
    except ValueError:
        print('invalid entry, input as number')

while True:
    try:
        payment = float(input('What is the payment to give? '))
        break
    except ValueError:
        print('invalid entry, input as number')

print(change_calculator(cost,payment))