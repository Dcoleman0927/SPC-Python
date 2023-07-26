# Denzel Coleman COP1000
# COllaborators: None.

def main():

    # Prompt the user to enter the budget of calories they would like to stay under
    WEEKLY_BUDGET = int(input('Enter your weekly caloric budget ==> '))
    
    # Assign a variable calories to represent the amount of calories for a meal or enter 0 to quit
    calories = int(input('Enter calories for a meal (as an integer or 0 to quit) ==> '))

    # Assign a variable total_calories to represent the addition of each calories inputted.
    total_calories = 0

    # Assign a variable meals to represent each meal being entered
    meals = 0


    # While calories does not equal 0
    while calories != 0:

    # Increase the counter for each meal by 1
        meals += 1
        
    # Calculate each calorie being inputted
        total_calories += calories

    # Continue the loop with inputting another calories
        calories = int(input('Enter calories for a meal (as an integer or 0 to quit) ==> '))

    # if calories DOES equal 0     
    else:

         # if the total calories is greater than the weekly budget,
         # let the user know how many meals they have entered
         # and how much they went over in calories.
        if total_calories > WEEKLY_BUDGET:
            print(f'You entered {meals} meals')
            print(f'You are over plan by {total_calories - WEEKLY_BUDGET}')


         # if the total calories is less than the weekly budet,
         # let the user know how many meals they have entered
         # and how much they were under in calories.
        elif total_calories < WEEKLY_BUDGET:
            print(f'You entered {meals} meals')
            print(f'You are under plan by {WEEKLY_BUDGET - total_calories}')

         # if the total calories is equal to the weekly budget,
         # let the user know how many meals they have entered
        elif total_calories == WEEKLY_BUDGET:
            print(f'You entered {meals} meals')
            print(f'Right on budget!')
            print('')

        

main()
