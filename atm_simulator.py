def atm_simulator():
    balance = 1000
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your balance is {balance}")
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print(f"Deposited {amount}. New balance: {balance}")
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrew {amount}. New balance: {balance}")
            else:
                print("Insufficient balance.")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

atm_simulator()
