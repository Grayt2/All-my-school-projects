global sigma
sigma = 0
global quarters
quarters = 0
global dimes
dimes = 0
global nickels
nickels = 0
global pennies
pennies = 0
global change
change = str(input('Enter amount of money you have: '))
change == sigma
if change[0] == '-':
    print('Error')
    exit()
change = (float(change))
def getting_coins():
    global quarters
    global sigma
    global change
    global dimes
    global nickels
    global pennies
    # quarters
    while change > 0.25:
        change = change - 0.25
        quarters = quarters + 1
    if change == 0.25:
        quarters = quarters + 1
        change = change - 0.25
    # dimes
    while change > 0.10:
        change = change - 0.10
        dimes = dimes + 1
    if change == 0.10:
        dimes = dimes + 1
        change = change - 0.10
    # nickels
    while change > 0.05:
        change = change - 0.05
        nickels = nickels + 1
    if change == 0.05:
        nickels = nickels + 1
        change = change - 0.05
    # pennies
    while change > 0.01:
        change = change - 0.01
        pennies = pennies + 1
    if change == 0.01:
        pennies = pennies + 1
        change = change - 0.01
    print(sigma,'dollars can be made with: ', quarters, 'quarters,', dimes, 'dimes,', nickels, 'nickels, and', pennies, 'pennies!')
getting_coins()