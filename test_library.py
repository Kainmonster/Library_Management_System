import unittest
import logging
from io import StringIO

from book_management import BookManager
from user_management import UserManager
from checkout_management import CheckoutManager

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager('test_books.json')
        self.user_manager = UserManager('test_users.json')
        self.checkout_manager = CheckoutManager('test_checkouts.json')
        # Clear existing data for clean tests
        self.book_manager.books = []
        self.user_manager.users = []
        self.checkout_manager.checkouts = []
        self.book_manager._save()
        self.user_manager._save()
        self.checkout_manager._save()

        # Set up logging
        self.log_stream = StringIO()
        logging.basicConfig(stream=self.log_stream, level=logging.INFO, format='%(message)s')

    def test_add_book(self):
        self.book_manager.add_book("Test Title", "Test Author", "123456")
        log_output = self.log_stream.getvalue()
        self.assertIn("Book added: Test Title by Test Author", log_output)

    def test_search_books(self):
        self.book_manager.add_book("Test Title", "Test Author", "123456")
        self.book_manager.search_books(title="Test Title")
        log_output = self.log_stream.getvalue()
        self.assertIn("Book found: Test Title by Test Author", log_output)

    def test_logging_operations(self):
        self.book_manager.add_book("Test Title", "Test Author", "123456")
        self.user_manager.add_user("Test User", "U001")
        log_output = self.log_stream.getvalue()
        self.assertIn("Book added: Test Title by Test Author", log_output)
        self.assertIn("User added: Test User with ID U001", log_output)

    def test_list_books(self):
        self.book_manager.add_book("Test Title", "Test Author", "123456")
        self.book_manager.list_books()
        log_output = self.log_stream.getvalue()
        self.assertIn("Book listed: Test Title by Test Author", log_output)

if __name__ == "__main__":
    unittest.main()
