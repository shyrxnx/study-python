max_books = 5
num_book = 0


# Function to add new book
def add_book(title, author, quantity):
    global num_book
    if num_book < max_books:
        title[num_book] = input("Enter book name: ")
        author[num_book] = input("Enter book author: ")
        quantity[num_book] = int(input("Enter book quantity: "))
        num_book += 1
        print("Book added successfully!\n")
    else:
        print("\nCannot add anymore.\n")


# Function to search for a book by title or author
def search_book(title, author, quantity):
    search_option = int(input("\n\nDo you want to search book by:\n1. Title\n2. Author\nEnter your choice: "))
    if search_option == 1:
        search_title = input("Enter book title: ")
        found = False
        for i in range(num_book):
            if search_title == title[i]:
                print("\n\nTitle: ", title[i])
                print("Author: ", author[i])
                print("Quantity: ", quantity[i], "\n")
                found = True
        if not found:
            print("\nBook not found!\n")
    elif search_option == 2:
        search_author = input("Enter book author: ")
        found = False
        for i in range(num_book):
            if search_author == author[i]:
                print("\n\nTitle: ", title[i])
                print("Author: ", author[i])
                print("Quantity: ", quantity[i], "\n")
                found = True
        if not found:
            print("\nBook not found!\n")
    else:
        print("Invalid choice! Exiting the program.......")


# Function to list all books in the library
def list_books(title, author, quantity):
    print("\n\nCurrent books in the library:\n")
    for i in range(num_book):
        print("\n\nTitle: ", title[i])
        print("Author: ", author[i])
        print("Quantity: ", quantity[i], "\n", "=" * 50)


# Function to update the quantity of `a book
def update_quantity(title, quantity):
    search_title = input("\n\nWhat book do you want to change quantity of?\nEnter title: ")
    found = False
    for i in range(num_book):
        if search_title == title[i]:
            print("\nCurrent quantity: ", quantity[i])
            quantity[i] = int(input("Enter new quantity: "))
            print("Quantity updated successfully!\n")
            found = True
    if not found:
        print("Book not found!\n")


# Arrays to store book information
titles = [""] * max_books
authors = [""] * max_books
quantities = [0] * max_books

# Main menu loop
while True:
    print("Choose: \n1. Add book\n2. Search book\n3. List books\n4. Update quantity\n5. Exit")
    option = int(input("Enter your choice: "))
    if option == 1:
        add_book(titles, authors, quantities)
    elif option == 2:
        search_book(titles, authors, quantities)
    elif option == 3:
        list_books(titles, authors, quantities)
    elif option == 4:
        update_quantity(titles, quantities)
    elif option == 5:
        print("Exiting the program...........")
        break
    else:
        print("\nInvalid choice!\n")

'''
I made this project first in C++ in preparation for my Final exam in Computer 
Programming I. I decided to recreate this project in Python to test my understanding
of arrays and functions.
'''