class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initial_account,acct_name):
        self.balance = initial_account
        self.name = acct_name
        print(f"\nAccount '{self.name}' created.\nBalance=${self.balance:.2f}")

    def get_balance(self):
        print(f"\bAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance = self.balance + amount 
        print(f"\nAccount '{self.name}', Deposit Completed; Your recent amount is ${self.balance:.2f}")
        #or self.get_balance()

    def viable_transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    def withdrawal(self,deduct,amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - deduct
            print(f"\nAccount '{self.name}', Withdrawal has been successfull '${self.balance:.2f}'")
            #or self.get_balance()
        except BalanceException as error:
            print(f"\nWithdrawal Interrupted: {error}")
    
    def transfer(self,send,amount):
        try:
            if(self.viable_transaction>0):
                print("You have enough money to transfer")
            else:
                print("You don't have any money to tranfer")
            self.send=self.balance - send
            print(f"\nAccount '{self.name}', Your Amount has been tranferred '{self.send}'")
        except BalanceException as error:
            print(f"\n Transfer Interrupted!")

class InterestRewardsAcct(BankAccount): 
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

class SavingsAcct(InterestRewardsAcct):
    def _init_(self, initial_amount, acct_name): 
        super()._init_(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount): 
        try: 
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee) 
            print("\nWithdraw completed.")
            self.get_balance() 
        except BalanceException as error: 
            print(f'\nWithdraw interrupted: {error}')
