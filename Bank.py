class Bank:


    def deposits(self, newamount, currentamount):
        self.is_zero(newamount)
        depositamount = newamount + currentamount
        return depositamount

    def withdraw(self, currentamount,takenamount):
        self.is_zero(takenamount)
        if currentamount < takenamount:
            raise Exception("Insufficent Funds")
        withdrawamount = currentamount - takenamount
        return withdrawamount

    def is_zero(self, amount):
        if amount == 0:
            raise Exception("Zero is not a valid amount")

