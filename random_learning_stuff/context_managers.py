with open('some_file.txt', 'w') as opened_file:
    opened_file.write('Hola!')


file = open('some_file.txt', 'r')
try:
    print(file.read())
finally:
    file.close()

"""At the very least a context manager has an __enter__ and __exit__
method defined."""

class File:
    """__exit__ method accepts three arguments. They are required by
    every __exit__ method which is a part of a Context Manager class.
    -----------------------------------------------------------------
    The with statement stores the __exit__ method of the File class.
    It calls the __enter__ method of the File class.
    The __enter__ method opens the file and returns it.
    The opened file handle is passed to opened_file.
    We write to the file using .write().
    The with statement calls the stored __exit__ method.
    The __exit__ method closes the file.
    """
    def __init__(self, file_name, method) -> None:
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
