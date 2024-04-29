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
    loan_status= True


    def __init__(self, name, email, password, type) -> None:
        super().__init__(name, email, password, type)
        self.account_number = 0
        self.accountNo = Account.account_number_counter
        Account.account_number_counter += 1
        self.balance = 0
        self.transaction_history=[]
        self.total_balence=0
        self.total_loan=0
        self.loan_count=0

        Account.accounts.append(self)


    def create_account(self,name,email,password,type):
        user=Account(name,email,password,type)
        self.accounts.append(user)


    def delete_user_account(self, na, p):
        for acc in Account.accounts:
            if p==self.password and na==self.name:
                Account.accounts.remove(acc)

    
    def deposit(self, amount):
        if amount > 0:
            self.balance+=amount
            # self.total_balance+=amount
            self.total_balence+=amount
            print(f'\ntk: {amount}/= Depsited successfully. New Balance is: {self.balance}\n')
            self.transaction_history.append(f'Depsited tk: {amount}/=')
        else:
            print('\nInvalid ammount\n')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f'\nTK: {amount}/= withdrawn successfully. New Balance is: {self.balance}\n')
            self.transaction_history.append(f'Withrawed tk: {amount}/=')
        else:
            print('\nInsufficient Balance\n')

    def showInfo(self):
        for account in self.accounts:
            print(f"Infos of {account.type} account of {account.name}:\n")
            print(f'\n\tAccount Type : {account.type}')
            print(f'\tName : {account.name}')
            print(f'\tAccount No : {account.accountNo}')
            print(f'\tCurrent Balance : {account.balance}\n')
            # print(f'\tAccount Number : {self.account_num}\n')

    def cheak_balence(self):
        print("\n\n\n-----------------------------------\n")
        print(f'Available Balance {self.balance}')
        print("\n-----------------------------------\n\n")


    def view_transaction_history(self):
        if len(self.transaction_history) > 0:
            for history in self.transaction_history:
                print(history)
        else:
            print('\nNo Transaction History\n')

    def take_loan(self, amount):
        if Account.loan_status and self.loan_count < 2:
            # self.loan_taken += amount
            self.balance += amount
            self.transaction_history.append(f"Loan taken: ${amount}")
            self.loan_count += 1
            self.total_loan+=amount
            self.total_balence-=amount
            print(f"Loan taken: ${amount}. New balance: ${self.balance}")
        elif not Account.loan_status:
            print("Loan feature is currently disabled by the bank.")
        else:
            print("You can only take a loan twice.")

    def total_bank_balence(self):
        print("----------------------------\n\n")
        print(f'Total Bank Balance is: {self.total_balnce}/=')
        print("\n\n----------------------------\n")


    def total_bank_loan(self):
        print("----------------------------\n\n")
        print(f'Total loan taken is: ${self.total_loan}')
        print("\n\n----------------------------\n")


    def set_loanStatus(self, status):
        Account.loan_status= status

    def transfer(self,pword,amount):
        if self.balance > amount:
            for user in Account.accounts:
                if user.password== pword:
                    user.balance+=amount
                    self.balance-=amount
                    self.transaction_history.append(f'transfered {amount}/= transfered to {pword}')
                    print(f'\nTk {amount} transfered . New Balance is: {self.balance}\n')
                    return
            print(f'AC {pword} not found')
        else:
            print('\nInsufficient Balance to transfer.\n')
       
        

while True:
    print('---------------Welcome to the Bank----------------')
    print('\n1 . Press 1 for Admin\n2 . Press 2 for User\n3 . Press 3 for exit')
    a=input("Enter your Option : ")
    if a=='1':
        b=input("Enter the Password:")
        if b=='111':
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
                    currentUser.total_bank_balence()

                elif c==5:
                    currentUser.total_bank_loan()

                elif c==6:
                    bl=input('Enter "N" to turn off "Y" to turn on: ')
                    if bl=="N":
                        currentUser.set_loanStatus(False)
                        print('\nLoan feature turned OFF\n')
                    elif bl=="Y":
                        currentUser.set_loanStatus(True)
                        print('\nLoan feature turned ON\n')
                    else:
                        print('Invalid Input\n')
                else:
                    break
        else:
            print("\n\nInvalid Password\n\n")

    elif(a=='2'):
        while True:
            print("1. Create an account ")
            print("2. Account Login ")
            print("3. Exit ")
            c=int(input("Enter the Option:"))
            if c==1:
                name=input("Name:")
                pa=input("Password:")
                em=input("Enter the Email:")
                d=input("Savings Account or special Account (sv/sp) :")
                currentUser=Account(name,em,pa,d)
                print(f'\tAccount No : {account.accountNo}')
                break
            elif c==2:
                pass
            else:
                break
    

    else:
        print('<<<<<<< Exited >>>>>>>>')
        break


