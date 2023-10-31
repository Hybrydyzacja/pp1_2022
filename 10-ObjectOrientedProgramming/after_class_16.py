class Account():
    
    def __init__(self, number):
        self.number = number
        self.account_balance = 0

    def deposit(self, new_deposit):
        self.account_balance += new_deposit

    def withdraw(self, new_withdraw):
        if self.account_balance < new_withdraw:
            print("Insufficient funds on the account")
        else:
            self.account_balance -= new_withdraw

    def show_status(self):
        print(f"Bank account No: {self.number}")
        print(f"Balance: PLN {self.account_balance}")


account1 = Account("12 3456 5555 9090 1111 0000 7722")

account1.show_status()
account1.deposit(25.30)
account1.show_status()
account1.withdraw(31.70)
account1.show_status()
account1.withdraw(14)
account1.show_status()
