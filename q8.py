pin = (input("Enter your pin"))
balance = float(input("Enter current balance"))
withdraw_amount = float (input("Enter withdraw amount"))


if pin == "1234":
    if withdraw_amount > balance:
        print("Insufficient balance in your account")

    elif (balance - withdraw_amount < 500 ):
             print("You must maintain a minimum balance of Rs.500")

    else:
            new_balance = balance - withdraw_amount
            print("Withdrawal successful!")
            print("Please collect your cash.")
            print("Remaining Balance: Rs. " + str(new_balance))

else:
    print("Error: Invalid PIN. Access denied.")
