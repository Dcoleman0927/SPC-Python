# program2_1.py
# Denzel Coleman SPC ID# 2436299
# Collaborators: None.

# Write a program that converts feet to fathoms.

def main():
    
    # Assign a variable called feet and assign it to a float function
    # that prompts the user to input the amount of feet they want converted.
    # Get the user input.
    feet = float(input('Enter the feet '))

    # Assign a variable fathom to equal the feet variable divided by 6 to
    # convert feet into fathoms
    # Do the math conversion for feet to fathoms
    fathom = feet/6

    # Create a print statement that contains a string that prints
    # the result of the feet to fathom conversion
    print(f'{feet} feet are {fathom:,.3f} fathoms')

main()
