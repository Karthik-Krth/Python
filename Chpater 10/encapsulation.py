class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
# print(account.get_balance())  # 1000
# print(account.__balance)  # Error: AttributeError
print(account._BankAccount__balance) #No error...