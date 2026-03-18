accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    global accountName, accountBalance, accountPassword
    print(' Name', accountName)
    print(' Balance:', accountBalance)
    print(' Password:', accountPassword)
    print()

def getBalance(password):
    global accountBalance, accountPassword, accountName
    if password != accountPassword:
        print('Wrong password')
        return None
    return accountBalance

def deposit(amountDeposit, password):
    global accountBalance, accountPassword, accountName
    if password != accountPassword:
        print('Wrong password')
        return None
    if amountDeposit < 0:
        print('Amount cannot be negative')
        accountBalance = accountBalance + amountDeposit
    return accountBalance

def withdraw(amount, password):
    global accountBalance, accountPassword, accountName
    if password != accountPassword:
        print('Wrong password')
        return None
    if amount < 0:
        print('Amount cannot be negative')
    if amount > accountBalance:
        print('Amount cannot be greater than balance')
    accountBalance = accountBalance - amount
    return accountBalance

newAccount('Ousmane', 100, 'soup')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()

    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    print('Done')





