contacts = {}
while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact saved ")

    elif choice == "2":
        if not contacts:
            print("No contacts found")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "3":
        name = input("Enter name to delete: ")
        contacts.pop(name, "Contact not found")

    elif choice == "4":
        print("Exiting ")
        break

    else:
        print("Invalid")
