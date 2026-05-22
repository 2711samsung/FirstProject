contact = {}

while True:
    command = input("What do you want to do? (add/search/list/update/delete/quit): ")
    
    if command == 'add':
        name = input("Enter name: ").lower()
        phone = input("Enter phone: ").lower()
        contact[name] = phone
        print(f"Contact {name} added with phone {phone}.")
    
    elif command == 'search':
        name = input("Enter name to search: ").lower()
        if name in contact:
            print(f"Contact found: {name} - {contact[name]}")
        else:
            print("Contact not found.")
  
    elif command == 'list':
        if contact:
            print("Contact List:")
            for name, phone in contact.items():
                print(f"{name} - {phone}")
        else:
            print("your contact list is empty.")
    
    elif command == 'update':
        name = input("Enter name to update: ").lower()
        if name in contact:
            new_phone = input("Enter new phone: ").lower()
            contact[name] = new_phone
            print(f"Contact {name} updated with new phone {new_phone}.")
        else:
            print("Contact not found.")

    elif command == 'delete':
        name = input("Enter name to delete: ").lower()
        if name in contact:
            del contact[name]
            print(f"Contact {name} was deleted.")
        else:
            print("Contact not found.")

    elif command == 'quit':
        print("Exiting the contact manager. Goodbye!")
        break
    else:
        print("Invalid command. Please try again.")
    