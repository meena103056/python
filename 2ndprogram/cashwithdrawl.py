balance = 5000

print("1. Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Balance:", balance)

elif choice == 2:
    amount = int(input("Deposit amount: "))
    balance += amount
    print("New Balance:", balance)

elif choice == 3:
    amount = int(input("Withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")