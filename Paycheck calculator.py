# Denzel Coleman COP1000
# Paycheck_calculator.py
# Collaborators: None.
# Write a program that prompts the user to enter their hourly pay rate,
# weekday hours worked, and weekend hours worked.
# Calculate and print the regular pay, overtime pay, weekend pay and total pay
# for the user.
def main():

    # Assign variables that prompt the user to enter
    # their hourly pay rate (hourly_pay), weekday hours (weekday_hours),
    # and weekend hours (weekend_hours)
    hourly_pay = float(input('Enter the hourly pay rate '))
    weekday_hours = float(input('Enter the weekday hours worked last week '))
    weekend_hours = float(input('Enter the weekend hours worked last week '))

    # Create an if statement that executes if the user enters less than
    # or equal to 40 hours worked, then calculate the math for variable reg_hours
    # being regular hours being equal to the amount of weekday hours multipled
    # by the users hourly pay.
    if weekday_hours <= 40:
        reg_hours = weekday_hours * hourly_pay

    # Create an if else statement that executes if the user enters over 40
    # hours worked, then calculate the regular hours worked being 40 multipled
    # by the users hourly pay.
    # Then, assign a variable for overtime pay, ot_pay, being the amount of
    # weekday hours worked minus 40 which gives us the amount of over time hours
    # multiplied by 1.5 (for amount of pay increase)
    # multiplied by the users hourly pay.
    if weekday_hours > 40:
        reg_hours = 40 * hourly_pay
        ot_pay = (weekday_hours - 40) * (1.5 * hourly_pay)
    else:

    # Else statement if the hours are not over 40, then overtime pay equals 0.
            ot_pay = 0

    # Assign a variable weekend_pay that calculates the pay the user is receiving
    # which is double pay.
    weekend_pay = weekend_hours * 2

    # Create an if statement that executes if the user has worked 1 or more
    # hours on the weekend. Then calculate the weekend pay which is the amount
    # of weekend hours multiplied by hourly pay multipled by 2.
    if weekend_hours > 1:
        weekend_pay = (weekend_hours * hourly_pay) * 2

    # Assign a variable total_pay that calculates the users total pay
    # which adds the regular hours worked plus any overtime and weekend time worked.
    total_pay = reg_hours + ot_pay + weekend_pay


    # Print statements that show each pay type including the total pay.
    print(f'Regular pay: ${reg_hours:,.2f}')
    print(f'Overtime pay: ${ot_pay:,.2f}')
    print(f'Weekend pay: ${weekend_pay:,.2f}')
    print(f'Total pay: ${total_pay:,.2f}')
    
main()
