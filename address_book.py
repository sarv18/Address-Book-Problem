
class AddressBook:
    def __init__(self):
        self.contacts = []
        
    def menu(self):
        """
            Description:
            This fuction prints menu for user operations.
            Parameter:
            self : Refers to the instance of the class AddressBook
            Return:
            choice: User's choice for operation.
        """
        print("Welcome to Address Book\nEnter any option given below:")
        print("1. Add a contact in Address Book")
        print("2. Edit a contact from Address Book")
        print("3. Delete a existing contact from Address Book")
        print("4. Add multiple contact ")
        print("5. Display all contacts")
        print("6. Return to Address Book System menu")
        choice = int(input("Enter your choice: "))
        return choice

    def create_contact(self):
        """
            Description:
            This fuction takes input from user for each parameter
            Parameter:
            self : Refers to the instance of the class AddressBook
            Return:
            None
        """
        
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        
        for contact in self.contacts:
            if contact['first_name'] == first_name and contact['last_name'] == last_name:
                print("This contact already exists..")
                return
        
        address = input("Enter Address : ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = int(input("Enter Zip Code: "))
        phone_number = int(input("Enter Phone Number: "))
        email = input("Enter Email address: ")
        
        contact = {
            'first_name': first_name,
            'last_name': last_name,
            'address': address,
            'city': city,
            'state': state,
            'zip_code': zip_code,
            'phone_number': phone_number,
            'email': email
        }
        self.contacts.append(contact)
        print("Contact added successfully!")
        
    def edit_contact(self, contact):
        """
            Description:
            This fuction takes input from user for edited contact
            Parameter:
            self : Refers to the instance of the class AddressBook
            contact: Contact dictionary containing contact of recent user
            Return:
            None
        """
        contact['first_name'] = input("Enter new First Name: ")
        contact['last_name'] = input("Enter new Last Name: ")
        contact['address'] = input("Enter new Address: ")
        contact['city'] = input("Enter new City: ")
        contact['state'] = input("Enter new State: ")
        contact['zip_code'] = int(input("Enter new Zip code: "))
        contact['phone_number'] = int(input("Enter new Phone number: "))
        contact['email'] = input("Enter new Email address: ")
        
        print("Contact updated successfully!")
            
    
    def del_contact(self):
        """
            Description:
            This fuction deletes details of the person.
            Parameter:
            self : Refers to the instance of the class AddressBook
            Return:
            None
        """
        full_name1 = input("Enter full name of the person to delete: ")
        contact_found = False
        for contact in self.contacts:
            if full_name1 == f"{contact['first_name']} {contact['last_name']}":
                self.contacts.remove(contact)
                contact_found = True
                print("Person details deleted successfully..")
                break
            
        if not contact_found:
            print("There is no existing contact with this name.")

    def add_multiple_contacts(self):
        """
            Description:
            This fuction to add multiple contacts.
            Parameter:
            self : Refers to the instance of the class AddressBook
            Return:
            None
        """
          
        data_add_count = int(input("Enter the number of contacts you want to add: "))
        for i in range(data_add_count):
            print(f"\nAdding contact {i + 1}...")
            self.create_contact() 
            print("Contacts added successfully!")

    def display_contacts(self):
        """
            Description:
            This fuction Displays all the contacts.
            Parameter:
            self : Refers to the instance of the class AddressBook
            Return:
            None
        """
        if not self.contacts:
            print("No contacts to display..")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {idx}:")
                for key, value in contact.items():
                    print(f"{key}: {value}")


    def selection(self, choice):
        """
            Description:
            This fuction takes input as choice.
            Parameter:
            self : Refers to the instance of the class AddressBook
            choice: Choice of option from user
            Return:
            None
        """
        
        match choice:
            case 1:
                self.create_contact()
            
            case 2:
                full_name = input("Enter the Full Name (To check for edit): ")
                for contact in self.contacts:
                    if full_name == f"{contact['first_name']} {contact['last_name']}":
                        self.edit_contact(contact)
                        break
                    else:
                        print("There is no existing contact with this name.")
                        
            case 3:
                self.del_contact()
                
            case 4:
                self.add_multiple_contacts()
                
            case 5:
                self.display_contacts()
            
            case 6:
                return False  
            case _:
                print("Invalid choice. Please try again.")
                
        return True


class AddressBookSystem:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self):
        """
        Description:
        This function creates a new Address Book with a unique name.
        Parameter:
        self : Refers to the instance of the class AddressBookSystem
        Return:
        None
        """
        name = input("Enter a unique name for the new Address Book: ")
        if name in self.address_books:
            print("An Address Book with this name already exists. Please choose a different name.")
        else:
            self.address_books[name] = AddressBook()
            print(f"Address Book '{name}' created successfully!")

    def select_address_book(self):
        """
        Description:
        This function selects an existing Address Book by name.
        Parameter:
        self : Refers to the instance of the class AddressBookSystem
        Return:
        selected_book: The selected Address Book instance.
        """
        name = input("Enter the name of the Address Book you want to select: ")
        if name in self.address_books:
            return self.address_books[name]
        else:
            print("No Address Book found with this name.")
            return None

    def list_address_books(self):
        """
        Description:
        This function lists all the available Address Books.
        Parameter:
        self : Refers to the instance of the class AddressBookSystem
        Return:
        None
        """
        if not self.address_books:
            print("No Address Books available.")
        else:
            print("Available Address Books:")
            for name in self.address_books:
                print(f"- {name}")


def main():
    
    address_book_system = AddressBookSystem()

    while True:
        print("\n1. Add a new Address Book")
        print("2. Select an Address Book")
        print("3. List all Address Books")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                address_book_system.add_address_book()
            case 2:
                selected_book = address_book_system.select_address_book()
                if selected_book:
                    while True:
                        user_choice = selected_book.menu()
                        if not selected_book.selection(user_choice):
                            break
            case 3:
                address_book_system.list_address_books()
            case 4:
                print("Exiting the Address Book System. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()
        