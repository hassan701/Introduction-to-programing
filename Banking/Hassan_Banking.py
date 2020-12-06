class Bank:
    numberOfCustomers = 0
    
    def __init__(self,bankName,customers):
        self.bankName = bankName
        self.customers = customers

    def addCustomer(self,f,l,u,p):
        self.customers.append(Customer(f,l,u,p))
        self.numberOfCustomers += 1
        
    def getNumberOfCustomers(self):
        return self.numberOfCustomers
    
    def getCustomer(self,index):
        return self.customers[index]
    

class Customer:
    def __init__(self,f,l,u,p):
        self.firstName = f
        self.lastName = l
        self.username = u
        self.Password = p
        self.account = Account()

    def getFName(self):
        return self.firstName

    def getLName(self):
        return self.lastName

    def getUser(self):
        return self.username

    def getPass(self):
        return self.Password
    
    def getAccount(self):
        return self.account
    
    def setAccount(self,acc):
        self.account = acc
   
     
class Account:
    #class variable
    noOfAccounts = 0
    
    def __init__(self,balance=1000):
        self.balance = balance  #instance variable

    def getBalance(self):
        return self.balance
    
    def deposit(self,amt):
        if amt > 0:
            self.balance = self.balance + amt
            return True
        else:
            return False
        
    def withdraw(self,amt):
        if amt <= self.balance:
            self.balance = self.balance - amt
            return True
        else:
            return False

def menu():
    RB.addCustomer("Hassan", "Hassan", "HM", "123")
    RB.addCustomer("Hassan", "Hassan", "MH", "12")
    RB.getCustomer(0).getAccount().deposit(123)
    print("Welcome to the RICH BANK, our company boss's 5 yearold child came up with name,...he died of cancer.\ncough\nHow may i help you today?\n ")
    print("1. Login")
    print("2.Create account")
    print("3.Info")
    y= input("Input:")
    if y=="1":
        login()
    elif y=="2":
        Createacc()
    elif y == "3":
        info()
    else:
        print(y)
        print("command not found")
        menu()
def Createacc():
    print("\n\nAlright let us get you all sorted out, dear customer.")
    First=input("First Name: ")
    Last = input("Last Name: ")
    Username = input("UserName:")
    for q in range(RB.getNumberOfCustomers()):
        if Username == RB.getCustomer(q).getUser():
            print("User already exists!")
            Createacc()
    Pasword = input("Password:")
    RB.addCustomer(First, Last, Username, Pasword)
    Intde = int(input("Intial deposit"))
    x = RB.getNumberOfCustomers() -1
    RB.getCustomer(x).getAccount().deposit(Intde)
    print("\nThank you for choosing our Bank, ",First,Last)
    suc(Username,Pasword,x)

def suc(Username,Password,Index):
    print("Welcome: ", Username)
    print("Name: ", RB.getCustomer(Index).getFName(), RB.getCustomer(Index).getLName())
    print("Curent deposit: ", RB.getCustomer(Index).getAccount().getBalance())
    print("\nNew you want to:\n1.Deposit money\n2.Send money\nAnything else to Logout and go back to menu")
    y = input("Input:")
    if y == "1":
        x = int(input("Amount:"))
        RB.getCustomer(Index).getAccount().deposit(x)
        print("Transaction Successful, Accounted updated ")
        suc(Username, Password, Index)
    elif y == "2":
        z = input("Username:")
        for q in range(RB.getNumberOfCustomers()):
            if z == RB.getCustomer(q).getUser():
                x = int(input("Amount:"))
                if x <= RB.getCustomer(Index).getAccount().getBalance():
                    RB.getCustomer(Index).getAccount().withdraw(x)
                    RB.getCustomer(q).getAccount().deposit(x)
                    print("Transaction Successful, Accounted updated ")
                    suc(Username, Password, Index)
                else:
                    print("Account balance is insufficient. Try again later.")
                    suc(Username, Password, Index)
            else:
                print("Username doesn't exist within the system. Try again later.")
                suc(Username, Password, Index)
    else:
        menu()

def login():
    print("Login")
    U = input("UserName:")
    P = input("Password:")
    for i in range(RB.getNumberOfCustomers()):
        print(RB.getCustomer(i).getUser())
        print(RB.getCustomer(i).getPass())
        if U== RB.getCustomer(i).getUser() and P==RB.getCustomer(i).getPass():
            suc(U,P,i)
        else:
            "Wrong User name or Password"
            menu()

def info():
    print("Total number of customers:",RB.getNumberOfCustomers())
    for i in range(RB.getNumberOfCustomers()):
        print(RB.getCustomer(i).getFName(),RB.getCustomer(i).getLName(),RB.getCustomer(i).getAccount().getBalance())
    menu()

def main():
    customers = []
    global RB
    RB = Bank("RICH BANK", customers)
    menu()


if __name__ == "__main__":
    main()













"""
    print(bCa.getNumberOfCustomers())
    
    bCa.addCustomer("Jonathan","Mannuela")
    
    print(bCa.getCustomer(0).getAccount().getBalance())
    
    bCa.addCustomer("Maria","Edward")
    
    print(bCa.getCustomer(1).getFName())
    
    print(bCa.getNumberOfCustomers())
    
    

    newCust = Customer("Darren","Wenan")
    
    newCust.setAccount(Account(1000000))
    
    
    print("New account >> ", newCust.getAccount().getBalance())
    if newCust.getAccount().deposit(50000):
        print("Balance updated ", newCust.getAccount().getBalance())
    else:
        print("Invalid transaction!!!")
        print("Balance is not updated ",newCust.getAccount().getBalance())
        
    if newCust.getAccount().withdraw(100000):
        print("Balance updated ", newCust.getAccount().getBalance())
    else:
        print("Invalid transaction!!!")
        print("Balance is not updated ",newCust.getAccount().getBalance())
    
    
    newAccount = Account()
    print("New account >> ", newAccount.getBalance())
    if newAccount.deposit(50000):
        print("Balance updated ", newAccount.getBalance())
    else:
        print("Invalid transaction!!!")
        print("Balance is not updated ",newAccount.getBalance())
        
    if newAccount.withdraw(100000):
        print("Balance updated ", newAccount.getBalance())
    else:
        print("Invalid transaction!!!")
        print("Balance is not updated ",newAccount.getBalance())
"""
if __name__ == "__main__":
    main()



