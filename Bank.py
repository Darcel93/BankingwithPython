class Bank:

    @staticmethod
    def deposits(newamount, currentamount):
        self.is_zero(newamount)
        depositamount = newamount + currentamount
        return depositamount

    def withdraw(currentamount,takenamount):
        self.is_zero(takenamount)
        if currentamount < takenamount:
            raise Exception("Insufficent Funds")
        withdrawamount = currentamount - takenamount
        return withdrawamount

    def is_zero(self, amount):
        if amount == 0:
            raise Exception("0 is not a valid amount")


