import os

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
        print("6. Sort contacts ")
        print("7. Return to Address Book System menu")
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
                self.sort_menu()
                
            case 7:
                return False  
            case _:
                print("Invalid choice. Please try again.")
                
        return True

    def search_contact_by_city_or_state(self, location_type, location_value):
        """
        Description:
        This function searches for contacts in the Address Book by city or state.
        Parameter:
        self : Refers to the instance of the class AddressBook
        location_type : 'city' or 'state' - indicates the type of location to search by
        location_value : The value of the city or state to search for
        Return:
        list: A list of matching contacts
        """
        matches = []
        for contact in self.contacts:
            if contact[location_type].lower() == location_value.lower():
                matches.append(contact)
        return matches

    def sort_contacts_by_name(self):
        """
        Description:
        This function sorts the contacts in the Address Book alphabetically by the person's name (first name, then last name).
        Parameter:
        self : Refers to the instance of the class AddressBook
        Return:
        None
        """
        self.contacts.sort(key=lambda contact: (contact['first_name'].lower(), contact['last_name'].lower()))
        print("Contacts sorted alphabetically by name.")
        
    def sort_contacts_by_city(self):
        """
        Description:
        This function sorts the contacts in the Address Book alphabetically by the city name.
        Parameter:
        self : Refers to the instance of the class AddressBook
        Return:
        None
        """
        self.contacts.sort(key=lambda contact: contact['city'].lower())
        print("Contacts sorted alphabetically by city.")

    def sort_contacts_by_state(self):
        """
        Description:
        This function sorts the contacts in the Address Book alphabetically by the state name.
        Parameter:
        self : Refers to the instance of the class AddressBook
        Return:
        None
        """
        self.contacts.sort(key=lambda contact: contact['state'].lower())
        print("Contacts sorted alphabetically by state.")

    def sort_contacts_by_zip(self):
        """
        Description:
        This function sorts the contacts in the Address Book by the zip code in ascending order.
        Parameter:
        self : Refers to the instance of the class AddressBook
        Return:
        None
        """
        self.contacts.sort(key=lambda contact: contact['zip_code'])
        print("Contacts sorted by zip code.")

    def sort_menu(self):
        """
        Description:
        Displays a sorting menu for the user to choose the sorting criterion.
        Parameter:
        self : Refers to the instance of the class AddressBook
        Return:
        None
        """
        print("\nSort contacts by:")
        print("1. Name")
        print("2. City")
        print("3. State")
        print("4. Zip Code")
        sort_choice = int(input("Enter your choice: "))

        match sort_choice:
            case 1:
                self.sort_contacts_by_name()
            case 2:
                self.sort_contacts_by_city()
            case 3:
                self.sort_contacts_by_state()
            case 4:
                self.sort_contacts_by_zip()
            case _:
                print("Invalid choice. Sorting by Name by default.")
                self.sort_contacts_by_name()

        self.display_contacts()

    def to_text(self):
        """
        Description:
        This function converts the Address Book contacts to a text format suitable for saving to a file.
        Parameter:
        self : Refers to the instance of the class AddressBookSystem
        Return:
        lines : A multi-line string, where each line represents one contact.
        """
        lines = []
        for contact in self.contacts:
            lines.append(f"{contact['first_name']}|{contact['last_name']}|{contact['address']}|{contact['city']}|"
                         f"{contact['state']}|{contact['zip_code']}|{contact['phone_number']}|{contact['email']}")
        return "\n".join(lines)

    def from_text(self, contact_lines):
        """
        Description:
        This function loads contacts from a text format (used when reading from a file).
        Parameter:
        self : Refers to the instance of the class AddressBookSystem
        contact_lines : List of contacts from data is loaded.
        Return:
        None
        """
        for line in contact_lines:
            if line.strip():  
                fields = line.split("|")
                if len(fields) == 8: 
                    first_name, last_name, address, city, state, zip_code, phone_number, email = fields
                    contact = {
                        'first_name': first_name,
                        'last_name': last_name,
                        'address': address,
                        'city': city,
                        'state': state,
                        'zip_code': int(zip_code),
                        'phone_number': int(phone_number),
                        'email': email
                    }
                    self.contacts.append(contact)
                else:
                    print(f"Skipping invalid line: {line}")


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

    def search_person_in_city_or_state(self):
        """
        Description:
        This function searches for a person in a city or state across all Address Books.
        Parameter:
        self : Refers to the instance of the class AddressBookSystem
        Return:
        None
        """
        location_type = input("Search by 'city' or 'state': ").strip().lower()
        if location_type not in ['city', 'state']:
            print("Invalid option. Please enter 'city' or 'state'.")
            return

        location_value = input(f"Enter the {location_type} name to search for: ").strip()

        found_contacts = []

        for book_name, address_book in self.address_books.items():
            matches = address_book.search_contact_by_city_or_state(location_type, location_value)
            if matches:
                found_contacts.append((book_name, matches))

        if not found_contacts:
            print(f"No contacts found in any Address Book for {location_type.capitalize()}: {location_value}")
        else:
            print(f"\nContacts found in {location_type.capitalize()}: {location_value}")
            for book_name, contacts in found_contacts:
                print(f"\nAddress Book: {book_name}")
                for contact in contacts:
                    print(f"  - {contact['first_name']} {contact['last_name']}, {contact['city']}, {contact['state']}")

    def display_all_data_for_city_or_state(self):
        """
        Description:
        This function takes a city or state from the user and displays all the data 
        of persons from all Address Books in the system for that city or state.
        Parameter:
        self : Refers to the instance of the class AddressBookSystem
        Return:
        None
        """
        location_type = input("Enter 'city' or 'state': ").strip().lower()
        if location_type not in ['city', 'state']:
            print("Invalid option. Please enter 'city' or 'state'.")
            return

        location_value = input(f"Enter the {location_type} to display all data for: ").strip()

        found_contacts = []

        for book_name, address_book in self.address_books.items():
            matches = address_book.search_contact_by_city_or_state(location_type, location_value)
            if matches:
                found_contacts.append((book_name, matches))

        if not found_contacts:
            print(f"No contacts found in any Address Book for {location_type.capitalize()}: {location_value}")
        else:
            print(f"\nAll contacts found in {location_type.capitalize()}: {location_value}")
            for book_name, contacts in found_contacts:
                print(f"\nAddress Book: {book_name}")
                for contact in contacts:
                    print(f"  - {contact['first_name']} {contact['last_name']}, {contact['address']}, {contact['city']}, {contact['state']}, {contact['zip_code']}, {contact['phone_number']}, {contact['email']}")

    def count_contacts_by_city_or_state(self):
        """
        Description:
        This function counts the number of contact persons by city or state across all Address Books in the system.
        Parameter:
        self : Refers to the instance of the class AddressBookSystem
        Return:
        None
        """
        location_type = input("Enter 'city' or 'state': ").strip().lower()
        if location_type not in ['city', 'state']:
            print("Invalid option. Please enter 'city' or 'state'.")
            return

        location_value = input(f"Enter the {location_type} to count contacts for: ").strip()

        total_count = 0

        for book_name, address_book in self.address_books.items():
            matches = address_book.search_contact_by_city_or_state(location_type, location_value)
            count = len(matches)
            total_count += count
            if count > 0:
                print(f"{count} contacts found in Address Book: {book_name}")

        print(f"\nTotal number of contacts found in {location_type.capitalize()}: {location_value} is {total_count}")

    def write_to_file(self, filename):
        """
        Description:
        This fuction saves all address books and their contacts to a text file.
        Parameter:
        self : Refers to the instance of the class AddressBookSystem
        filename : Filename of file to save data.
        Return:
        None
        """
        with open(filename, 'w') as file:
            for book_name, book in self.address_books.items():
                file.write(f"AddressBook:{book_name}\n")
                file.write(book.to_text())
                file.write("\n---\n")
        print(f"Data saved to {filename}.")

    def read_from_file(self, filename):
        """
        Description:
        This function loads address books and contacts from a text file.
        Parameter:
        self : Refers to the instance of the class AddressBookSystem
        filename : Filename of file from the data is loaded.
        Return:
        None
        """
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                content = file.read().strip()
                sections = content.split("\n---\n")

                for section in sections:
                    lines = section.splitlines()
                    if lines[0].startswith("AddressBook:"):
                        book_name = lines[0].split(":")[1]
                        contacts = lines[1:]
                        if book_name not in self.address_books:
                            self.address_books[book_name] = AddressBook()
                        self.address_books[book_name].from_text(contacts)
            print(f"Data loaded from {filename}.")
        else:
            print(f"File '{filename}' does not exist.")

def main():
    
    address_book_system = AddressBookSystem()

    while True:
        print("\n1. Add a new Address Book")
        print("2. Select an Address Book")
        print("3. List all Address Books")
        print("4. Search Person by City or State")
        print("5. Display all data for a City or State")
        print("6. Count contacts by City or State")
        print("7. Save Address Books to file")
        print("8. Load Address Books from file")
        print("9. Exit")
        
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
                address_book_system.search_person_in_city_or_state()
                
            case 5:
                address_book_system.display_all_data_for_city_or_state()
                    
            case 6:
                address_book_system.count_contacts_by_city_or_state()
                    
            case 7:
                filename = input("Enter the filename to save data: ")
                address_book_system.write_to_file(filename)
                
            case 8:
                filename = input("Enter the filename to load data: ")
                address_book_system.read_from_file(filename)
                
            case 9:
                print("Exiting the Address Book System. Goodbye!")
                break
            
            case _:
                print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()
        