
class Bank:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposite(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Amount withdrawn successfully")
        else:
            print("\nInsufficient balance")
            
    def display(self):
        print("Account number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)

b1 = Bank(101, "Attessy", "saving", 50000)

b1.display()

b1.deposite(20000)
print("Balance after deposit:", b1.balance)

b1.withdraw(1000)
print("Balance after withdrawal:", b1.balance)

