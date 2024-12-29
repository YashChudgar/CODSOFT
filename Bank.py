class Account:
    AccountNo=12345
    def __init__(self,name,balance,pin,typeA):
        Account.AccountNo+=1
        self.YourAccountNo=Account.AccountNo
        self.name=name
        self.balance=balance
        self.pin=pin
        self.type=typeA
        self.PDetails()
    def PDetails(self):
        print(self.name)
        print(self.YourAccountNo)
        print(self.pin)
        print(self.balance)

class Staff:
    Id=0
    def __init__(self,name,pin,work,salary,shift):
        Staff.Id+=1
        self.ID=Staff.Id
        self.name=name
        self.pin=pin
        self.work=work
        self.salary=salary
        self.shift=shift
        self.SDetails()
    def SDetails(self):
        print(self.ID)
        print(self.name)
        print(self.work)
        print(self.salary)
        print(self.shift)

class Bank:
    AccountList={}
    staffList={}

    def __init__(self):
        self.login=0
        self.stafflogin=0
    
    def createAccount(self,name,balance,pin,typeA):
        acc=Account(name,balance,pin,typeA)
        Bank.AccountList.update({acc.YourAccountNo:acc})

    def UserApp(self):
        self.AccLogin()

    def AccLogin(self):
        acc=int(input("Enter your Account Number"))
        pin=int(input("Enter Your Pin"))

        if acc in Bank.AccountList:
            if pin==Bank.AccountList[acc].pin:
                print("Welcome")
                self.login=acc
                self.menu()

            else:
                print("You have Entered wrong details")
                self.UserApp()

    def menu(self):            
        print('press 1 to check your balance')
        print('press 2 to change your pin')
        print('press 3 to transfer amount')
        print('press 4 to exit')

        i = int(input())
        if i == 1:
            a = Bank.AccountList[self.login].balance
            print(a)
            self.menu()
        elif i == 2:
            self.changepin()
            self.menu()
        elif i == 3:
            acc=int(input("Enter Senders Account No"))
            amount=int(input("Enter Amount"))
            self.transfer(self.login,acc,amount)
            self.menu()
        elif i == 4:
            pass

    def changepin(self):
        i = int(input("Enter your current Pin"))
        if Bank.AccountList[self.login].pin == i:
            pin=int(input("Enter your New Pin"))
            confirmpin=int(input("Confirm New Pin"))
            if pin==confirmpin:
                Bank.AccountList[self.login].pin=confirmpin
                print("Pin Changed Succesfully")
        else:
            print("You have entered wrong pin")

    def transfer(self,account1,account,amount):
        if account1 in Bank.AccountList and account in Bank.AccountList:
            if Bank.AccountList[account1].balance >= amount:
                Bank.AccountList[account1].balance -= amount
                Bank.AccountList[account].balance += amount
                print(f"Amount Transfer Successfull. Balance Remaining: {Bank.AccountList[account1].balance}")
            else:
                print("Low Balance")
        else:
            print("Entered wrong Account Details")
    
    def Deposit(self,account,amount):
        Bank.AccountList[account].balance+=amount
        print(f"Available Balance After Deposit: {Bank.AccountList[account].balance}")

    def Withdraw(self,account,amount):
        Bank.AccountList[account].balance-=amount
        print(f"Available Balance After Withdrawing: {Bank.AccountList[account].balance}")

    def CreateStaff(self,name,pin,work,salary,shift):
        a = Staff(name,pin,work,salary,shift)
        Bank.staffList.update({a.ID: a})

    def StaffApp(self):
        self.login=0
        self.sLogin()
    
    def sLogin(self):
        acc=int(input("Enter your ID number: "))

        if  acc in Bank.staffList:
            pin=int(input("Enter your pin"))
            if pin == Bank.staffList[acc].pin:
                print("Welcome")
                self.stafflogin = acc
                self.menu2()
            else:
                print("Wrong Pin")
                self.StaffApp()
        else:
            print("Wrong Details Entered")
            self.StaffApp()

    def menu2(self):
        print('press 1 to create account')
        print('press 2 to transfer amount')
        print('press 3 to deposite')
        print('press 4 to withdrawal')
        print('press 5 to exit')
        i = int(input())

        if i==1:
            name = input('enter your name')
            amt = int(input('enter your amount'))
            pin = int(input('enter your pin number'))
            typeA=input("Enter your Account Type")
            self.createAccount(name,amt,pin,typeA)
            self.menu2()


        elif i==2:
            acc1 = int(input('enter first account number'))
            acc2 = int(input('enter second account number'))
            amount = int(input('enter your amount'))
            self.transfer(acc1,acc2,amount)
            self.menu2()

        elif i ==3:
            acc = int(input('enter account number'))
            amount = int(input('enter your amount'))
            self.Deposit(acc,amount)
            self.menu2()

        elif i==4:
            acc = int(input('enter account number'))
            amount = int(input('enter your amount'))
            self.Withdraw(acc,amount)
            self.menu2()

        elif i == 5:
            print("you are logged out")

B=Bank()
B.CreateStaff("Bhumil",123,"Manager",5000,"Morning")
B.createAccount("Dev",9000,456,"Savings")
B.createAccount("Kartik",100000,999,"Savings")
B.UserApp()


