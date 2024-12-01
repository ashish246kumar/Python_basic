class BankAccount:
    def __init__(self,account_number:str, name:str, balance=0):
        self.name=name
        self.__balance=balance
        self.account_number=account_number

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount")

    def withDraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print(f"WithDraw: {amount}")
        else:
            print("Insufficient balance in your account")   

    def get_balance(self):
        return self.__balance
    def get_account_info(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance:{self.__balance}"

   
    