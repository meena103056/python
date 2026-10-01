balance = 10000

amount = int(input("Enter deposit amount: ₹"))

if amount <= 0:
    print("Invalid deposit amount.")
else:
    balance += amount
    print("Deposit successful.")
    print("Updated Balance: ₹", balance)
