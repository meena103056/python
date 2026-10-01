import json

FILE = "contacts.json"

try:
    with open(FILE, "r") as file:
        contacts = json.load(file)
except:
    contacts = []


def save():
    with open(FILE, "w") as file:
        json.dump(contacts, file, indent=4)


while True:

    print("\n--- CONTACT MANAGEMENT SYSTEM ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        save()

        print("Contact added!")

    elif choice == "2":

        name = input("Enter name to search: ")

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print("Name :", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                break
        else:
            print("Contact not found!")

    elif choice == "3":

        name = input("Enter name to delete: ")

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)
                save()
                print("Contact deleted!")
                break
        else:
            print("Contact not found!")

    elif choice == "4":

        name = input("Enter name to update: ")

        for contact in contacts:
            if contact["name"].lower() == name.lower():

                contact["phone"] = input("Enter new phone: ")
                contact["email"] = input("Enter new email: ")

                save()
                print("Contact updated!")
                break
        else:
            print("Contact not found!")

    elif choice == "5":

        if not contacts:
            print("No contacts available.")

        for contact in contacts:
            print("\nName :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")