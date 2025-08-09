class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("\n--- Add New Contact ---")
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def view_contacts(self):
        print("\n--- Contact List ---")
        if not self.contacts:
            print("No contacts found.")
            return
        for i, contact in enumerate(self.contacts, start=1):
            print(f"\nContact #{i}")
            print(contact)

    def search_contact(self):
        print("\n--- Search Contact ---")
        query = input("Enter name or phone number to search: ").lower()
        found = False
        for contact in self.contacts:
            if query in contact.name.lower() or query in contact.phone:
                print("\nContact Found:")
                print(contact)
                found = True
                break
        if not found:
            print("No matching contact found.")

    def update_contact(self):
        print("\n--- Update Contact ---")
        name = input("Enter the name of the contact to update: ").lower()
        for contact in self.contacts:
            if contact.name.lower() == name:
                print("\nCurrent Details:")
                print(contact)
                contact.name = input("Enter new name: ")
                contact.phone = input("Enter new phone: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self):
        print("\n--- Delete Contact ---")
        name = input("Enter the name of the contact to delete: ").lower()
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name:
                print("\nContact Found:")
                print(contact)
                confirm = input("Are you sure you want to delete this contact? (y/n): ").lower()
                if confirm == 'y':
                    del self.contacts[i]
                    print("Contact deleted successfully.")
                else:
                    print("Deletion cancelled.")
                return
        print("Contact not found.")

    def menu(self):
        while True:
            print("\n--- Contact Management System ---")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Management System. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    cm = ContactManager()
    cm.menu()
