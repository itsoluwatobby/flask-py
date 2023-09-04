
class BalanceException(Exception):
    pass


class Bank_Account():
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit completed")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
        except BalanceException as amountError:
            print(f"\nWithdrawal of ${amount} interrupted: {amountError}")
        else:
            self.balance -= amount
            print(f"\nWithdrawal of ${amount} completed.")
            self.getBalance()

    def transfer(self, amount, account):
        try:
            self.viableTransaction(amount)
        except BalanceException as amountError:
            print(f"\nTransfer of ${amount} interrupted: {amountError}")
        else:
            print("\n*******************************")
            self.withdraw(amount)
            print(f"\nTransfer of ${amount} completed.")
            account.deposit(amount)

class InterestRewardsAccount(Bank_Account):
    
     def deposit(self, amount):
        interest = 0.05 * amount
        self.balance += amount + interest
        print("\nDeposit completed")
        self.getBalance()

class SavingsAccount(InterestRewardsAccount):
    
    def __init__(self, initialAmount, accountName):
        super().__init__(initialAmount, accountName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction((amount + self.fee))
        except BalanceException as amountError:
            print(f"\nWithdrawal of ${amount} interrupted: {amountError}")
        else:
            self.balance -= amount + self.fee
            print(f"\nWithdrawal of ${amount} completed.")
            self.getBalance()

