# Denzel Coleman COP1000
# Smallest_Integer.py
# Collaborators: None

# Create a program that prompts the user to enter three integers.
# The program should be able to determine which integer inputted out of
# the three is the smallest.
def main():

    # Assign variables num1, num2, and num3 that represent the numbers being
    # inputted by the user.
    num1 = int(input('Enter the first number ==> '))
    num2 = int(input('Enter the second number ==> '))
    num3 = int(input('Enter the third number ==> '))

    # Nested decision blocks that determine which number is the smallest
    # of the three inputs.
    
    if num1 < num2 and num1 < num3: #If number 1 is less than number 2 and number 3, it is the smallest.
        print(f'{num1} is the smallest')
    else:
        if num2 < num1 and  num2 < num3: # Proper indentation that shows nested decision block.
            # If number 2 is less than number 1 and number 3, it is the smallest.
            print(f'{num2} is the smallest')
        else:
            if num3 < num1 and num3 < num2: # Proper indentation that shows nested decision block.
                print(f'{num3} is the smallest') #If number 3 is less than number 1 and number 2, it is the smallest.

main()
