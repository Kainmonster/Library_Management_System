from book_management import BookManager
from user_management import UserManager
from checkout_management import CheckoutManager

# Initialize managers with respective storage files
book_manager = BookManager('books.json')
user_manager = UserManager('users.json')
checkout_manager = CheckoutManager('checkouts.json')

def print_header(title):
    """
    Prints a header with the given title for better visibility.
    """
    print("\n" + "="*40)
    print(f"{title}".center(40))
    print("="*40)

def main_menu():
    """
    Displays the main menu and returns the user's choice.

    Returns:
        str: The user's menu choice.
    """
    print_header("Library Management System")
    print()
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Manage Checkouts")
    print("4. Exit")
    print()
    return input("Enter your choice: ")

def manage_books():
    """
    Manages book-related operations.
    """
    while True:
        print_header("Book Management")
        print()
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. List Books")
        print("5. Search Books")
        print("6. Back")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            if title and author and isbn:
                book_manager.add_book(title, author, isbn)
            else:
                print("All fields are required.")
        elif choice == '2':
            print()
            isbn = input("Enter book ISBN to update: ").strip()
            title = input("Enter new book title (leave blank to keep current): ").strip()
            author = input("Enter new book author (leave blank to keep current): ").strip()
            book_manager.update_book(isbn, title, author)
        elif choice == '3':
            print()
            isbn = input("Enter book ISBN to delete: ").strip()
            book_manager.delete_book(isbn)
        elif choice == '4':
            print()
            book_manager.list_books()
        elif choice == '5':
            print()
            title = input("Enter book title (leave blank to skip): ").strip()
            author = input("Enter book author (leave blank to skip): ").strip()
            isbn = input("Enter book ISBN (leave blank to skip): ").strip()
            print()
            book_manager.search_books(title, author, isbn)
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

def manage_users():
    """
    Manages user-related operations.
    """
    while True:
        print_header("User Management")
        print()
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. List Users")
        print("5. Search Users")
        print("6. Back")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            name = input("Enter user name: ").strip()
            user_id = input("Enter user ID: ").strip()
            if name and user_id:
                user_manager.add_user(name, user_id)
            else:
                print("Both name and user ID are required.")
        elif choice == '2':
            print()
            user_id = input("Enter user ID to update: ").strip()
            name = input("Enter new user name (leave blank to keep current): ").strip()
            user_manager.update_user(user_id, name)
        elif choice == '3':
            print()
            user_id = input("Enter user ID to delete: ").strip()
            user_manager.delete_user(user_id)
        elif choice == '4':
            print()
            user_manager.list_users()
        elif choice == '5':
            print()
            name = input("Enter user name (leave blank to skip): ").strip()
            user_id = input("Enter user ID (leave blank to skip): ").strip()
            print()
            user_manager.search_users(name, user_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

def manage_checkouts():
    """
    Manages book checkout and check-in operations.
    """
    while True:
        print_header("Checkout Management")
        print()
        print("1. Checkout Book")
        print("2. Checkin Book")
        print("3. List Checkouts")
        print("4. Back")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            user_id = input("Enter user ID: ").strip()
            isbn = input("Enter book ISBN to checkout: ").strip()
            print()
            checkout_manager.checkout_book(user_id, isbn)
        elif choice == '2':
            print()
            isbn = input("Enter book ISBN to checkin: ").strip()
            print()
            checkout_manager.checkin_book(isbn)
        elif choice == '3':
            print()
            checkout_manager.list_checkouts()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def main():
    """
    Main function to run the library management system.
    """
    while True:
        choice = main_menu()
        if choice == '1':
            manage_books()
        elif choice == '2':
            manage_users()
        elif choice == '3':
            manage_checkouts()
        elif choice == '4':
            print()
            print("Exiting the system. Goodbye!")
            break
        else:
            print()
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
