contacts = []

n = int(input("Enter number of contacts: "))

for i in range(n):
    print("\nContact", i + 1)

    name = input("Enter name: ")
    phone = input("Enter phone: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)

with open("contacts.txt", "w") as file:
    for contact in contacts:
        file.write(contact["name"] + "," + contact["phone"] + "\n")

print("\nAll contacts saved successfully!")