import os
import platform

# Get the current working directory (in this case it's the folder which this file is)
print(os.getcwd())

# The difference between absolute and relative file path is that the absolute file path always begin with the
# root folder and relative file paths do not

# Checks if the string is an absolute path or not (return either True or False)
print(os.path.isabs('C:\Shyrine\PycharmProjects\study-python\day-8.png'))

# Returns the directory path of a file
print(os.path.dirname('C:\Shyrine\PycharmProjects\study-python\day-8.png'))

# Returns the last part of the file path
print(os.path.basename('C:\Shyrine\PycharmProjects\study-python\day-8.png'))

# Returns either True or False depending if the said file is really in the computer
print(os.path.exists(r"C:\Users\Shyrine\Pictures\day-8.png"))

# Returns either True or False depending if the said string is a file
print(os.path.isfile(r"C:\Users\Shyrine\Pictures\day-8.png"))

# Returns either True or False depending if the said string is a folder
print(os.path.isdir(r"C:\Users\Shyrine\Pictures\day-8.png"))

# Returns the size of the file
print(os.path.getsize(r"C:\Users\Shyrine\Videos\World full of data.mp4"))

# Returns the size of the file
print(os.listdir(r"C:\Users\Shyrine\Documents\Paradox Interactive"))

# Checks the total size of the folder from its files
total_size = 0
for filename in os.listdir(r"C:\Users\Shyrine\Pictures\No Mans Sky"):
    if not os.path.isfile(os.path.join(r"C:\Users\Shyrine\Pictures\No Mans Sky", filename)):
        continue
    total_size = total_size + os.path.getsize(os.path.join(r"C:\Users\Shyrine\Pictures\No Mans Sky", filename))

print(total_size)

# Create directories
# os.makedirs(r"C:\Users\Shyrine\Pictures\loco")

# Check what OS you are running
print(platform.system())

# Opens a text file (tried using docx but returns an error, apparently can't do it so you need external lib like docx2txt)
open_practice = open(r"C:\Users\Shyrine\Downloads\os_open_practice.txt")
content = open_practice.read()
print(content)
