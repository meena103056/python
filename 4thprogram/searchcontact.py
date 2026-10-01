contacts = [
    {"name": "Meena", "phone": "9876543210", "email": "meena@gmail.com"},
    {"name": "Priya", "phone": "9876501234", "email": "priya@gmail.com"}
]

name = input("Enter name to search: ")

for contact in contacts:
    if contact["name"].lower() == name.lower():
        print("Contact Found")
        print("Name :", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        break
else:
    print("Contact not found")