from models import Checkout
from storage import Storage

class CheckoutManager:
    """
    Manages book checkout operations in the library system.

    Attributes:
        storage (Storage): The storage handler for checkouts.
        checkouts (list): The list of book checkouts.
    """
    def __init__(self, storage_file):
        """
        Initializes the CheckoutManager with the given storage file.

        Args:
            storage_file (str): The file path to load and save checkout data.
        """
        self.storage = Storage(storage_file)
        self.checkouts = [Checkout(**checkout) for checkout in self.storage.load()]

    def checkout_book(self, user_id, isbn):
        """
        Records the checkout of a book by a user.

        Args:
            user_id (str): The ID of the user checking out the book.
            isbn (str): The ISBN of the book being checked out.
        """
        if any(checkout.isbn == isbn for checkout in self.checkouts):
            print("Book is already checked out.")
            return

        checkout = Checkout(user_id, isbn)
        self.checkouts.append(checkout)
        self._save()
        print("Book checked out successfully.")

    def checkin_book(self, isbn):
        """
        Records the check-in of a book.

        Args:
            isbn (str): The ISBN of the book being checked in.
        """
        self.checkouts = [checkout for checkout in self.checkouts if checkout.isbn != isbn]
        self._save()
        print("Book checked in successfully.")

    def list_checkouts(self):
        """
        Lists all book checkouts.
        """
        if not self.checkouts:
            print("No checkouts available.")
        else:
            for checkout in self.checkouts:
                print(checkout)

    def _save(self):
        """
        Saves the current state of the checkouts to storage.
        """
        self.storage.save([checkout.to_dict() for checkout in self.checkouts])

