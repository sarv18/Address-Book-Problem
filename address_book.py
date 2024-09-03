
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
        for contact in self.contacts:
            contact['first_name'] = input("Enter new First Name: ")
            contact['last_name'] = input("Enter new Last Name: ")
            contact['address'] = input("Enter new Address: ")
            contact['city'] = input("Enter new City: ")
            contact['state'] = input("Enter new State: ")
            contact['zip_code'] = int(input("Enter new Zip code: "))
            contact['phone_number'] = int(input("Enter new Phone number: "))
            contact['email'] = input("Enter new Email address: ")
            
    
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
        for contact in self.contacts:
            if full_name1 == f"{contact['first_name']} {contact['last_name']}":
                self.contacts.remove(contact)
                print("Person details deleted successfully..")
            else:
                print("There is no existing contact with this name.")



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
                      
            case _:
                print("Invalid choice. Please try again.")

def main():
    
    address_book = AddressBook()
    
    while True:
        user_choice = address_book.menu()
        address_book.selection(user_choice)
        choice_to_exit = input("Do you want to continue ( yes / no ):")
        if choice_to_exit == 'no':
            break
    
if __name__ == "__main__":
    main()
        