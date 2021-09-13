class BankAccount:

    def __init__(self, balance=0, int_rate=.01):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

        return self

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
            print(self.balance)

        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance

        print(self.balance)

        return self


james = BankAccount(50, .01)
james.deposit(200).deposit(50).deposit(20).withdraw(
    150).yield_interest().display_account_info()

dean = BankAccount(0, .02)
dean.deposit(500).deposit(200).withdraw(30).withdraw(100).withdraw(
    65).withdraw(20).yield_interest().display_account_info()
