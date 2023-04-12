# Using os.path.join on Windows:

import os

print(os.path.join('usr', 'bin', 'spam'))

"""Absolute vs. Relative paths

There are two ways to specify a file path.

    An absolute path, which always begins with the root folder
    A relative path, which is relative to the program’s current working directory
    """