class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print(f"interest rate is: {self.int_rate} Balance is : {self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
    @classmethod
    def all_accounts(cls):
        # we use cls to refer to the class
        for account in cls.accounts:
            print(f"interest is {account.int_rate} and balance is {account.balance}")



kostas = BankAccount(0.01,5000)
adriana = BankAccount(0.01,2000)

kostas.deposit(1000).deposit(3000).deposit(1000).withdraw(1000).yield_interest()

adriana.deposit(1000).deposit(3000).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest()

BankAccount.all_accounts()
