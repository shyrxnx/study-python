import os

# Write a program that counts the number of files in a directory (excluding directories themselves).

print(os.listdir(r"..\..\Downloads\JPCS Picture Layouts"))

main_directory = r"..\..\Downloads\JPCS Picture Layouts"
file = r"..\..\Downloads\JPCS Picture Layouts\logo.png"
count = 0


# Checks if the path given is a file or not (folder)
def check_if_file():
    return os.path.isfile(main_directory)


if check_if_file():
    print("The path is a file")
else:
    print("The path is a folder")


# Checks if the path given is a folder or not (file)
def check_if_folder():
    return os.path.isdir(file)


if check_if_folder():
    print("The path is a folder")
else:
    print("The path is a file")
