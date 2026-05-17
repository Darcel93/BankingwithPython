from User import User
from Bank import Bank
from Menu import Menu

menu = Menu()
banking = Bank()

def main():
    select = ""
    while select != "1" and select != "2"  and select != "3":
        menu.mainMenu()
        select = input("\n Please select an option: ")
        if select != "1" and select != "2"  and select != "3":
            print("Invalid selection, please try again \n")

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







#main()
#signIn()
signUp()