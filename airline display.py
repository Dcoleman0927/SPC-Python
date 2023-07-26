# airline_display
# Collaborators: None.
# This program reads the text file created in program 6_1
# and displays the data with the reduced and sale prices.

def main():

    # Open the file for reading
    air_file = open('airline.txt','r')


    # Read the first line from the file
    des = air_file.readline()

    # Display the columns
    print(f'{"DESTINATION":<15} {"REG.PRICE":<10} {"REDUCED":<10} {"SALE PRICE":<10}')

    # If a destination was read, continue processing.
    while des != '':

        # Read the price and discounts
        price = int(air_file.readline())
        discount = int(air_file.readline())
        
        # Strip the newlines from the price field.
        des = des.rstrip('\n')

        # Calculate the reduced price
        reduced = price * (discount /100)
        
        # Calculate discounted price
        new_price = price * (1 - (discount / 100))
        
        # Display the record
        print(f'{des:<15} {price:<12.2f} {reduced:<12.2f} {new_price:<12.2f}')

        # Read the name field of the next record
        des = air_file.readline()

    # Close the file
    air_file.close()



# Call the main function
if __name__ == '__main__':
    main()
