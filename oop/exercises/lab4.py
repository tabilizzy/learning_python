class BankAccount:
    bank_name = "Cameroon National Bank"
    def __init__(self, account_number: str, balance: float = 0.0 ):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def show_balance(self):
        print(f"your new account banance is: {self.balance}")



acc1 = BankAccount("ACC001", 500.0)
acc2 = BankAccount("ACC002")

acc1.deposit(200)
acc1.show_balance()
acc1.withdraw(100)
acc1.show_balance()
print(BankAccount.bank_name)