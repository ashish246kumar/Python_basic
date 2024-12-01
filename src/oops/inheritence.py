from encapsulation import BankAccount
class SavingAccount(BankAccount):
    def __init__(self,account_number,name,balance=0.0,interest_rate=0.01):
        super().__init__(account_number,name,balance)
        self.interest_rate=interest_rate
    
    def get_account_info(self):
        basic_info=super().get_account_info()
        return f"{basic_info},Interest Rate: {self.interest_rate}" 
    
    def apply_interest(self):
       self.deposit(self.interest_rate*self.get_balance())
       
savingAccount=SavingAccount("987654321", "ninja", 5000,0.08)
print(savingAccount.get_account_info())
savingAccount.apply_interest()
print(savingAccount.get_balance())
