import sys
import random
import string
User = {}

Users = {
    1023659471120800 : {'Name': 'Makus Maxwell', 'Balance' : 30000, 'pin' : 1007}, 
    1086405609728292 : {'Name': 'Sage Tochukwu', 'Balance' : 11000, 'pin' : 4006}
         }
Account_balance = 0

#Define account balance
print("Welcome !")

ExstUsr = input('Are you an existing user? ')
if ExstUsr == 'yes' :
    Existing_user = input("Kindly enter your sixteen digits card number: ")

    if len(Existing_user) != 16 :
        print("Invalid card number")
        sys.exit(0)

    if Existing_user == 1023659471120800 :
        print(int(input("Welcome " + Users[1023659471120800] + "Please enter your pin: ")))

    elif Existing_user == 1086405609728292 :
        print(int(input("Welcome " + Users[1086405609728292] + "Please enter your pin: ")))

else :
    Q1 = input("Would you like to sign up: ").strip().lower()
    if Q1 == "yes" :
        Name = input("Enter your name: ").strip().lower()
        Card_number = "".join(random.choices(string.digits, k = 16))
        print(f"Your new account number is {Card_number}")
        pin = input("Please enter your four digit pin: ")
        if len(pin) < 4 :
            print('Invalid. Enter a four digits pin')
            sys.exit(0)
        elif len(pin) > 4 :
            print('Invalid. Enter a four digits pin')
            sys.exit(0)
        else :
            print("Accueillir ")
        User[Card_number] = {
            'Name' : Name,
            'pin' : pin,
        'Account_balance' : Account_balance
        }
        print("Welcome to Duch Bank. Please fund your card :) ")
    else:
        print("Thank you")
        sys.exit(1)

def Deposit() :
    Card_number = input("Enter your card number: ")
    Amount = int(input("Enter amount"))
    pin = int(input("Please enter your pin: "))
    if len(pin) < 4 :
            print('Invalid. Enter a four digits pin')
            sys.exit(0)
    elif len(pin) > 4 :
            print('Invalid. Enter a four digits pin')
            sys.exit(0)
    else :
        Account_balance += Amount
        print(f"Deposited {Amount} Successfully")
        Show_balance()

def Show_balance(): 
    print(f"Your balance is {Account_balance}")

def Withdraw():
    Amount = int(input("Enter amount to be withdrawn: "))
    pin = input('Enter four digits pin: ')
    if len(pin) < 4 :
        print('Invalid. Enter a four digits pin')
        sys.exit(0)
    elif len(pin) > 4 :
        print('Invalid. Enter a four digits pin')
        sys.exit(0)
    else :
        if Amount > Account_balance:
                print('Insufficient funds')
        else :
                print(f"{Amount:.2f} withdrawn successfully")


def Transfer():
    account_num = int(input("Please enter account number: "))
    Bank_name = input("Enter bank name: ").strip().lower()
    print("Confirm account name")
    Amount = int(input("Enter amount: "))
    pin = input("Enter your pin: ")
    if len(pin) < 4 :
        print('Invalid. Enter a four digits pin')
        sys.exit(0)
    elif len(pin) > 4 :
        print('Invalid. Enter a four digits pin')
        sys.exit(0)
    else :
        if Amount > Account_balance:
            print('Insufficient funds')
        else :
            print(f"{Amount} transferred successfully")

def FundCard() :
    account_num = int (input("Please enter your card number: "))
    if account_num != Card_number : 
        print("Error. Kindly enter your card number")
    else :
        Amount = int(input('Enter amount to be deposited into your card: '))
        print(f"Your new account balance is {Account_balance + Amount}")


while True :
    print("1. Show balance")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Fund card")
    print("5. Exit")

    Choice = int(input("What do you want to do?: "))

    if Choice == 1 :
        Show_balance()

    elif Choice == 2 :
        Withdraw()

    elif Choice == 3 :
        Transfer()

    elif Choice == 4 :
        FundCard()

    else :
       sys.exit(0)

