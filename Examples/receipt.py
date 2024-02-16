# Import the csv module
import csv

# Define a function to read a CSV file into a dictionary
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.

    Return: a compound dictionary that contains the contents of the CSV file.
    """
    # Create an empty dictionary
    dictionary = {}

    # Open the file for reading
    with open(filename, "r") as file:
        # Create a csv reader object
        reader = csv.reader(file)

        # Loop through each row in the file
        for row in reader:
            # Get the key from the specified column index
            key = row[key_column_index]

            # Add the key and the row as a value to the dictionary
            dictionary[key] = row

    # Return the dictionary
    return dictionary

# Define a function to print a receipt for a customer's order
def print_receipt():
    """Print a receipt for a customer's order."""

    # Read the products.csv file into a dictionary
    products_dict = read_dictionary("products.csv", 0)

    # Print a header for the receipt
    print("Requested Items")

    # Open the request.csv file for reading
    with open("request.csv", "r") as file:
        # Create a csv reader object
        reader = csv.reader(file)

        # Skip the first line of the file
        next(reader)

        # Loop through each row in the file
        for row in reader:
            # Get the product number and quantity from the row
            product_number = row[0]
            quantity = row[1]

            # Find the corresponding item in the products dictionary
            item = products_dict[product_number]

            # Get the product name and price from the item
            product_name = item[1]
            product_price = item[2]

            # Print the product name, quantity, and price
            print(f"{product_name}: {quantity} @ {product_price}")

# Call the print_receipt function
if __name__ == "__main__":
    print_receipt()
