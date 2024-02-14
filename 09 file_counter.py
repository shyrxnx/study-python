import os

# Write a program that counts the number of files and folders in a directory (excluding the directory provided itself).

main_directory = r"C:\Users\Shyrine\Downloads\JPCS Picture Layouts"


def count_files_and_folders(directory):
    files_count = 0
    folders_count = 0

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            files_count += 1
        elif os.path.isdir(item_path):
            folders_count += 1

            # Recursively count files and folders within the folder
            files_in_folder, folder_in_folder = count_files_and_folders(item_path)
            files_count += files_in_folder
            folders_count += folder_in_folder

    return files_count, folders_count


# Call the function to count files and folders in the directory
total_files, total_folders = count_files_and_folders(main_directory)
print(f"The total files in the directory is: {total_files}")
print(f"The total folders in the directory is: {total_folders}")
