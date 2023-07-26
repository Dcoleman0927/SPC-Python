# Denzel Coleman COP1000
# Looped_Rows.py
# Collaborators: None.

# Create a program that displays the numbers 0 through 9, starting with
# the number 0 and adding 1 number per row utilizing nested loops

def main():

    # Assign a variable rows to determine the amount of
    # rows to display.
    rows = 9

    # Create the outer for loop within the range of number of rows,
    # what number to start with, and how many to add per row.
    
    for a in range(0, rows + 1, 1):

    # Create the inner for loop displaying the number 0 first,
    # and adding one to each row and print it
        for b in range (0, a + 1):
            print (b, end= '')
        print ("")

    # Repeat the prior loop
    for a in range(0, rows + 1, 1):
        for b in range (0, a + 1):
            print (b, end= '')

        print ("")

    # Repeat the prior loop
    for a in range(0, rows + 1, 1):
        for b in range (0, a + 1):
            print (b, end= '')

        print ("")
    

main()
