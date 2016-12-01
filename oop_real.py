#OOP Real World Problem
#By hms91

#defining the base class
class BankAccount(object):

    def __init__(self):
        pass

    def withdraw():
        pass
    def deposit():
        pass

#the derived class 
class SavingsAccount(BankAccount):

	#initialize attributes, set balance to default 1000
    def __init__(self):
        self.balance = 1000

	#method to add deposit into balance, return balance
    def deposit(self, amount):
        if (amount < 0):
            return "Invalid deposit amount"
        else:
            self.balance += amount
            return self.balance

	#method to add withdraw and return balance
    def withdraw(self, amount):
        if ((self.balance - amount) > 0) and ((self.balance - amount) < 1000):
            return "Cannot withdraw beyond the minimum account balance"
        elif (self.balance - amount) < 0:
            return "Cannot withdraw beyond the current account balance"
        elif amount < 0:
            return "Invalid withdraw amount"
        else:
            self.balance -= amount
            return self.balance 

class CurrentAccount(BankAccount):

	#initialize balance to 0
    def __init__(self):
        self.balance = 0

	#method to increment balance
    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        else:
            self.balance += amount
            return self.balance

	#method to widthdraw 
    def withdraw(self, amount):
        if amount < 0:
            return "Invalid withdraw amount"
        elif self.balance < amount:
            return "Cannot withdraw beyond the current account balance"
        else:
            self.balance -= amount
            return self.balance

