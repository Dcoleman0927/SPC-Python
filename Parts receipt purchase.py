# Denzel Coleman COP1000
# Parts_receipt_purchase.py
# Create a program that operates like a cashier terminal in an auto parts store.
# Prompt the user for the number of different items being purchased and then loop.
# In the loop, prompt the item description, part number, price and quantity of each item being purchased.
# These four values should be passed as arguments to a custom function that is defined within a separate module file.
# The imported function should print the subttotal for the item and return it to main.
# The total should be printed in main after the loop ends.

import parts_receipt_import

def main():

    # Prompt the user for how many different items are being purchased.
    purchases = int(input('How many different items are being purchased? '))

    # Assign a variable parts to represent the addition of each item being purchased
    parts = 0

    # Start a counter for the total price to be added
    total_price = 0
    
    # Start the loop for the amount of items being purchase
    for parts in range(purchases):
        description = input(f'Enter the description of item {parts + 1} ')
        part_num = int(input(f'Enter part number of item {parts + 1} '))
        price = int(input(f'Enter price of item {parts + 1} '))
        quantity = int(input(f'Enter the quantity for item {parts + 1} '))
        subtotal = quantity * price

        # Add the each subtotal within the loop
        total_price = total_price + subtotal
        parts_receipt_import
        print(f'Item: {description}, Part Number: {part_num}, subtotal: ${subtotal:.2f} ')
        print('')
      
                        
        
    # After the loop is completed, display the Total price of all items being purchased
    # which is calculated by multiplying the subtotal and the amount of parts that was purchased.
    
    print(f'Your total is ${total_price:.2f}')

    # Dunders test
if __name__ == '__main__':

    main()
