import json

class Storage:
    """
    Handles file-based storage for library data.

    Attributes:
        file_name (str): The name of the file used for storage.
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, data):
        """
        Saves data to a file in JSON format.

        Args:
            data (list): The data to be saved.
        """
        with open(self.file_name, 'w') as f:
            json.dump(data, f, indent=4)

    def load(self):
        """
        Loads data from a file. If the file does not exist, returns an empty list.

        Returns:
            list: The loaded data.
        """
        try:
            with open(self.file_name, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
