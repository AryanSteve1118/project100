class Atm:
    def __init__(self,card_num,pin):
        self.card_num=card_num
        self.pin=pin
    def cashWithDrawl(self,amount):
        balance=50,000-amount
        print("you have withdrawn "+str(amount))
        print("your remaining balance is "+str(balance))
    def BalanceEnquiry(self):
        print("your balance is 50,000")

def main():
    card_num=input("insert your card number: ")
    pin = input("enter your pin")

    user= Atm(card_num,pin)
    print("choose your activity")
    print("1.balance Enquiry 2.Cash Withdrawl")
    activity=int(input("Enter :"))
    if(activity==1):
        user.BalanceEnquiry()
    elif(activity==2):
        amount=int(input("enter the amount : "))
        user.cashWithDrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()