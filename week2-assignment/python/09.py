class BankAccount:
    
    '''A class representing a bank account with basic functionalities.'''

    def __init__(self, account_holder: str, balance:float, account_type: str):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        '''Deposits the specified amount into the account.'''
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        '''Withdraws the specified amount from the account if sufficient funds are available.'''
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def display_balance(self):
        '''Returns a string representation of the account details and current balance.'''
        return f"Account holder: {self.account_holder}, Account Type: {self.account_type}, Current balance: ₹${self.balance:.2f}"    
    

if __name__ == "__main__":
    b1 = BankAccount("Iqbal", 1000.0, "Checking")
    print(b1.display_balance())  # Account holder: Alice, Account Type: Checking, Current balance: ₹1000.00
    b1.deposit(500)
    print(b1.display_balance())  # Account holder: Alice, Account Type: Checking, Current balance: ₹1500.00
    b1.withdraw(200)
    print(b1.display_balance())  # Account holder: Alice, Account Type: Checking, Current balance: ₹1300.00
    print(b1.withdraw(2000))     # Insufficient funds    