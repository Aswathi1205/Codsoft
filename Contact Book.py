class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
contacts = []

def add_contact(name, phone, email):
    contact = Contact(name, phone, email)
    contacts.append(contact)

def view_contacts():
    for contact in contacts:
        print(contact)

def search_contact(name):
    for contact in contacts:
        if contact.name == name:
            print(contact)
            return
    print("Contact not found.")

def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact.name != name]
def menu():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
