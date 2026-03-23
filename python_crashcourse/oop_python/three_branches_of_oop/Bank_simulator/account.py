
from utils import *
class BankAccount:
    def __init__(self, holder_name, starting_balance=0, account_type=''):
        self.holder_name = holder_name
        self.starting_balance = starting_balance
        self.account_number = get_generator_account_number()
        self.transactions = []
        self.user_info = {}
        self.account_type = account_type


    def deposit(self, amount):
       if amount < 0:
           return "You cannot deposit negative amount"
       else:
           self.starting_balance += amount
           self.transactions.append({
               'Account Type': self.account_type,
               'Account Holder': self.holder_name,
               'type': 'Deposit',
               'amount': amount,
               'timestamp': timeStamp()
           })
           return self.transactions

    def withdraw(self, amount):
        if amount < 0:
            return "You cannot withdraw negative amount"
        elif amount > self.starting_balance:
            return "Insufficient fund. no overdraft"
        else:
            self.starting_balance -= amount
            self.transactions.append({
                'Account Type': self.account_type,
                'Account Holder': self.holder_name,
                'type': 'Withdraw',
                'amount': amount,
                'timestamp': timeStamp()
            })
            return self.transactions
    def get_balance(self):
        return self.starting_balance

    def display_info(self):
        self.user_info['Account Type'] = self.account_type
        self.user_info['Account Holder'] = self.holder_name
        self.user_info['Account Number'] = self.account_number
        self.user_info['Account Balance'] = self.starting_balance
        return self.user_info

    def get_transaction_history(self):
        for transaction in self.transactions:
            print(
                f"[{transaction['timestamp']}] | {transaction['Account Holder']}, "
                f"you have successfully made a {transaction['type'].lower()} of "
                f"${transaction['amount']:,.2f} from your {transaction['Account Type']} account."
            )
    def to_dict(self):
        return {
            'Account Type:         ': self.account_type,
            'Account Holder:       ': self.holder_name,
            'Account Number:       ': self.account_number,
            'Account Balance:      ': self.starting_balance,
            'Transactions:         ': self.transactions
        }






