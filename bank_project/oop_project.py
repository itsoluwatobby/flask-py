from bank_accounts import *

Dave = Bank_Account(1_000, 'Dave Gray')
Mark = Bank_Account(1_800, 'Mark Santos')

Adam = InterestRewardsAccount(4000, 'Adam')

Matthew = SavingsAccount(4000, 'Matthew')

Adam.deposit(100)

Adam.transfer(3500, Dave)

Matthew.withdraw(2200)

Matthew.deposit(1500)
# Dave.getBalance()
# # Mark.getBalance()

# Dave.deposit(4200)
# # Mark.deposit(2200)

# # Dave.withdraw(3250)

# Dave.transfer(2100, Mark)
