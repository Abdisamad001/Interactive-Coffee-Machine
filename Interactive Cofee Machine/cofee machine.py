drink_list = {'coffee': 3, 'cappuccino': 5, 'espresso': 4.4, 'mocha': 4.2, 'latte': 3.2, 'water': 1}

print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
print('🅸🅱🆄🆄🆁 🅲🅾🅵🅵🅴🅴 🅼🅰🅲🅷🅸🅽🅴')
print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')

drink_names = list(drink_list.keys())
drink = input(f'What do you want to drink? {drink_names} ').lower()

if drink not in drink_list:
    print(f'Sorry, we cannot make your drink: {drink}')
else:
    money = float(input(f'Please put the money in the pocket ({drink_list[drink]}$ ):'))

    if money < drink_list[drink]:
        print(f'The money is not enough. We cannot make your drink. Here is your money ({money})')

    elif money == drink_list[drink]:
        print(f'Done! Here is your drink: {drink}. Enjoy! \U0001F60B')

    else:
        change = money - drink_list[drink]
        print(f'Done! Please take your change ({change}), and here is your {drink}. Enjoy! \U0001F60B')