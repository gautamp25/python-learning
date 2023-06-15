"""
File System Structure-
    - At the top, there are one or more root nodes.
    - Each root node contains files and folders, which can contain more files and subfolders.
    - A file can be identified through its path in the file system starting with root node.
    - A files Absolute path contains root node and require no context to locate the file.
    - A given path is either relative or absolute
    - A relative path requires context.
    - There can be several relative paths, but only one absolute path.

    ** The file system control storage and retrieval of files.

    

How can we create a directory with the Pathlib module?
Ans-    dir_path = Path("logs/")
        dir_path.mkdir()

How can we retrieve the file names that have the following sequence at the end of their file path?
 -2020.png
 Ans- glob.glob('*-2020.png')



How does the Pathlib module represent paths?
    with an object
    Correct 

"""

# count files in folder and its subfolder

import os
from pathlib import Path

def count_files_with_os_walk(path):
    total = 0
    for base,subdirs,files in os.walk(path):
        for _ in files:
            total+= 1
            # print(file)
    return total

def count_files_with_scandir(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total+= 1
        else:
            total+=count_files_with_scandir(entry)
    return total

def count_files_with_pathlib(path):
    total = 0
    for entry in Path(path).iterdir():
        if entry.is_file():
            total+=1
        else:
            total+= count_files_with_pathlib(entry)
    return total

if __name__ == "__main__":
    print("Count with count_files_with_os_walk",count_files_with_os_walk("."))
    print("Count with count_files_with_scandir",count_files_with_scandir("."))
    print("Count with count_files_with_pathlib",count_files_with_pathlib("."))