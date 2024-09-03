def menu():
    """
        Description:
        This fuction prints menu for user operations.
        Parameter:
        None
        Return:
        choice: User's choice for operation.
    """
    print("Welcome to Address Book\nEnter any option given below:")
    print("1. Add the contacts in address book")
    choice = int(input("Enter your choice: "))
    return choice

def create_contact():
    """
        Description:
        This fuction takes input from user for each parameter
        Parameter:
        None
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


def selection(choice):
    """
        Description:
        This fuction takes input as choice.
        Parameter:
        choice: Choice of option from user
        Return:
        None
    """
    
    match choice:
        case 1:
            create_contact()
        case _:
            print("Invalid choice. Please try again.")

def main():
    
    user_choice = menu()
    selection(user_choice)
    
if __name__ == "__main__":
    main()
        