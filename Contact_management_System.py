class Contact:
    def __init__(self,name,phone_number,email):
        self.name=name
        self.phone_number=phone_number
        self.email=email

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name=input("Enter contact name: ")
        phone_number=input("Enter contact phone number: ")
        email=input("Enter contact email: ")
        self.contacts[name] = Contact(name, phone_number, email)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, contact in self.contacts.items():
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print("------------------------")

    def edit_contact(self):
        name=input("Enter contact name to edit: ")
        if name in self.contacts:
            contact = self.contacts[name]
            print("Enter new details (press enter to skip):")
            contact.name=input(f"Name ({contact.name}): ") or contact.name
            contact.phone_number=input(f"Phone Number ({contact.phone_number}): ") or contact.phone_number
            contact.email=input(f"Email ({contact.email}): ") or contact.email
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name=input("Enter contact name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

def main():
    contact_manager = ContactManager()
    while True:
        print("Contact Management Program")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Quit")
        choice=input("Enter your choice: ")
        if choice == "1":
            contact_manager.add_contact()
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            contact_manager.edit_contact()
        elif choice == "4":
            contact_manager.delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()