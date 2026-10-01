encrypted = input("Enter Encrypted Password: ")
key = 3

decrypted = ""
for ch in encrypted:
    decrypted += chr(ord(ch) - key)

print("Original Password:", decrypted)