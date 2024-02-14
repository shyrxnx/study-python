import os

# Create a script that calculates the total size of all files in a directory.

directory_path = r"C:\Users\Shyrine\Downloads\JPCS Picture Layouts"


def calculate_total_size(directory):
    total_size = 0
    # Walk through all directories and subdirectories starting from the specified directory
    for main_directory, sub_directory, files in os.walk(directory):
        # Iterate over the files in the current directory
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(main_directory, file)
            # Add the size of the file to the total size
            total_size += os.path.getsize(file_path)
    return total_size


# Call the function to calculate the total size of all files in the directory and its subdirectories
calculated_size = calculate_total_size(directory_path)

print(f"The total size of the directory is: {calculated_size}")
