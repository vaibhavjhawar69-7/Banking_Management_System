# BMS
import random   # NEW: for generating account numbers

accounts = {}          #Dictionary - used as it stores account details
account_numbers = []   #List - used as it stores all account numbers
names_set = set()      #Set - used as it stores unique names

MIN_BALANCE = 500   # NEW: Minimum balance rule


def create_account():
    print("Select Account Type:")
    print("1. Current")
    print("2. Savings")
    choice = input("Enter choice (1/2): ")

    # NEW LOGIC
    if choice == "1":
        print("Current Account feature is under development. Please choose Savings.")
        return   # stops function here

    elif choice == "2":
        acc_type = "Savings"

    else:
        print("Invalid choice! Defaulting to Savings.")
        acc_type = "Savings"

    # NEW: Auto-generate account number (no duplicates)
    acc_no = str(random.randint(1000, 9999))
    while acc_no in accounts:
        acc_no = str(random.randint(1000, 9999))

    print("Generated Account Number:", acc_no)

    name = input("Enter Name: ")
    balance = float(input("Enter Initial Deposit: "))

    accounts[acc_no] = (name, balance, acc_type)

    account_numbers.append(acc_no)   
    names_set.add(name)              

    print("Account Created Successfully!")


# Function - 2: to deposit money
def deposit():
    acc_no = input("Enter Account Number: ")
    amount = float(input("Enter Amount to Deposit: "))

    if acc_no in accounts:
        name, balance, acc_type = accounts[acc_no]   
        balance += amount
        accounts[acc_no] = (name, balance, acc_type)
        print("Deposit Successful!")
    else:
        print("Account Not Found!")


# Function to withdraw money
def withdraw():
    acc_no = input("Enter Account Number: ")
    amount = float(input("Enter Amount to Withdraw: "))

    if acc_no in accounts:
        name, balance, acc_type = accounts[acc_no]

        if (balance - amount) >= MIN_BALANCE:
            balance -= amount
            accounts[acc_no] = (name, balance, acc_type)
            print("Withdrawal Successful!")
        else:
            print("Minimum balance of 500 must be maintained!")
    else:
        print("Account Not Found!")


# Function to check balance
def check_balance():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        name, balance, acc_type = accounts[acc_no]

        if acc_type.lower() == "savings":
            interest = balance * 0.0725
            print("Interest (1 year):", interest)

        print("Account Holder:", name)
        print("Account Type:", acc_type)
        print("Balance:", balance)
    else:
        print("Account Not Found!")


# Function to display all accounts
def display_all():
    print("All Accounts:")
    for acc_no in account_numbers:
        name, balance, acc_type = accounts[acc_no]
        print(f"Acc No: {acc_no}, Name: {name}, Type: {acc_type}, Balance: {balance}")


# Main program loop
while True:
    print("\n---- Bank Management System ----")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        display_all()
    elif choice == 6:
        print("Thank you!")
        break
    else:
        print("Invalid Choice!")