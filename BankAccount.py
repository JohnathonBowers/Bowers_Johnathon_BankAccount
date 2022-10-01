class BankAccount:
    all_account_info = []
    
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        BankAccount.all_account_info.append(self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self
    
    @classmethod
    def all_instances(cls):
        print(BankAccount.all_account_info)

account1 = BankAccount(.01, 500)
account2 = BankAccount(.01, 700)

account1.deposit(200).deposit(100).deposit(500).withdraw(1000).yield_interest().display_account_info()

account2.deposit(800).deposit(100).withdraw(100).withdraw(50).withdraw(200).withdraw(400).yield_interest().display_account_info()

BankAccount.all_instances()