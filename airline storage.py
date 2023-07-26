# airline_storage.py
# Collaborators: None.
# Create a program that use a while loop to store to a file, the names of
# destinations, regular prices and price reductions (percents) for selected
# flights in the promotion.

def main():

    # Open a file for writing.
    file = open('airline.txt','w')

    # Prompt the user to enter a destination.
    des = input('Enter destination name or Enter to quit ')

    # While loop whenever a destination has been entered.
    while des != '':
        price = int(input("Enter flight's regular price "))
        discount = int(input('Enter reduction percent for sale '))

        # Writes the data as a record to the file name.
        file.write(des + '\n')
        file.write(str(price) + '\n')
        file.write(str(discount) + '\n')

        # The loop repeats by entering another destination
        des = input('Enter destination name or Enter to quit ')

    # Close the file.
    file.close()
    print('File was created')
    


# Call the main function
if __name__ == '__main__':
    main()
