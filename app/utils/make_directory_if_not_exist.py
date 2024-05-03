import os

def make_directory_if_not_exists(directory: str):
    """Make a directory if it doesn't exist
    
    Keyword arguments:
    directory(str) -- The directory to create
    Return: None
    """
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    