class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account is created for "+ self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance+= amount
            self.showBalance()
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Amount must be greater than zero and not more than your account balance")

        self.showBalance()

    def showBalance(self):
        print("Available balance is {}".format(self.balance))


if __name__ == "__main__":
    gautam = Account("Gautam",0)
    gautam.showBalance()

    gautam.deposit(1000)
    # gautam.showBalance()
    gautam.withdraw(500)
    # gautam.showBalance()
    gautam.withdraw(5000)