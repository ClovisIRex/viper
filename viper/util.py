import os

from viper.exceptions import FileContentMismatchError


def verify_file(file_path, content=None):
    """
    Ensure file exists and content is accurate.

    :param file_path: path to file
    :param content: string to check file against
    :return: True if file matches
    """
    with open(file_path) as file:
        if type(content) == str:
            file_content = file.read()
            if file_content != content:
                raise FileContentMismatchError(file_path)
        elif content is None:
            pass
        else:
            raise TypeError(
                "expected a string, got {}".format(type(content))
            )
    return True


def create_file(file_path, content=None):
    """
    If file already exists, check that the contents are the same.
    If they are dissimilar, then raise an error.

    :param file_path: name of file to create
    :param content: string to write to file
    :return: True if successfully created a file
    """
    if type(content) == str:
        if os.path.isfile(file_path):
            try:
                verify_file(file_path, content)
            except FileContentMismatchError:
                raise FileExistsError(file_path)
        with open(file_path, "w") as file:
            file.write(content)
    else:
        with open(file_path, "w"):
            pass
    return True
