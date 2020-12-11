class BankAccount:
    
    name = 'jef'
    balance = 0.0

    def __init__(self, name):
        self.name = name

    def deposit(self, number):
        self.balance += number
        return self.balance
    
    def withdraw(self, number):
        self.balance -= number
        return self.balance


account = BankAccount('Alex')

print(account.name)
print(account.balance)

account.deposit(8)
account.withdraw(5)

print(account.balance)

