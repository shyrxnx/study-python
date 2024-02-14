import os

# Create a script that takes a list of directory names as input and creates those directories
# within a specified parent directory.

print(os.getcwd())

print("===============================")

# os.makedirs(r"C:\Users\Shyrine\Desktop\new")

folder_names = input("Enter the folder names you want to create separated by a comma. (Ex. folder1, "
                     "folder2, etc...\nEnter folder name/s: ").split(", ")

print(f"These are the folder that will be created: {folder_names}")

print("===============================")

for folder in folder_names:
    print(folder)

print("===============================")

print(os.path.relpath(r"C:\Users\Shyrine\Desktop"))

print("===============================")

root_path = r"..\..\Desktop"

for folder in folder_names:
    os.makedirs(os.path.join(r"C:\Users\Shyrine\Desktop", folder))


