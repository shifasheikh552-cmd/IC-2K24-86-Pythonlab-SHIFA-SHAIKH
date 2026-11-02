# Q5. Phone Directory using Lists and Reverse Lookup
# Stores: name -> {"phones": [numbers], "email": email, "city": city}

contacts = {
    "Anita": {"phones": ["9876543210"], "email": "anita@mail.com", "city": "Pune"},
    "Manoj": {"phones": ["9123456780", "9988776655"],
              "email": "manoj@mail.com", "city": "Delhi"},
    "Zara": {"phones": ["9000011111"], "email": "zara@mail.com", "city": "Pune"}
}


def valid_phone(number):
    # Keep phone numbers as strings so leading zeroes are not lost.
    return number.isdigit() and len(number) == 10


def number_owner(number):
    """Return the contact name who owns a number, or None."""
    reverse_lookup = {
        phone: name
        for name, data in contacts.items()
        for phone in data["phones"]
    }
    return reverse_lookup.get(number)


def add_contact():
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter 10-digit phone number: ").strip()
    if not valid_phone(phone):
        print("Rejected: phone number must contain exactly 10 digits.")
        return
    owner = number_owner(phone)
    if owner is not None:
        print(f"Rejected: this number already belongs to {owner}.")
        return

    email = input("Enter email: ").strip()
    city = input("Enter city: ").strip()
    contacts[name] = {"phones": [phone], "email": email, "city": city}
    print("Contact added successfully.")


def add_number():
    name = input("Enter existing contact name: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    phone = input("Enter additional 10-digit number: ").strip()
    if not valid_phone(phone):
        print("Rejected: phone number must contain exactly 10 digits.")
        return
    owner = number_owner(phone)
    if owner is not None:
        print(f"Rejected: this number already belongs to {owner}.")
        return
    contacts[name]["phones"].append(phone)
    print("Number added successfully.")


def update_contact():
    name = input("Enter contact name: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return

    print("1. Update email")
    print("2. Update city")
    choice = input("Enter choice: ").strip()
    if choice == "1":
        contacts[name]["email"] = input("Enter new email: ").strip()
        print("Email updated successfully.")
    elif choice == "2":
        contacts[name]["city"] = input("Enter new city: ").strip()
        print("City updated successfully.")
    else:
        print("Invalid choice.")


def delete_contact():
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def search_contact():
    term = input("Enter full or partial name: ").strip().lower()
    matches = {
        name: data for name, data in contacts.items() if term in name.lower()
    }
    if matches:
        for name, data in matches.items():
            print(name, ":", data)
    else:
        print("No matching contact found.")

    number = input("Enter a phone number for reverse lookup (or press Enter to skip): ").strip()
    if number:
        owner = number_owner(number)
        if owner:
            print(f"{number} belongs to {owner}.")
        else:
            print("Number not found.")


def show_reports():
    # Reverse lookup dictionary created with a dictionary comprehension.
    reverse_lookup = {
        phone: name
        for name, data in contacts.items()
        for phone in data["phones"]
    }
    print("\nNumber -> name reverse lookup:")
    print(reverse_lookup)

    city_groups = {}
    for name, data in contacts.items():
        city_groups.setdefault(data["city"], []).append(name)
    for names in city_groups.values():
        names.sort()
    print("\nContacts grouped by city:", city_groups)

    multiple_numbers = sorted([
        name for name, data in contacts.items() if len(data["phones"]) > 1
    ])
    print("\nContacts with more than one number:", multiple_numbers)

    print("\nComplete directory (alphabetical):")
    if not contacts:
        print("Directory is empty.")
    for name in sorted(contacts):
        data = contacts[name]
        print(f"{name}:")
        print("  Phone numbers:", ", ".join(data["phones"]))
        print("  Email:", data["email"])
        print("  City:", data["city"])


def main():
    while True:
        print("\n===== PHONE DIRECTORY =====")
        print("1. Add contact")
        print("2. Add another number")
        print("3. Update email or city")
        print("4. Delete contact")
        print("5. Search")
        print("6. Reports")
        print("7. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            add_number()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            search_contact()
        elif choice == "6":
            show_reports()
        elif choice == "7":
            print("Exiting Phone Directory.")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
