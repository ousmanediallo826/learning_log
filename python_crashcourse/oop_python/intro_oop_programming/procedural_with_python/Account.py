class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amount, password):
        if password != self.password:
            print('Password does not match')
        elif amount <= 0:
            print('Amount cannot be negative')
        else:
            self.balance = self.balance + amount
    def withdraw(self, amount, password):
        if password != self.password:
            print('Password does not match')
        elif amount <= 0:
            print('Amount cannot be negative')
        elif amount > self.balance:
            print('Amount exceeds balance')
        else:
            self.balance = self.balance - amount
    def getBalance(self):
        return self.balance

    def showUser(self):
        print()
        print('Name: ' + self.name)
        print('Balance: ' + str(self.balance))
        print('Password: ' + self.password)

