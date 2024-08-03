class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
    """
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn})"

    def to_dict(self):
        """
        Converts the Book instance to a dictionary.
        
        Returns:
            dict: The dictionary representation of the Book instance.
        """
        return {'title': self.title, 'author': self.author, 'isbn': self.isbn}


class User:
    """
    Represents a user in the library system.

    Attributes:
        name (str): The name of the user.
        user_id (str): The unique ID of the user.
    """
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"User(name={self.name}, user_id={self.user_id})"

    def to_dict(self):
        """
        Converts the User instance to a dictionary.
        
        Returns:
            dict: The dictionary representation of the User instance.
        """
        return {'name': self.name, 'user_id': self.user_id}


class Checkout:
    """
    Represents a book checkout transaction.

    Attributes:
        user_id (str): The ID of the user who checked out the book.
        isbn (str): The ISBN of the book being checked out.
    """
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn

    def __repr__(self):
        return f"Checkout(user_id={self.user_id}, isbn={self.isbn})"

    def to_dict(self):
        """
        Converts the Checkout instance to a dictionary.
        
        Returns:
            dict: The dictionary representation of the Checkout instance.
        """
        return {'user_id': self.user_id, 'isbn': self.isbn}

