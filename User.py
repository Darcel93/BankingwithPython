class User:
    def __init__(self, firstName, lastName, username, password, email="", accountNumber = "", amount = 1000):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.email = email
        self.accountNumber = accountNumber
        self.amount = amount
