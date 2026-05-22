
class Menu:

    def mainMenu(self):
        print("\nMain Menu\n")
        print("1. Login")
        print("2. Register")
        print("3. Exit")


    def homePage(self, accountNumber, currentBalance):
        print("Account Home")
        print("Account Number: " + accountNumber)
        print("Current Balance: " + str(currentBalance) + "\n")
        print("1. Deposits")
        print("2. Withdrawls")
        print("3. Logout")


