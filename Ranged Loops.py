# Denzel Coleman COP1000
# Ranged_loops.py
# Collaborators: None.

# Create a program that uses a for loop that displays numbers 100 through 200
# that are divisible by 3, 5, and that 3 and 5 both share.

def main():

    # Find the numbers within the range of 100-200
    for num in range (100,201):

    # Display the range of numbers and if the number is divisible by both
    # 5 and 3, then print World Cup!
    
        if num % 5 == 0 and num % 3 == 0:
            print(f'{num} World Cup!')

    # If the number is divisible by 5, print World  
        elif num % 5 == 0:
            print(f'{num} World')

    # If the number is divisible by 3, print Cup
        elif num % 3 == 0:
            print(f'{num} Cup')

        

    

    

main()
