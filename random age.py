# random_age.py
# Create a program that presents a list of 100 random ages in descending order.
# Display the oldest person, youngest person, average age, number of minors,
# number of seniors and how many college-age adults in the survey
# Collaborators: None.
import random


def main():

    # Create an empty list.
    mylist = []

    # For loop that presents a list of 100 random
    # integers from 1 to 100.
    for i in range (1,101):
        x = random.randint(1,100)
        mylist.append(x)

    # Call the sortlist function
    sortlist(mylist)

    # Calculate the average age from the random integer list.
    average = sum(mylist)/len(mylist)

    # Display the oldest persons age.
    print('Oldest Person: ', max(mylist))

    # Display the youngest persons age.
    print('Youngest Person: ',min(mylist))

    # Display the average age.
    print(f'Average: {average:.2f}')


    # Creat a count for minor ages and senior ages
    minor_count = 0
    senior_count = 0

    # Create a for loop that counts +1 for all ages under 18
    # and also counts +1 for ages over 65.
    for num in mylist:
        if num < 18:
            minor_count += 1
        elif num > 65:
            senior_count += 1
    # Print the minor and senior ages
    print(f'Number of minors is: {minor_count}')
    print(f'Number of seniors is: {senior_count}')

    # Create a count for college students and a for loop
    # that counts +1 for every age over 18 but greater than or
    # equal to 21.
    college_count = 0
    for num in mylist:
        if num > 18 and num <= 21:
            college_count += 1
    print(f'There were {college_count} college-age adults in the survey')

    # Sortlist function that sorts the list in descending order,
    # prints that list, and returns it back to the main function.
def sortlist(mylist):
    mylist2 = mylist
    mylist2.sort(reverse=True)
    print(*mylist, sep = ', ')
    return sortlist


    


    
main()
        
