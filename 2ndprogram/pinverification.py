pin = 1234

user_pin = int(input("Enter ATM PIN: "))

if user_pin == pin:
    print("Login Successful")
else:
    print("Invalid PIN")