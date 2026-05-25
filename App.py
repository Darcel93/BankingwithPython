
from User import User
from Bank import Bank
from Menu import Menu
import random
import string

menu = Menu()
banking = Bank()
userdata =[]

def main():
    while True:
        menu.mainMenu()
        select = getAnswer("\n Please select an option: ")
        if select in ("1", "2", "3"):
            return select
        print("Invalid selection, please try again \n")




#Will come back to after database
def signIn():
    while True:
        print("***Login*** \n")
        userinfo = (getAnswer("Please Enter Username: "), getAnswer("Please Enter Password: "))
        print("\n***Would you like to Continue?***")
        selection = getAnswer("\n 1. Yes, Continue\n" " 2. Return to Main Menu\n" "\n")
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




def getAnswer(question):
    while True:
        answer = input(question).strip()
        if answer:
            return answer
        print("\nField Cannot Be Left Blank!\n")


def signUp():
    print("\n***Registration***\n")
    nameFirst = getAnswer("Enter First Name: ")
    nameLast = getAnswer("Enter Last Name: ")
    email = getAnswer("Please enter a valid email address: ")
    selectUser = getAnswer("Enter Desired Username: ")

    while True:
        password = getAnswer("Create Password: ")
        confirm = getAnswer("Confirm Password: ")
        if password != confirm:
            print("\n Passwords do not match, please re-enter password \n")
        else:
            break
    print("\n Account Created Successfully!\n")

    newAccount = User(nameFirst, nameLast, selectUser, password, email, random.choice(string.ascii_uppercase) + str(random.randint(100000000, 999999999)))
    userdata.append(newAccount)
    return newAccount

def accountHome(newUser):
    while True:
        accountNumber = newUser.accountNumber
        accountAmount = newUser.amount
        menu.homePage(accountNumber, accountAmount)
        try:
            select = getAnswer("\n Please select an option: ")
            match select:
                case "1":
                    print("\nDeposits \n")
                    newAmount = getAnswer("Depoist Amount: ")
                    newUser.amount = banking.deposits(int(newAmount), accountAmount)
                case "2":
                    print("\nWithdrawals \n")
                    newAmount = getAnswer("Withdrawal Amount: ")
                    newUser.amount = banking.withdraw(accountAmount, int(newAmount))
                case "3":
                    break
                case _:
                    raise ValueError
            print("")
        except ValueError as v:
            print("\nIncorrect Value\n")
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







