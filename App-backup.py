from User import User
from Bank import Bank

Darcel = User("Darcel", "Sanders", "Darcel93", "dummy1", "testingtesting1@testhoo.com", "Z123456789", 1000)
Uyi= User("Omoruyi", "Omofonmwan", "AfricanKing", "SSJ")
Uyi.amount = 500
print(Uyi.amount)
Account = Bank()
Uyi.amount = Account.deposits(600, Uyi.amount)
Uyi.amount = Account.deposits(500, Uyi.amount)
print(Uyi.firstName)
print(Uyi.amount)
Uyi.amount = Account.withdraw(Uyi.amount, 800)
print(Uyi.amount)
#noZero()

def noZero():
    try:
        makeDeposit = Account.deposits(0, 1000)
        print(makeDeposit)
    except Exception:
        print("Zero is not a valid amount")


noZero()

def notEnough():
    try:
        makeWithdraw = Account.withdraw(1000, 1100)
        print(makeWithdraw)
    except Exception:
        print("Brokey!!")

notEnough()