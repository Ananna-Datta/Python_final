class Bank:
    def __init__(self,name,email,password,type) -> None:
        self.name=name
        self.email=email
        self.password=password
        self.type=type


class Account(Bank):
    accounts=[]
    total_amount=0
    account_number_counter = 1000


    def __init__(self, name, email, password, type) -> None:
        super().__init__(name, email, password, type)
        self.account_number = 0
        self.accountNo = Account.account_number_counter
        Account.account_number_counter += 1
        self.balance = 0

        Account.accounts.append(self)


    def create_account(self,name,email,password,type):
        user=Bank(name,email,password,type)
        self.accounts.append(user)


    def delete_user_account(self, na, p):
        for acc in Account.accounts:
            if p==self.password and na==self.name:
                Account.accounts.remove(acc)

    
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"\n--> Deposited {amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrew ${amount}. New balance: ${self.balance}")
        else:
            print("\nInvalid withdrawal amount")

    def showInfo(self):
        for account in self.accounts:
            print(f"Infos of {account.type} account of {account.name}:\n")
            print(f'\n\tAccount Type : {account.type}')
            print(f'\tName : {account.name}')
            print(f'\tAccount No : {account.accountNo}')
            print(f'\tCurrent Balance : {account.balance}\n')
            # print(f'\tAccount Number : {self.account_num}\n')


while True:
    print("1. Create an account ")
    print("2. Delete any user account")
    print("3. See all user accounts list")
    print("4. Check the total available balance of the banK")
    print("5. Check the total loan amount.")
    print("6. Can on or off the loan feature of the bank.")
    print("7. Logout.\n")
    c=int(input("Enter the Option:"))
    if c==1:
        name=input("Name:")
        pa=input("Password:")
        em=input("Enter the Email:")
        d=input("Savings Account or special Account (sv/sp) :")
        currentUser=Account(name,em,pa,d)

    elif c==2:
        name=input("Name:")
        pa=input("Password:")
        currentUser.delete_user_account(name,pa)

    elif c==3:
        currentUser.showInfo()
    elif c==4:
        pass
    elif c==5:
        pass
    elif c==6:
        pass
    else:
        break