from models import Book
from storage import Storage

class BookManager:
    """
    Manages book-related operations in the library system.

    Attributes:
        storage (Storage): The storage handler for books.
        books (list): The list of books in the library.
    """
    def __init__(self, storage_file):
        """
        Initializes the BookManager with the given storage file.

        Args:
            storage_file (str): The file path to load and save book data.
        """
        self.storage = Storage(storage_file)
        self.books = [Book(**book) for book in self.storage.load()]

    def add_book(self, title, author, isbn):
        """
        Adds a new book to the collection.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        if not title or not author or not isbn:
            print("All fields are required.")
            return

        if any(book.isbn == isbn for book in self.books):
            print("Book with this ISBN already exists.")
            return
        
        book = Book(title, author, isbn)
        self.books.append(book)
        self._save()
        print("Book added successfully.")

    def update_book(self, isbn, title=None, author=None):
        """
        Updates the details of an existing book.

        Args:
            isbn (str): The ISBN of the book to be updated.
            title (str, optional): The new title of the book.
            author (str, optional): The new author of the book.
        """
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self._save()
                print("Book updated successfully.")
                return
        print("Book with this ISBN does not exist.")

    def delete_book(self, isbn):
        """
        Deletes a book from the collection.

        Args:
            isbn (str): The ISBN of the book to be deleted.
        """
        self.books = [book for book in self.books if book.isbn != isbn]
        self._save()
        print("Book deleted successfully.")

    def list_books(self):
        """
        Lists all books in the collection.
        """
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(book)

    def search_books(self, title=None, author=None, isbn=None):
        """
        Searches for books based on various attributes.

        Args:
            title (str, optional): The title of the book to search for.
            author (str, optional): The author of the book to search for.
            isbn (str, optional): The ISBN of the book to search for.
        """
        results = [book for book in self.books if
                   (title and book.title == title) or
                   (author and book.author == author) or
                   (isbn and book.isbn == isbn)]

        if not results:
            print("No books found.")
        else:
            for book in results:
                print(book)

    def _save(self):
        """
        Saves the current state of the books to storage.
        """
        self.storage.save([book.to_dict() for book in self.books])
