from models import User
from storage import Storage

class UserManager:
    """
    Manages user-related operations in the library system.

    Attributes:
        storage (Storage): The storage handler for users.
        users (list): The list of users in the system.
    """

    def __init__(self, storage_file):
        """
        Initializes the UserManager with the given storage file.

        Args:
            storage_file (str): The file path to load and save user data.
        """
        self.storage = Storage(storage_file)
        self.users = [User(**user) for user in self.storage.load()]

    def add_user(self, name, user_id):
        """
        Adds a new user to the system. Checks for duplicate user IDs and names.

        Args:
            name (str): The name of the user.
            user_id (str): The unique ID of the user.
        """
        if not name or not user_id:
            print("Both name and user ID are required.")
            return

        if any(user.user_id == user_id for user in self.users):
            print("User ID already exists. Please enter a different User ID.")
            return
        
        if any(user.name == name for user in self.users):
            print("User with this name already exists. Please enter a different name.")
            return
        
        user = User(name, user_id)
        self.users.append(user)
        self._save()
        print(f"User '{name}' with ID '{user_id}' added successfully.")

    def update_user(self, user_id, name=None):
        """
        Updates the details of an existing user.

        Args:
            user_id (str): The ID of the user to be updated.
            name (str, optional): The new name of the user.
        """
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                self._save()
                print("User updated successfully.")
                return
        print("User with this ID does not exist.")

    def delete_user(self, user_id):
        """
        Deletes a user from the system.

        Args:
            user_id (str): The ID of the user to be deleted.
        """
        self.users = [user for user in self.users if user.user_id != user_id]
        self._save()
        print("User deleted successfully.")

    def list_users(self):
        """
        Lists all users in the system.
        """
        if not self.users:
            print("No users available.")
        else:
            for user in self.users:
                print(user)

    def search_users(self, name=None, user_id=None):
        """
        Searches for users based on various attributes.

        Args:
            name (str, optional): The name of the user to search for.
            user_id (str, optional): The ID of the user to search for.
        """
        results = [user for user in self.users if
                   (name and user.name == name) or
                   (user_id and user.user_id == user_id)]

        if not results:
            print("No users found.")
        else:
            for user in results:
                print(user)

    def _save(self):
        """
        Saves the current state of the users to storage.
        """
        self.storage.save([user.to_dict() for user in self.users])

