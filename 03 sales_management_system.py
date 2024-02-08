"""Sales Management System: Create a Python program for managing sales. Allow users to input
sales transactions with details like product name, quantity sold, and total revenue.
Implement functions to add new transactions, display sales details for a specific product,
and calculate the overall sales.

Reflections.... few points to consider:
1. Input Validation: You might want to add input validation to ensure that the user enters valid data,
   especially when inputting quantity sold and price.
2. Documentation: Adding comments or docstrings to your functions can improve code readability
   and make it easier for others (and yourself) to understand your code's purpose.
3. Error Handling: Your code currently handles the case when a product is not found during the
   calculation of product sales. Consider adding error handling for other potential issues, such
   as invalid inputs or division by zero.

Note: This project is kind of like the library management system. The difference lies in the
array and the functions that was used/made.
"""

max_products = 5
num_product = 0


def add_transaction(name, quantity, price):
    global num_product
    if num_product < max_products:
        name.append(input("Enter product name: "))
        quantity.append(int(input("Enter quantity sold: ")))
        price.append(float(input("Enter price of the product: ")))
        num_product += 1

        print("\nProduct added successfully!\n")
    else:
        print("\nFull, cannot add anymore!\n")


def calculate_sales(name, quantity, price):
    search_name = input("\nEnter the product you want to learn the sales of: ")
    found = False
    for i in range(num_product):
        if search_name == name[i]:
            print(f"\nProduct name: {name[i]}")
            total_sales = quantity[i] * price[i]
            print(f"Total sales: ₱{total_sales}\n")
            found = True
    if not found:
        print("\nProduct not found in the inventory.\n")


def overall_sales(name, quantity, price):
    total_sales = 0
    for i in range(len(name)):
        total_sales += quantity[i] * price[i]
    print(f"\nOverall Sales: ₱{total_sales}\n")


names = []
quantities = []
prices = []

while True:
    option = int(
        input("Choose:\n1. Add transaction\n2. Calculate a product sales\n3. Calculate total sales\nEnter choice: "))
    if option == 1:
        add_transaction(names, quantities, prices)
    elif option == 2:
        calculate_sales(names, quantities, prices)
    elif option == 3:
        overall_sales(names, quantities, prices)
