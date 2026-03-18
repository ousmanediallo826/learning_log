accountName = "Joe"
accountBalance = 100
accountPassword = 'shop'


while True:
    print()
    print('Press b to get the balance')
    print('press d to make a deposit')
    print('press w to make a withdrawal')
    print('press s to show the account')
    print('press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get balance')
        user_password = input('Enter your password: ')
        if user_password != accountPassword:
            print('Passwords do not match')
        else:
            print('Your balance is {}'.format(accountBalance))
    elif action == 'd':
        print('Make a deposit')
        userDepositAmount = int(input('Enter your deposit amount: '))
        if userDepositAmount < 0:
            print('Your deposit amount cannot be negative')
        else:
            accountBalance += int(userDepositAmount)
            print('Your deposit amount is successful.')

    elif action == 'w':
        print('Make a withdrawal')
        userWithdrawAmount = int(input('Enter your withdrawal amount: '))
        if userWithdrawAmount < 0:
            print('Your withdrawal amount cannot be negative')
        elif userWithdrawAmount > accountBalance:
            print('Your withdrawal amount cannot be greater than your balance')
        else:
            accountBalance -= int(userWithdrawAmount)
            print('Your withdrawal amount is successful.')

    elif action == 's':
        print('Show your account')
        print('          Name: {}'.format(accountName))
        print('          Balance: {}'.format(accountBalance))
        print('          Password: {}'.format(accountPassword))

    elif action == 'q':
        break
    else:
        print('Invalid input')

