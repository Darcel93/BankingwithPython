
from User import User
from Bank import Bank
from Menu import Menu

menu = Menu()
banking = Bank()
userdata =[]

def main():
    select = ""
    while select != "1" and select != "2"  and select != "3":
        menu.mainMenu()
        select = input("\n Please select an option: ")
        if select != "1" and select != "2"  and select != "3":
            print("Invalid selection, please try again \n")
    return select



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
    for currentUser in userdata:
        if userName == currentUser.username and password == currentUser.password:
            print("\nLogin Successful\n")
            return currentUser


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
    print("\n Account Created Successfully!\n")
    newAccount = User(nameFirst, nameLast, selectUser, pWord, email, "Z12345678")
    userdata.append(newAccount)
    return newAccount

def accountHome(newUser):
    select = ""
    while select != "3":
        accountNumber = newUser.accountNumber
        accountAmount = newUser.amount
        menu.homePage(accountNumber, accountAmount)
        try:
            select = input("\n Please select an option: ")
            if select == "1":
                print("Deposits \n")
                newAmount = input("Depoist Amount: ")
                newUser.amount = banking.deposits(int(newAmount), accountAmount)
            if select == "2":
                print("Withdrawals \n")
                newAmount = input("Withdrawal Amount: ")
                newUser.amount = banking.withdraw(accountAmount, int(newAmount))
            print("")
        except ValueError as v:
            print("Incorrect Value")
        except Exception as e:
            print(f"Error: {e} \n")




while True:
    choice = main()
    if choice == "3":
        print("Exiting Application \n")
        break
    account = signIn() if choice == "1" else signUp()
    if account == None:
        print("\nError: Login or Registration invalid \n")
    else:
        accountHome(account)







