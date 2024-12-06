# Initial balance and PIN
balance = 1000.0
correct_pin = "6666"

def check_balance():
    print("Your balance in the abyss is: £%.2f" % balance)

def deposit_amount(amount):
    global balance
    balance += amount
    print("New balance is: £%.2f" % balance)

def withdraw_amount(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("New balance is: £%.2f" % balance)
    else:
        print("Insufficient funds.")

def main():
    pin = input("Enter your secret code of darkness: ")
    if pin == correct_pin:
        print("Access to the Darkness granted! ")
        while True:
            print("\nDark ATM Menu")
            print("1. Check Balance")
            print("2. Deposit Amount")
            print("3. Withdraw Amount")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                check_balance()
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                deposit_amount(amount)
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                withdraw_amount(amount)
            elif choice == "4":
                print("Goodbye, may the darkness be with you.")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Incorrect code of darkness. Access denied.")

if __name__ == "__main__":
    main()
