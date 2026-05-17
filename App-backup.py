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

#Storage

menu = Menu()
banking = Bank()

def main():
    select = ""
    while select != "1" and select != "2"  and select != "3":
        menu.mainMenu()
        select = input("\n Please select an option: ")
        if select != "1" and select != "2"  and select != "3":
            print("Invalid selection, please try again \n")
        if select == "1":
            signIn()
        if select == "2":
            signUp()

#Will come back to after database
def signIn():
    print("Login \n")
    userName = input("Please Enter Username: ")
    password = input("Please Enter Password: ")
    selection = ""
    while selection != "1" and selection != "2":
        selection = input("\n 1. Enter    2. Cancel\n")
        if selection != "1" and selection != "2":
            print("\nNot a valid option, please try again \n")

def signUp():
    nameFirst = input("Enter First Name: ")
    nameLast = input("Enter Last Name: ")
    email = input("Please enter a valid email address: ")
    selectUser = input("Enter Desired Username: ")
    pWord = input("Create Password: ")
    confirm = input("Confirm Password: ")
    while pWord != confirm:
        print("\n Passwords do not match, please re-enter password \n")
        pWord =input("Create Password: ")
        confirm = input("Confirm Password: ")
    register = User(nameFirst, nameLast, selectUser, pWord, email)
    print(register.username)
    print(register.amount)







main()
#signIn()
#signUp()