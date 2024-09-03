
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
        print("1. Add the contacts in address book")
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
            case _:
                print("Invalid choice. Please try again.")

def main():
    
    address_book = AddressBook()
    user_choice = address_book.menu()
    address_book.selection(user_choice)
    
if __name__ == "__main__":
    main()
        