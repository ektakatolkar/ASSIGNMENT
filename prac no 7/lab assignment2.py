balance = 0

while True:
    print("\n--- BANK MENU ---")
    print("1.Display Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 4:
        break

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Amount Deposited")

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")

    else:
        print("Invalid choice")