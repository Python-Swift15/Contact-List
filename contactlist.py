names = []
phones = []
emails = []
birthdays = []
addresses = []

while True:
    print("\n=== My Contact List ===")
    print("1. Add new contact")
    print("2. Display all contacts")
    print("3. Save contacts")
    print("4. Exit")

    choice = input("What would you like to do? (1/2/3/4): ").strip()

    if choice == "4":
        print("Goodbye!")
        break

    elif choice == "1":
        print("\nAdding new contact...")
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()
        birthday = input("Enter birthday (DD/MM/YY): ").strip()
        address = input("Enter address: ").strip()

        names.append(name)
        phones.append(phone)
        emails.append(email)
        birthdays.append(birthday)
        addresses.append(address)

        print("Contact added successfully!")

    elif choice == "2":
        if not names:
            print("\nNo contacts yet.")
        else:
            print("\nAll Contacts:")
            for i in range(len(names)):
                print(f"\nContact #{i+1}:")
                print(f"Name: {names[i]}:")
                print(f"Phone: {phones[i]}:")
                print(f"Email: {emails[i]}:")
                print(f"Birthday: {birthdays[i]}:")
                print(f"Address: {addresses[i]}:")

    elif choice == "3":
        #save_contacts()
        print("Saving contacts...")
        print("Contact saved!")

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4 only!")