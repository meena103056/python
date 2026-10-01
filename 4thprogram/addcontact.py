contacts = []

name = input("Enter name: ")
phone = input("Enter phone: ")
email = input("Enter email: ")

contact = {
    "name": name,
    "phone": phone,
    "email": email
}

contacts.append(contact)

print("Contact added successfully!")
print(contacts)