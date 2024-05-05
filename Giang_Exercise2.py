# Alex Giang
# Professor Abolghasemi
# CIS 502
# 29 January 2024

# Exercise 2

# This file, Giang_Exercise2.py, provides classes
# BankAccount and Transaction for a simple
# bank account managing system. Upon the running of this
# file, an instance of BankAccount will be made for the user
# and the user may interactively deposit, withdraw,
# check the balance of their account, or view their
# transaction history.

import datetime


class BankAccount:

    # initializes attributes account number, account holder name,
    # and account balance in dollars.
    def __init__(self, number: int, holder_name: str, balance: float):
        self.number = number
        self.holder_name = holder_name
        self.balance = balance
        self.transactions = []

    # changes account balance by the indicated amount,
    # if the amount after the change is -0.00499 (negative half
    # a cent) or above.
    # does nothing otherwise
    def deposit(self, amount: float):
        if -amount > self.balance + 0.00499:
            return 'Could not withdraw ' + str(amount) + \
                ' | Balance is only $' + "{:.2f}".format(self.balance)
        else:
            self.transactions.insert(0, Transaction(amount, datetime.datetime.now()))
            self.transactions[0].display()
            ret = '\nSuccess! | Your balance is now: $' + '{:.2f}'.format(self.balance)
            self.balance += amount
            return ret + ' -> $' + '{:.2f}'.format(self.balance)

    # changes account balance by the inverse of the
    # indicated amount if possible.
    def withdraw(self, amount: float):
        return self.deposit(-amount)

    # returns a string indicating all details of the account
    def check_balance(self):
        return 'Account #' + str(self.number) + ' | ' + self.holder_name + \
            ' | Balance: $' + str(self.balance)

    # prints all transaction objects held within attribute transactions
    # and returns the initial balance of the account
    def show_transactions(self):
        print('Transactions for Account #' + str(self.number))
        print('Most recent at the top:')
        cumulative_balance = self.balance
        for i in self.transactions:
            trans_amt = i.display()
            print(' | Balance: ${:.2f}'.format(cumulative_balance))
            cumulative_balance -= trans_amt
        return cumulative_balance


class Transaction:
    # initializes fields amount deposited (negative if withdrawn)
    # and the real-world date-time of the transaction.
    def __init__(self, amount: float, date: datetime.datetime):
        self.amount = amount
        self.date = date

    # prints transaction details and returns the amount deposited
    # in the transaction; negative if withdrawn.
    def display(self):
        d_or_w = 'Deposit' if (self.amount > 0) else 'Withdrawal'
        print(d_or_w + ' on ' + str(self.date) + ' of ${:.2f}'.format(abs(self.amount)), end='')
        return self.amount


print('This program is a simple Bank Account Manager. An account has been set')
print('up for you below with the following details:')
user_account = BankAccount(12345, 'You', 23456.78)
print(user_account.check_balance())
print('You may enter the letters to perform the following actions:')
print('d - Make a deposit')
print('w - Make a withdrawal')
print('c - Check your account balance')
print('t - Show your transaction history')
print('Enter any other letter to quit the program.')
print('Type your letter below:')
choice = input()
while 1:
    if 'd' in choice:
        print('Enter amount to deposit (positive amount to two decimal places):')
        amount = 0.0
        # collect input until valid numerical value is given
        while amount < 0.005:
            try:
                amount = float(eval(input()))
                assert amount >= 0.005
            except Exception:
                print('Not a positive decimal amount. Try again:')
        print(user_account.deposit(amount))
    elif 'w' in choice:
        print('Enter amount to withdraw (positive amount to two decimal places):')
        amount = 0.0
        # collect input until valid numerical value is given
        while amount < 0.005:
            try:
                amount = float(eval(input()))
                assert amount >= 0.005
            except Exception:
                print('Not a positive decimal amount. Try again:')
        print(user_account.withdraw(amount))
    elif 'c' in choice:
        print(user_account.check_balance())
    elif 't' in choice:
        print('Initial balance: ${:.2f}'.format(user_account.show_transactions()))
    else:
        # only break case: invalid menu input
        print('Program ended. Thank you!')
        break
    print('Make your next choice below from the menu (a letter):')
    # collect next input
    choice = input()
