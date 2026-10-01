password = input("Enter Password: ")
key = 3

encrypted = ""
for ch in password:
    encrypted += chr(ord(ch) + key)

print("Encrypted Password:", encrypted)