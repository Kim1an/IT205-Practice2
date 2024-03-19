phone_book = {}

def add_contact(name, phone_number):
    phone_book[name] = phone_number
    print(f"Contact addded successfully.")

def lookup_contact(name):
    if name in phone_book:
        print(f"{name}'s Phone number is {phone_book[name]}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Contact deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    while True:
        print("\nSimple Phone Book")
        print("1. Add Contact")
        print("2. Look up Contact")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            add_contact(name, phone_number)
        elif choice == "2":
            name = input("Enter contact name to lookup: ")
            lookup_contact(name)
        elif choice == "3":
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
