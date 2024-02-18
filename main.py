import datetime

class atm:
    def __init__(self,total_amount,pin):
        self.total_amount=total_amount
        self.pin = pin
        self.amount=0


# receipt for the transaction
    def last(self):
        while True:
            print("1.Print Receipt")
            print("2.Cancel")
            withdraw_input = int(input("Enter your Choice : "))
            if withdraw_input == 1:
                print("---------------------------------")
                print("     STATE BANK OF INDIA     ")
                today = datetime.datetime.now()
                print("     ", today.strftime("%d-%m-%y  %H-%M-%S"), " ")
                print("---------------------------------")
                print("   Name : Jack_Rose")
                print("   Card Number : xxxx 2365")
                if choice==1:
                    print("   Withdraw Amount : ", self.amount)
                elif choice==2:
                    print("   Amount added : ", self.amount)
                print("   Available Amount :", self.total_amount)
                print("---------------------------------")
                print("         Thank You     ")
                print("---------------------------------")
                break
            elif withdraw_input == 2:
                break


    # 1== withdraw operation
    def withdraw(self):
        pin_number=input("Enter Your Pin : ")
        if(self.pin==pin_number):
            self.amount=int(input("Enter Amount : "))
            if self.amount < self.total_amount :
                self.total_amount-=self.amount
                print("     Take Your Cash")
            else:
                print("     Insufficient Balance")
            self.last()
        else:
            print("     invalid Pin     ")


    # 2 == add cash through atm
    def add_cash(self):
        pin_number = input("Enter Your Pin : ")
        if (self.pin == pin_number):
            self.amount=int(input("Enter Amount :"))
            self.total_amount+=self.amount
            self.last()
        else:
            print("     invalid Pin     ")


   # 3== available balance|
    def balance_inquiry(self):
        pin_number = input("Enter Your Pin : ")
        if (self.pin == pin_number):
            self.last()
        else:
            print("     invalid Pin     ")



#  starting of a program
print("STATE BANK OF INDIA")
while True:
    print("     Main Menu      ")
    print("select our Service")
    print("1. Withdraw")
    print("2. Add Cash")
    print("3. Balance Inquiry")
    print("4. Exit")

    choice=int(input("Pick for Action : "))

    object=atm(10000,"1234")

    if choice==1:
        object.withdraw()
    elif choice==2:
        object.add_cash()
    elif choice==3:
        object.balance_inquiry()
    elif choice==4:
        print("     Thank you ! Visit Again     ")
        break
    else:
        print("   Invalid Choice   ")

