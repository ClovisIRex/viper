class FileContentMismatchError(OSError):
    """
    Exception raised when the contents of a file have changed
    unexpectedly.
    """
    def __init__(self, path, message=None):
        self.path = path
        if message is not None:
            self.message = message
        else:
            self.message = 'unexpected contents'

    def __str__(self):
        return "{}: '{}'".format(self.message, self.path)

    def __repr__(self):
        return self.__name__
