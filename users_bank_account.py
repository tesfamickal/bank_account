from account import BankAccount


class Users:
    def __init__(self, name, balance):
        self.name = name
        self.account = BankAccount(balance)

    def make_deposit(self):
        print(self.account.deposit(100))
        return self

    def make_withdrawal(self):
        print(self.account.withdraw(20))
        return self

    def display_user_balance(self):
        print(self.account.balance)
        return self


# adrien = Users("Adrien", 200)
# adrien.make_deposit().display_user_balance()


# class BankAccount:

#     def __init__(self, int_rate=.01, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(self.balance)

#         return self

#     def withdraw(self, amount):
#         if (self.balance - amount) > 0:
#             self.balance -= amount
#             print(self.balance)
#         else:
#             print("Insufficient Funds: Charging a $5 fee")
#             self.balance -= 5
#             print(self.balance)

#         return self

#     def display_account_info(self):
#         print(f"Balance: ${self.balance}")
#         return self

#     def yield_interest(self):
#         if self.balance > 0:
#             self.balance += self.int_rate * self.balance

#         print(self.balance)

#         return self
