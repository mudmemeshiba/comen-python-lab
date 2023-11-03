class BankAccount:
    def __init__(self, accountID="1001", balance=500):
        self.ID = accountID
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdrawal(self, amount):
        self.balance -= amount
    def set_balance(self, new_balance):
        self.balance = new_balance
    def __str__(self):
        return f'ID: {self.ID}, Balance: {self.balance:.2f}'