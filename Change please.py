# Change_please.py
# Collaborators: None.

# Write a program that prompts the user to enter a dollar amount
# less than or equal to 50 and provide change.

def main():

    # Assign a variable named TOTAL that holds the value of 50
    # which represents the dollar bill the user is paying with
    # Assign a variable named cost where the user will input
    # the cost of the item
    TOTAL = 50
    cost = int(input( "Enter the cost in dollars: "))

    # Assign a variable named dollars to equal the dollar bill being used to
    # purchase the item, subtracted by the cost.
    dollars = TOTAL - cost
    
    # Print a statement that shows bills being dispensed.
    print('\nBills dispensed as change:')

    # Assign a variable that calculates how many 20 dollar bills to give
    # back to the customer and print a statement showing how many.
    twenty = dollars // 20
    print(f'$20 - {twenty}')

    # Do the math
    dollars = dollars - twenty * 20

    # Assign a variable that calculates how many 10 dollar bills to give
    # back to the customer and print a statement showing how many.
    ten = dollars // 10
    print(f'$10 - {ten}')

    # Do the math
    dollars = dollars - ten * 10
    
    # Assign a variable that calculates how many 5 dollar bills to give
    # back to the customer and print a statement showing how many.
    five = dollars // 5
    print(f'$5  - {five}')

    # Do the math
    dollars = dollars - five * 5
    
    # Assign a variable that calculates how much 1 dollar bills to give
    # back to the customer and print a statement showing how many.
    one = dollars // 1
    print(f'$1  - {one}')

    

main()
