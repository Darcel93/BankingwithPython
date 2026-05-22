
from User import User
from Bank import Bank
from Menu import Menu

menu = Menu()
banking = Bank()
userdata =[]

def main():
    while True:
        menu.mainMenu()
        select = input("\n Please select an option: ")
        if select in ("1", "2", "3"):
            return select
        print("Invalid selection, please try again \n")




#Will come back to after database
def signIn():
    while True:
        print("***Login*** \n")
        userinfo = (input("Please Enter Username: "), input("Please Enter Password: "))
        print("\n***Would you like to Continue?***")
        selection = input("\n 1. Yes, Continue\n" " 2. Return to Main Menu\n")
        if selection not in ("1", "2"):
            print("\nNot a valid option, please try again \n")
            continue
        if selection == "2":
            break
        for currentUser in userdata:
                if currentUser.username == userinfo[0] and currentUser.password == userinfo[1]:
                    print("\nLogin Successful\n")
                    return currentUser
        raise Exception ("\n***Username or Password Incorrect, Please Try Again***\n")







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
            print()
            if select == "1":
                print("\nDeposits \n")
                newAmount = input("Depoist Amount: ")
                newUser.amount = banking.deposits(int(newAmount), accountAmount)
            if select == "2":
                print("\nWithdrawals \n")
                newAmount = input("Withdrawal Amount: ")
                newUser.amount = banking.withdraw(accountAmount, int(newAmount))
            print("")
        except ValueError as v:
            print("Incorrect Value \n")
        except Exception as e:
            print(f"Error: {e} \n")




while True:
    choice = main()
    if choice == "3":
        print("Exiting Application \n")
        break
    try:
        account = signIn() if choice == "1" else signUp()
        if account != None:
            accountHome(account)
    except Exception as e:
        print(e)







